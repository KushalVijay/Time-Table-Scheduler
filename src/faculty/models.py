from django.db import models

# Create your models here.
class faculty_info(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    contact = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    experience = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)

    def __str__(self):
        return self.username
