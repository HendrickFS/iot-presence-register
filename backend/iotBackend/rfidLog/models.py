from django.db import models

class employee(models.Model):
    rfid = models.CharField(max_length=10, primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class rfidLog(models.Model):
    types = [
        ('IN', 'IN'),
        ('OUT', 'OUT')
    ]

    employee = models.ForeignKey(employee, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=3)

    def __str__(self):
        return self.employee.name + " " + str(self.timestamp)