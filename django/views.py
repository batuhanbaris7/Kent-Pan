from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import ScreenControl
from .serializers import ScreenControlSerializer

# Basit bir API view (kontrol amaçlı kullanılabilir)
@api_view(['GET'])
def hello(request):
    return Response({"message": "Merhaba React!"})

# 🟢 Yeni: Aktif şehir verisini getiren endpoint
@api_view(['GET'])
def get_active_city(request):
    active_config = ScreenControl.objects.filter(is_active=True).order_by('-updated_at').first()
    if active_config and active_config.city:
        return Response({
            "city": active_config.city
        })
    else:
        return Response({
            "city": None
        })

# ScreenControl modelini yöneten ViewSet
class ScreenControlViewSet(viewsets.ModelViewSet):
    queryset = ScreenControl.objects.all()
    serializer_class = ScreenControlSerializer
    permission_classes = [AllowAny]  # Şu an herkes erişebilir, istersen değiştirirsin
