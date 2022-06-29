from turtle import title
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.db import models

class BlogPost(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=250, verbose_name= 'Blog Title')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title