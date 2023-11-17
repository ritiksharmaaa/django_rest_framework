from django.db import models

# Create your models here.
class Student_data(models.Model):
    name = models.CharField( max_length=150)
    last_name = models.CharField( max_length=150)
    roll= models.IntegerField()
    city = models.CharField( max_length=150 )
    passby = models.CharField( max_length=150 )

