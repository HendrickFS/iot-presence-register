from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import rfidLog, employee
from .api.serializers import rfidLogSerializer, employeeSerializer


def index(request):
    return render(request, 'rfidLog/index.html')

class logsAPIView(APIView):
    def get(self, request):
        logs = rfidLog.objects.all()
        serializer = rfidLogSerializer(logs, many=True)
        return Response(serializer.data)
    
class logsByEmployeeAPIView(APIView):
    def get(self, request, rfid):
        logs = rfidLog.objects.filter(employee=rfid)
        serializer = rfidLogSerializer(logs, many=True)
        return Response(serializer.data)

class employeesAPIView(APIView):
    def get(self, request):
        employees = employee.objects.all()
        serializer = employeeSerializer(employees, many=True)
        return Response(serializer.data)
    
class presentsAPIView(APIView):
    def get(self, request):
        employees = employee.objects.all()
        presents = []
        for emp in employees:
            logs = rfidLog.objects.filter(employee=emp.rfid)
            if logs.count() > 0:
                if logs[0].type == 'IN':
                    presents.append(emp)
        serializer = employeeSerializer(presents, many=True)
        return Response(serializer.data)
    

def employeesList(request):
    employees = employee.objects.all()
    for emp in employees:
        logs = rfidLog.objects.filter(employee=emp.rfid)
        if logs.count() > 0:
            if logs[logs.count() - 1].type == 'IN':
                emp.present = True
            else:
                emp.present = False
        else:
            emp.present = False
    return render(request, 'rfidLog/employeesList.html', {'employees': employees})
    
def logsList(request):
    logs = rfidLog.objects.all()
    return render(request, 'rfidLog/logsList.html', {'logs': logs})