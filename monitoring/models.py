from django.db import models
from django.core.validators import RegexValidator
import uuid

class SamsungBPABloodPressureDevice(models.Model):
    eui = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    model = models.CharField(max_length=10)
    version = models.CharField(max_length=10)
    bp_sys = models.PositiveSmallIntegerField()
    bp_dia = models.PositiveSmallIntegerField()
    fraud = models.BooleanField(default=False)
    ts = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Device {self.model} ({self.eui}) - {self.bp_sys}/{self.bp_dia} mmHg - created at : {self.ts}"

class SamsungX1SHeartRateDevice(models.Model):
    eui = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    model = models.CharField(max_length=10)
    version = models.CharField(max_length=10) 
    hr = models.PositiveSmallIntegerField()
    fraud = models.BooleanField(default=False)
    ts = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Device {self.model}/{self.version} ({self.eui}) - heart rate {self.hr} pulse per minute - created at : {self.ts}"

class PolarMX2HeartRateDevice(models.Model):
    eui = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    fw = models.CharField(max_length=10)
    pulse = models.FloatField()
    fraud = models.BooleanField(default=False)
    ts = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Device {self.fw} ({self.eui}) - heart rate {self.pulse} pulse per second - created at : {self.ts}"