from django.contrib import admin
from .models import SamsungBPABloodPressureDevice, SamsungX1SHeartRateDevice, PolarMX2HeartRateDevice

admin.site.register(SamsungBPABloodPressureDevice)
admin.site.register(SamsungX1SHeartRateDevice)
admin.site.register(PolarMX2HeartRateDevice)