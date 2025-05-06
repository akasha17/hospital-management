from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    USERTYPE_CHOICES = [
        ('admin', 'Admin'),
        ('doctor', 'Doctor'),
        ('patient', 'Patient'),
    ]
    usertype = models.CharField(max_length=50, choices=USERTYPE_CHOICES, default="patient")

class Department(models.Model):
    dep_name = models.CharField(max_length=100)

class Doctor(models.Model):
    depid = models.ForeignKey(Department, on_delete=models.CASCADE)
    dcid = models.OneToOneField(User, on_delete=models.CASCADE, limit_choices_to={'usertype': 'doctor'})
    qualification = models.CharField(max_length=100)

class Patient(models.Model):
    depid = models.ForeignKey(Department, on_delete=models.CASCADE)
    pid = models.OneToOneField(User, on_delete=models.CASCADE, limit_choices_to={'usertype': 'patient'})
    age = models.IntegerField()
    address = models.CharField(max_length=100)
    GENDER_CHOICES = [('male', 'Male'), ('female', 'Female')]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=15)  



