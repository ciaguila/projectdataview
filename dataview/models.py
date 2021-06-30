from django.db import models

# Create your models here.
class Data(models.Model):
    xdata = models.IntegerField()
    ydata = models.IntegerField()
