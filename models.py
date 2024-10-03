#Models for learning_tool

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone

#Model voor beheerders
class Beheerder(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='')
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.name

class Docent(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='')
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.name
    
class Student(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='')
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.name