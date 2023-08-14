from django.db import models

# Create your models here.
class Printer(models.Model):
    location = models.CharField(max_length=40, blank=False, primary_key=True)
    dns = models.CharField(max_length=40)
    ip = models.CharField(max_length=15)
    manufacter = models.CharField(max_length=40)
    model = models.CharField(max_length=40)

class Connection(models.Model):
    user = models.CharField(max_length=40, blank=False, primary_key=True)
    location = models.CharField(max_length=40)
    rdp = models.BooleanField(default=True)
    ip = models.CharField(max_length=15)