import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from control.models import ScreenControl


# Yardımcı fonksiyon: Aktif şehir al
def get_active_city():
    active_config = ScreenControl.objects.filter(is_active=True).order_by('-updated_at').first()
    if active_config is None or not active_config.city or not active_config.city.strip():
        return 'ANKARA'
    return active_config.city.strip().upper()


# Aktif şehir API'si
class ActiveCityView(APIView):
    def get(self, request):
        city = get_active_city()
        return Response({"city": city}, status=status.HTTP_200_OK)


# Akaryakıt fiyatları API'si
class FuelPriceView(APIView):
    def get(self, request):
        city = get_active_city()
        try:
            r = requests.get(f"https://hasanadiguzel.com.tr/api/akaryakit/sehir={city}", timeout=10)
            data = parse_fuel(r)
            return Response(data, status=status.HTTP_200_OK)
        except requests.RequestException as e:
            return Response(
                {"error": "Harici API'ye erişilemedi.", "detail": str(e)},
                status=status.HTTP_503_SERVICE_UNAVAILABLE
            )


# API yanıtını ayrıştır
def parse_fuel(r):
    if r.status_code != 200:
        return fuel_data_none()

    try:
        the_data = r.json()
        first_key = list(the_data["data"].keys())[0]
        item = the_data["data"][first_key]
        return {
            "Benzin": parse_float(first_key),
            "Motorin Eurodiesel": parse_float(item.get("Gazyagi_TL/lt")),
            "Motorin Excellium Eurodiesel": parse_float(item.get("Motorin(Eurodiesel)_TL/lt")),
            "Otogaz": parse_float(item.get("Kalorifer_Yakiti_TL/kg")),
        }
    except (KeyError, ValueError, TypeError):
        return fuel_data_none()


def fuel_data_none():
    return {
        "Benzin": None,
        "Motorin Eurodiesel": None,
        "Motorin Excellium Eurodiesel": None,
        "Otogaz": None,
    }


def parse_float(data):
    try:
        return float(str(data).replace(",", "."))
    except (ValueError, TypeError):
        return None
