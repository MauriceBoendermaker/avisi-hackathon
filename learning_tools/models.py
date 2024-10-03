from django.contrib.auth.models import User
from django.db import models


# Model voor beheerders
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
    feedback_field = models.TextField(max_length=600)

    def __str__(self):
        return self.name
    

class Werkprocess(models.Model):
    pass

class Criterium(models.Model):
    pass

class Verantwoording(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='verantwoording_owner')

    beoordelaar_1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='verantwoording_beoordelaar_1')
    feedback_1 = models.CharField(max_length=100)
    feedback_1_niveaus = models.CharField(max_length=100)

    beoordelaar_2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='verantwoording_beoordelaar_2')
    feedback_2 = models.CharField(max_length=100)
    feedback_2_niveaus = models.CharField(max_length=100)

    beoordelaar_3 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='verantwoording_beoordelaar_3')
    feedback_3 = models.CharField(max_length=100)
    feedback_3_niveaus = models.CharField(max_length=100)

    def __str__(self):
        return self.owner.username
