from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=90)
    desc = models.TextField(max_length=900)
    pub_date = models.DateTimeField()