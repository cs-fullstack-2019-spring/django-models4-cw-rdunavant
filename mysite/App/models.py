from django.db import models

# Create your models here.
class Mom(models.Model):
    mom_first_name = models.CharField(max_length=10)
    mom_last_name = models.CharField(max_length=15)
    mom_phone_number = models.IntegerField(max_length=10)

def __str__(self):
    return self.mom_name

class Child(models.Model):
    child_first_name = models.CharField(max_length=10)
    child_last_name = models.CharField(max_length=15)
    child_phone_number = models.IntegerField(max_length=10)

class State(models.Model):
    state_name = models.CharField(max_length=12)

class Citizen(models.Model):
    citizen_first_name = models.CharField(max_length=12)
    citizen_last_name = models.CharField(max_length=12)
    citizen_state =models.CharField(max_length=12)