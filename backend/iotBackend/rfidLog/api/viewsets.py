from rest_framework import viewsets
from rfidLog.api import serializers
from rfidLog.models import employee, rfidLog, sensor

class employeeViewSet(viewsets.ModelViewSet):
    queryset = employee.objects.all()
    serializer_class = serializers.employeeSerializer

class rfidLogViewSet(viewsets.ModelViewSet):
    queryset = rfidLog.objects.all()
    serializer_class = serializers.rfidLogSerializer

class sensorViewSet(viewsets.ModelViewSet):
    queryset = sensor.objects.all()
    serializer_class = serializers.sensorSerializer
