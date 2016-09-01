from __future__ import unicode_literals

from django.db import models


class payment_data(models.Model):
    refrence_id=models.CharField(max_length=10,blank=True,null=True)
    amount=models.CharField(max_length=120,blank=True,null=True)
    flag=models.PositiveSmallIntegerField(default=0)