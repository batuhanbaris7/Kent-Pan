from django.db import models

FUEL_CITIES  = [
    ("ADANA", "ADANA"),
    ("ADIYAMAN", "ADIYAMAN"),
    ("AFYON", "AFYON"),
    ("AGRI", "AGRI"),
    ("AKSARAY", "AKSARAY"),
    ("AMASYA", "AMASYA"),
    ("ANKARA", "ANKARA"),
    ("ANTALYA", "ANTALYA"),
    ("AYDIN", "AYDIN"),
    ("BALIKESIR", "BALIKESIR"),
    ("BARTIN", "BARTIN"),
    ("BATMAN", "BATMAN"),
    ("BILECIK", "BILECIK"),
    ("BOLU", "BOLU"),
    ("BURDUR", "BURDUR"),
    ("BURSA", "BURSA"),
    ("CANAKKALE", "CANAKKALE"),
    ("CANKIRI", "CANKIRI"),
    ("CORUM", "CORUM"),
    ("DENIZLI", "DENIZLI"),
    ("DIYARBAKIR", "DIYARBAKIR"),
    ("DUZCE", "DUZCE"),
    ("EDIRNE", "EDIRNE"),
    ("ELAZIĞ", "ELAZIĞ"),
    ("ERZINCAN", "ERZINCAN"),
    ("ERZURUM", "ERZURUM"),
    ("ESKISEHIR", "ESKISEHIR"),
    ("GAZİANTEP", "GAZİANTEP"),
    ("GIRESUN", "GIRESUN"),
    ("HATAY", "HATAY"),
    ("ISPARTA", "ISPARTA"),
    ("ISTANBUL", "ISTANBUL"),
    ("IZMIR", "IZMIR"),
    ("İÇEL", "İÇEL"),
    ("K.MARAS", "K.MARAS"),
    ("KARABUK", "KARABUK"),
    ("KARAMAN", "KARAMAN"),
    ("KASTAMONU", "KASTAMONU"),
    ("KAYSERI", "KAYSERI"),
    ("KIRIKKALE", "KIRIKKALE"),
    ("KIRKLARELI", "KIRKLARELI"),
    ("KIRSEHIR", "KIRSEHIR"),
    ("KOCAELI", "KOCAELI"),
    ("KONYA", "KONYA"),
    ("KUTAHYA", "KUTAHYA"),
    ("MALATYA", "MALATYA"),
    ("MANISA", "MANISA"),
    ("MARDİN", "MARDİN"),
    ("MUGLA", "MUGLA"),
    ("NEVSEHIR", "NEVSEHIR"),
    ("NİĞDE", "NİĞDE"),
    ("ORDU", "ORDU"),
    ("OSMANIYE", "OSMANIYE"),
    ("RIZE", "RIZE"),
    ("SAKARYA", "SAKARYA"),
    ("SAMSUN", "SAMSUN"),
    ("SIVAS", "SIVAS"),
    ("SİNOP", "SİNOP"),
    ("ŞANLIURFA", "ŞANLIURFA"),
    ("TEKIRDAG", "TEKIRDAG"),
    ("TOKAT", "TOKAT"),
    ("TRABZON", "TRABZON"),
    ("USAK", "USAK"),
    ("VAN", "VAN"),
    ("YALOVA", "YALOVA"),
    ("YOZGAT", "YOZGAT"),
    ("ZONGULDAK", "ZONGULDAK"),
]


class ScreenControl(models.Model):
    title = models.CharField(max_length=100)
    city = models.CharField(max_length=16, choices=FUEL_CITIES, null=False,blank=False)
    temperature = models.CharField(max_length=10, blank=True, null=True)
    weather = models.CharField(max_length=100, blank=True, null=True)
    news = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
