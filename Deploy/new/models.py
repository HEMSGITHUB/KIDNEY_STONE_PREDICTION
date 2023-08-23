from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class UserPredictDataModel(models.Model):
    gravity = models.CharField(max_length=100)
    ph = models.CharField(max_length=100)
    osmo = models.CharField(max_length=100)
    cond = models.CharField(max_length=100)
    urea = models.CharField(max_length=100)
    calc = models.CharField(max_length=100)
    target = models.CharField(max_length=100)


def __str__(self):
    return self.gravity, self.ph,self.osmo,self.cond,self.urea,self.calc,self.target

class FeedModel(models.Model):
    Feedback = models.TextField(max_length=100)

    def __str__(self):
        return str(self.Feedback)