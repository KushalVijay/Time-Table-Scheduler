from django.db import models

# Create your models here.

class subject_priority(models.Model):
    sub1 = models.CharField(max_length=100)
    sub2 = models.CharField(max_length=100)
    sub3 = models.CharField(max_length=100)
    sub4 = models.CharField(max_length=100)
    sub5 = models.CharField(max_length=100)