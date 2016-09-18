from __future__ import unicode_literals

from django.db import models

# Create your models here.
class password_reset_otp(models.Model):
    refrence_id=models.CharField(max_length=10,blank=True,null=True)
    number=models.CharField(max_length=120,blank=True,null=True)
    otp=models.PositiveSmallIntegerField(default=0)
    flag=models.PositiveSmallIntegerField(default=0)

