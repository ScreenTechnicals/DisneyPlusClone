from django.db import models

# Create your models here.

class BannerCards(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    content = models.TextField()
    imageurl = models.CharField(max_length=1000)
    targetUrl = models.CharField(max_length=1000)

    def __str__(self):
        return self.title

class Cards(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    imageurl = models.CharField(max_length=1000)
    targetUrl = models.CharField(max_length=1000)

    def __str__(self):
        return self.title

