from django.db import models

# Create your models here.
class Post(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    Title = models.CharField(max_length=200)
    Author = models.CharField(max_length=100)
    Content = models.TextField()
    Date = models.DateField()
    Genre = models.CharField(max_length=50)