from django.db import models

class sensor(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    location = models.CharField(max_length=100)
    enabled = models.BooleanField(default=True) 

    def __str__(self):
        return self.name

class employee(models.Model):
    rfid = models.CharField(max_length=10, primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    icon = models.CharField(max_length=100, default="./assets/person.jpg")

    def __str__(self):
        return self.name

class rfidLog(models.Model):
    employee = models.ForeignKey(employee, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=3)
    sensor = models.ForeignKey(sensor, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return self.employee.name + " " + str(self.timestamp)