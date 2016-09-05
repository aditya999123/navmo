from __future__ import unicode_literals

from django.db import models


class user_data(models.Model):
    refrence_id=models.CharField(max_length=10,blank=True,null=True)
    first_name=models.CharField(max_length=120,blank=True,null=True)
    last_name=models.CharField(max_length=120,blank=True,null=True)
    number=models.CharField(max_length=120,blank=True,null=True)
    email=models.CharField(max_length=120,blank=True,null=True)
    parent_father=models.CharField(max_length=120,blank=True,null=True)
    parent_mother=models.CharField(max_length=120,blank=True,null=True)
    dob=models.CharField(max_length=120,blank=True,null=True)
    tshirt_size=models.CharField(max_length=120,blank=True,null=True)
    address=models.CharField(max_length=120,blank=True,null=True)
    school=models.CharField(max_length=120,blank=True,null=True)
    grade=models.CharField(max_length=120,blank=True,null=True)
    exam_centre_1=models.CharField(max_length=120,blank=True,null=True)
    exam_centre_2=models.CharField(max_length=120,blank=True,null=True)
    flag_workshop=models.PositiveSmallIntegerField(default=0)
    flag_mpe_student=models.PositiveSmallIntegerField(default=0)
    flag_exam_group=models.PositiveSmallIntegerField(default=0)
    flag_exam_centre_1=models.PositiveSmallIntegerField(default=0)
    flag_exam_centre_2=models.PositiveSmallIntegerField(default=0)