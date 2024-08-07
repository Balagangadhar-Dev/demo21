from django.db import models

# Create your models here.
class cars(models.Model):
    model = models.CharField(max_length=30)
    year = models.DateField()
    no_of_doors = models.IntegerField(max_length=2)
    color = models.CharField(max_length=30)
    engine_type = models.CharField(max_length=15)