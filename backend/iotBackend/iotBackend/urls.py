"""
URL configuration for iotBackend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from rfidLog.api import viewsets
from rfidLog.views import logsAPIView, employeesAPIView, presentsAPIView, logsByEmployeeAPIView, employeesList, logsList, sensorsAPIView, sensorsList

route = routers.DefaultRouter()

route.register(r'employee', viewsets.employeeViewSet)
route.register(r'rfidLog', viewsets.rfidLogViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(route.urls)),
    path('logs/', logsAPIView.as_view()),
    path('logs/<str:rfid>/', logsByEmployeeAPIView.as_view()),
    path('employees/', employeesAPIView.as_view()),
    path('presents/', presentsAPIView.as_view()),
    path('sensors/', sensorsAPIView.as_view()),

    path('employeesList/', employeesList, name='employeesList'),
    path('logsList/', logsList, name='logsList'),
    path('sensorsList/', sensorsList, name='sensorsList'),
]
