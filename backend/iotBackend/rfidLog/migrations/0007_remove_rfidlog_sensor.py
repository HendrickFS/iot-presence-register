# Generated by Django 5.1.3 on 2024-11-22 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rfidLog', '0006_sensor_rfidlog_sensor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rfidlog',
            name='sensor',
        ),
    ]