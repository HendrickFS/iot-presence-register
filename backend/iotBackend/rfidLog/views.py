from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import rfidLog, employee, sensor
from .api.serializers import rfidLogSerializer, employeeSerializer, sensorSerializer


def index(request):
    return render(request, 'rfidLog/index.html')

class logsAPIView(APIView):
    def get(self, request):
        logs = rfidLog.objects.all()
        serializer = rfidLogSerializer(logs, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = rfidLogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
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
    
class sensorsAPIView(APIView):
    def get(self, request):
        sensors = sensor.objects.all()
        serializer = sensorSerializer(sensors, many=True)
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
    presents = []
    absents = []
    for emp in employees:
        logs = rfidLog.objects.filter(employee=emp.rfid)
        if logs.count() > 0:
            if logs[logs.count() - 1].type == 'IN':
                emp.present = True
                presents.append(emp)
            else:
                emp.present = False
                absents.append(emp)
        else:
            emp.present = False
    employees = presents + absents        
    return render(request, 'rfidLog/employeesList.html', {'employees': employees})
    
def logsList(request):
    logs = rfidLog.objects.all()
    for log in logs:
        timestamp = log.timestamp
        log.timestamp = timestamp.strftime("Data: %d/%m/%Y | Horário: %H:%M:%S")
    return render(request, 'rfidLog/logsList.html', {'logs': logs})

def sensorsList(request):
    sensors = sensor.objects.all()
    return render(request, 'rfidLog/sensorsList.html', {'sensors': sensors})

def index(request):
    return render(request, 'rfidLog/index.html')