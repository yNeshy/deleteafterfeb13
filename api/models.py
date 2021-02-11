from djongo import models

# Create your models here.
class Stocks(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        app_label = 'api'

class History(models.Model):
    stock = models.CharField(max_length=10)
    value = models.IntegerField()

    class Meta:
        app_label = 'api'