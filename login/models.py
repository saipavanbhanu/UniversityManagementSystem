from django.db import models

# Create your models here.

class Login(models.Model):
    unique_id=models.CharField(max_length=100,primary_key=True)
    password=models.CharField(max_length=50)

    def __str__(self):
        return self.unique_id
