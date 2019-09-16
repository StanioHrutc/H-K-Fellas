from django.db import models

# Create your models here.

class Hackathon(models.Model):
    title      = models.CharField(max_length=100, unique=True)
    info       = models.TextField(unique=False)
    when       = models.CharField(max_length=30, unique=False, default='')
    price      = models.CharField(max_length=30, unique=False, default='')
    img        = models.TextField()
    links      = models.TextField()

    def __str__(self):
        return self.title