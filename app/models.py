
from django.db import models
from django.contrib.auth.models import User

import datetime
from django.utils import timezone
import pytz
# Create your models here.
class Foo(models.Model):
    ph = models.CharField(max_length=50)
    humdit = models.CharField(max_length=50)
    waterTemp = models.CharField(max_length=50)
    temp = models.CharField(max_length=50)
    date = models.DateTimeField(default=timezone.now()
, blank=True)


    def __str__(self):
        return self.name + ' ' + self.email