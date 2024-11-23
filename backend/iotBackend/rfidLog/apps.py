from django.apps import AppConfig
from threading import Thread
from .serialReader import readSerial


# class RfidlogConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'rfidLog'

#     def ready(self):
#         Thread(target=readSerial, daemon=True).start()
