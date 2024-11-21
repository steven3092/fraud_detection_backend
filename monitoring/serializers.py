from rest_framework import serializers
from .models import SamsungBPABloodPressureDevice, SamsungX1SHeartRateDevice, PolarMX2HeartRateDevice

class SamsungBPABloodPressureDeviceSerializer(serializers.ModelSerializer):
    fraud = serializers.CharField(read_only=True)
    eui = serializers.CharField(read_only=True)
    class Meta:
        model = SamsungBPABloodPressureDevice
        fields = ['eui', 'model', 'version', 'bp_sys', 'bp_dia', 'fraud', 'ts']

class SamsungX1SHeartRateDeviceSerializer(serializers.ModelSerializer):
    fraud = serializers.CharField(read_only=True)
    eui = serializers.CharField(read_only=True)
    class Meta:
        model = SamsungX1SHeartRateDevice
        fields = ['eui', 'model', 'version', 'hr', 'fraud', 'ts']

class PolarMX2HeartRateDeviceSerializer(serializers.ModelSerializer):
    fraud = serializers.CharField(read_only=True)
    eui = serializers.CharField(read_only=True)
    class Meta:
        model = PolarMX2HeartRateDevice
        fields = ['eui', 'fw', 'pulse', 'fraud', 'ts']
