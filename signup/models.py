from django.db import models
class adddata(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)

    class Meta:
        db_table='user'
# Create your models here.
