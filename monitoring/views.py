import logging
from rest_framework.views import APIView
from rest_framework import viewsets

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import SamsungX1SHeartRateDeviceSerializer, PolarMX2HeartRateDeviceSerializer, SamsungBPABloodPressureDeviceSerializer
from .models import SamsungBPABloodPressureDevice, SamsungX1SHeartRateDevice, PolarMX2HeartRateDevice

logger = logging.getLogger(__name__)

class SamsungBPABloodPressureDeviceViews(APIView):
    def post(self, request):
        try:
            base_sys = 100
            structured_data = {
                "model": request.data.get("model"),
                "version": request.data.get("version"),
                "bp_dia": request.data.get("payload").get("bp_dia"),
                "bp_sys": request.data.get("payload").get("bp_sys"),
            }
            serializer = SamsungBPABloodPressureDeviceSerializer(data=structured_data)
            if serializer.is_valid():
                if int(request.data.get("payload").get("bp_sys")) > (base_sys * 1.2):
                    serializer.validated_data['fraud'] = True
                    fraud_reason = f"FRAUD_WARNING: high blood pressure rate detected {request.data.get("payload").get("bp_sys")} mmHg"
                    logger.warning(f"FRAUD_WARNING: Device Samsung BPA - {fraud_reason}")
                    serializer.save()
                    recorded_data = {
                        "eui": serializer.data.get("eui"),
                        "model": serializer.data.get("model"),
                        "version": serializer.data.get("version"),
                        "payload": {
                            "bp_sys": serializer.data.get("bp_sys"),
                            "bp_dia": serializer.data.get("bp_dia"),
                        },
                        "fraud": serializer.data.get("fraud"),
                        "ts": serializer.data.get("ts"),
                    }
                    return Response({"status": "FRAUD_WARNING", "data": recorded_data, "fraud_reason": fraud_reason}, status=status.HTTP_200_OK)
                serializer.validated_data['fraud'] = False
                serializer.save()
                recorded_data = {
                        "eui": serializer.data.get("eui"),
                        "model": serializer.data.get("model"),
                        "version": serializer.data.get("version"),
                        "payload": {
                            "bp_sys": serializer.data.get("bp_sys"),
                            "bp_dia": serializer.data.get("bp_dia"),
                        },
                        "fraud": serializer.data.get("fraud"),
                        "ts": serializer.data.get("ts"),
                    }
                return Response({"status": "SUCCESS", "data": recorded_data})
            else:
                return Response({"status": "ERROR", "data": serializer.errors})
        except SamsungBPABloodPressureDevice.DoesNotExist:
            return Response({"error": "Device not found"}, status=status.HTTP_404_NOT_FOUND)
    def get(self, request, id=None):
        if id:
            sensor = SamsungBPABloodPressureDevice.objects.get(eui=id)
            serializer = SamsungBPABloodPressureDeviceSerializer(sensor)
            return Response({"status": "SUCCESS", "data": serializer.data}, status=status.HTTP_200_OK)
        sensors = SamsungBPABloodPressureDevice.objects.all()
        serializer = SamsungBPABloodPressureDeviceSerializer(sensors, many=True)
        return Response({"status": "SUCCESS", "data": serializer.data}, status=status.HTTP_200_OK)

class SamsungX1SHeartRateDeviceViews(APIView):
    def post(self, request):
        try:
            base_hr = 75
            structured_data = {
                "model": request.data.get("model"),
                "version": request.data.get("version"),
                "hr": request.data.get("payload").get("hr"),
            }
            serializer = SamsungX1SHeartRateDeviceSerializer(data=structured_data)
            if serializer.is_valid():
                if int(request.data.get("payload").get("hr")) > (base_hr * 1.3):
                    serializer.validated_data['fraud'] = True
                    fraud_reason = f"FRAUD_WARNING: High heart rate detected {request.data.get("payload").get("hr")} beats per minutes"
                    logger.warning(f"FRAUD_WARNING: Device Samsung X1S - {fraud_reason}")
                    serializer.save()
                    recorded_data = {
                        "eui": serializer.data.get("eui"),
                        "model": serializer.data.get("model"),
                        "version": serializer.data.get("version"),
                        "payload": {
                            "hr": serializer.data.get("hr"),
                        },
                        "fraud": serializer.data.get("fraud"),
                        "ts": serializer.data.get("ts"),
                    }
                    return Response({"status": "FRAUD_WARNING", "data": recorded_data, "fraud_reason": fraud_reason}, status=status.HTTP_200_OK)
                serializer.validated_data['fraud'] = False
                serializer.save()
                recorded_data = {
                    "eui": serializer.data.get("eui"),
                    "model": serializer.data.get("model"),
                    "version": serializer.data.get("version"),
                    "payload": {
                        "hr": serializer.data.get("hr"),
                    },
                    "fraud": serializer.data.get("fraud"),
                    "ts": serializer.data.get("ts"),
                }
                return Response({"status": "SUCCESS", "data": recorded_data})
            else:
                return Response({"status": "ERROR", "data": serializer.errors})
        except SamsungX1SHeartRateDevice.DoesNotExist:
            return Response({"error": "Device not found"}, status=status.HTTP_404_NOT_FOUND)
    def get(self, request):
        eui = request.query_params.get('eui')
        if eui:
            sensor = SamsungX1SHeartRateDevice.objects.get(eui=eui)
            serializer = SamsungX1SHeartRateDeviceSerializer(sensor)
            return Response({"status": "SUCCESS", "data": serializer.data}, status=status.HTTP_200_OK)
        sensors = SamsungX1SHeartRateDevice.objects.all()
        serializer = SamsungX1SHeartRateDeviceSerializer(sensors, many=True)
        return Response({"status": "SUCCESS", "data": serializer.data}, status=status.HTTP_200_OK)

class PolarMX2HeartRateDeviceViews(APIView):
    def post(self, request):
        try:
            base_hr_in_seconds = 75 / 60
            serializer = PolarMX2HeartRateDeviceSerializer(data=request.data)
            if serializer.is_valid():
                if float(request.data.get('pulse')) > (base_hr_in_seconds * 1.3):
                    serializer.validated_data['fraud'] = True
                    fraud_reason = f"FRAUD_WARNING: High heart rate detected {request.data.get('pulse')} beats per seconds"
                    logger.warning(f"FRAUD_WARNING: Device Polar MX2 - {fraud_reason}")
                    serializer.save()
                    return Response({"status": "FRAUD_WARNING", "data": serializer.data, "fraud_reason": fraud_reason}, status=status.HTTP_200_OK)
                serializer.validated_data['fraud'] = False
                serializer.save()
                return Response({"status": "SUCCESS", "data": serializer.data})
            else:
                return Response({"status": "ERROR", "data": serializer.errors})
        except PolarMX2HeartRateDevice.DoesNotExist:
            return Response({"error": "Device not found"}, status=status.HTTP_404_NOT_FOUND)
    def get(self, request, id=None):
        if id:
            sensor = PolarMX2HeartRateDevice.objects.get(eui=id)
            serializer = PolarMX2HeartRateDeviceSerializer(sensor)
            return Response({"status": "SUCCESS", "data": serializer.data}, status=status.HTTP_200_OK)
        sensors = PolarMX2HeartRateDevice.objects.all()
        serializer = PolarMX2HeartRateDeviceSerializer(sensors, many=True)
        return Response({"status": "SUCCESS", "data": serializer.data}, status=status.HTTP_200_OK)

