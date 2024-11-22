from rest_framework import serializers
from rfidLog.models import employee, rfidLog, sensor

class employeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = employee
        fields = '__all__'

class rfidLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = rfidLog
        fields = '__all__'

class sensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = sensor
        fields = '__all__'