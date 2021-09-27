from django.db import models

# Create your models here.
class StudentModel(models.Model):
    name=models.CharField(max_length=50)
    desc=models.TextField(max_length=500)
    admission_date=models.DateField()
