from django.db import models

# Create your models here.
class empdetails(models.Model):
    ename=models.CharField(max_length=50)
    emno=models.IntegerField()
    email=models.EmailField()

