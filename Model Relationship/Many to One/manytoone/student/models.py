from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    user1=models.ForeignKey(User,on_delete=models.CASCADE)
    post_title=models.CharField(max_length=30)
    post_cat=models.CharField(max_length=30)
    post_publish_date=models.DateField()