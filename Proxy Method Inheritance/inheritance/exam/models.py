from django.db import models

# Create your models here.
class ExamCenter(models.Model):
    cname=models.CharField(max_length=30)
    city=models.CharField(max_length=30)

class Student(ExamCenter):
    class Meta:
        proxy = True