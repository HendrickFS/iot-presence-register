# Generated by Django 5.1.3 on 2024-11-20 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rfidLog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='rfid',
            field=models.CharField(max_length=10, primary_key=True, serialize=False, unique=True),
        ),
    ]
