from django.db import models

# Create your models here.


class Data(models.Model):
    xdata = models.IntegerField()
    ydata = models.IntegerField()

    def __str__(self):
        return (self.xdata, self.ydata)
