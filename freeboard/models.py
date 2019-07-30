from django.db import models
from datetime import datetime

# Create your models here.


class Post(models.Model):
    user_id = models.IntegerField()
    owner = models.CharField(max_length=20, default="???")
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date_published')
    body = models.TextField()
    views = models.IntegerField()

    def __str__(self):
        return self.title

    def increaseViews(self):
        self.views +=1
        self.save()