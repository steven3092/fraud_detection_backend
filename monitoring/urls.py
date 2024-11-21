from django.urls import path
from .views import SamsungBPABloodPressureDeviceViews, SamsungX1SHeartRateDeviceViews, PolarMX2HeartRateDeviceViews

urlpatterns = [
    path('api/samsung-bpa-blood-pressure/', SamsungBPABloodPressureDeviceViews.as_view()),
    path('api/samsung-bpa-blood-pressure/<int:id>/', SamsungBPABloodPressureDeviceViews.as_view()),
    path('api/samsung-x1s-heart-rate/', SamsungX1SHeartRateDeviceViews.as_view()),
    path('api/samsung-x1s-heart-rate/<int:id>/', SamsungX1SHeartRateDeviceViews.as_view()),
    path('api/polar-mx2-heart-rate/', PolarMX2HeartRateDeviceViews.as_view()),
    path('api/polar-mx2-heart-rate/<int:id>/', PolarMX2HeartRateDeviceViews.as_view()),


]