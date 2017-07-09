from random import randint
from django.db import models
from django.utils import timezone

def random_number():
    return randint(1, 100)

class RandomNumber(models.Model):
  number = models.IntegerField(default=random_number)
  created_at = models.DateTimeField(default=timezone.now)



