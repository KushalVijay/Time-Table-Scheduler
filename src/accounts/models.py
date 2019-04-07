from django.db import models

# Create your models here.

class register(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    password2 = models.CharField(max_length=200)

class login_page(models.Model):
    #email = models.EmailField()
    username = models.CharField(max_length=50,null=True,blank=True)
    password = models.CharField(max_length=200)

class admin_login(models.Model):
    #email = models.EmailField()
    username = models.CharField(max_length=50,null=True,blank=True)
    password = models.CharField(max_length=200)

