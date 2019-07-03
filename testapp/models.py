from django.db import models

# Create your models here.
class Memo(models.Model):
    user_id = models.IntegerField(max_length=20)
    keyword = models.CharField(max_length=30)
    urls = models.TextField(default=None)
    memo = models.TextField(default="")

    def __str__(self):
        return self.keyword
    