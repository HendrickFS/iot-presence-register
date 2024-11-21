from rest_framework import serializers
from rfidLog.models import employee, rfidLog

class employeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = employee
        fields = '__all__'

class rfidLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = rfidLog
        fields = '__all__'