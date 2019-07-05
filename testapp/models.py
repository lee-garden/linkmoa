from django.db import models
import jsonfield

# Create your models here.
class Memo(models.Model):
    user_id = models.IntegerField()
    directory = models.CharField(max_length=20, default="recently")
    display = models.CharField(max_length=10, default="visible")
    keyword = models.CharField(max_length=30)
    urls = models.TextField(default=None)
    memo = models.TextField(default="")

    def __str__(self):
        return self.keyword
    
    def split(urls):
        urlList = urls.split('\n')
        return urlList