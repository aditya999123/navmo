from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from .models import *
from importlib import import_module
from django.core.urlresolvers import clear_url_caches
from django.db import models
from django.apps import apps
from django.contrib import admin
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.views import login,logout
from otp.models import otp_data
from payment.models import payment_data
import random
def login_check(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/home')
    else:
        return login(request)
@csrf_protect
def registration(request):	
	if request.user.is_authenticated():
		return HttpResponseRedirect('/logout_and_register/')
	if(request.method=="GET"):
		return render(request,'registration/registration.html')
	if(request.method=="POST"):
		firstname=request.POST.get('firstname')
		lastname=request.POST.get('lastname')
		fathername=request.POST.get('fathername')
		mothername=request.POST.get('mothername')
		dob=request.POST.get('dob')
		gender=request.POST.get('gender')
		tsize=request.POST.get('tsize')
		email=request.POST.get('email')
		pnum=request.POST.get('pnum')
		address=request.POST.get('address')
		school=request.POST.get('school')
		sclass=request.POST.get('sclass')
		exam_group=request.POST.get('exam_group')
		first_prefrence=request.POST.get('sname')
		first_choice=request.POST.get('choices')
		second_choice=request.POST.get('choices1')
		second_prefrence=request.POST.get('sec_name')
		workshop=request.POST.get('workshop')
		mpe=request.POST.get('mpe')
		gender=request.POST.get('gender')


		this_refrence_id=str(int(user_data.objects.all().last().refrence_id)+1)
		if(int(mpe)==1):
			mpe_flag=1
		else:
			mpe_flag=0
		user_data.objects.create(
			refrence_id=this_refrence_id,
			first_name=firstname,
			last_name=lastname,
			number=pnum,
			email=email,
			parent_father=fathername,
			parent_mother=mothername,
			dob=dob,
            tshirt_size=tsize,
            address=address,
            school=school,
            grade=sclass,
            exam_centre_1=first_prefrence,
            exam_centre_2=second_prefrence,
            flag_mpe_student=mpe_flag,
            flag_exam_group=int(exam_group),
            flag_exam_centre_1=int(first_choice),
            flag_exam_centre_2=int(second_choice),
            flag_workshop=int(workshop),
            gender=gender
            )
		print user_data.objects.get(refrence_id=this_refrence_id)
			

		User.objects.create_user(
			username=this_refrence_id,
			password=request.POST.get('password'),
			email=email,
			)

		n=random.randint(1000,9999)
		payment_data.objects.create(refrence_id=this_refrence_id,flag=0,amount=0,domain_type=int(exam_group))
		otp_data.objects.create(refrence_id=this_refrence_id,otp=n,flag=0,number=pnum)
		return render(request,
			'message/message.html',
			{
			'message':'Please note the refrence id \n this will be used for user login'+str(int(user_data.objects.all().last().refrence_id))
			}
			)

@login_required
def home(request):
	if(otp_data.objects.get(refrence_id=str(request.user)).flag==1):
		if(request.method=="POST"):
			return HttpResponseRedirect("/payment/")
		user_data_row=user_data.objects.get(refrence_id=str(request.user))
		json={
		'refrence_id':user_data_row.refrence_id,
		'first_name':user_data_row.first_name,
	    'last_name':user_data_row.last_name,
	    'number':user_data_row.number,
	    'email':user_data_row.email,
	    'parent_father':user_data_row.parent_father,
	    'parent_mother':user_data_row.parent_mother,
	    'dob':user_data_row.dob,
	    'tshirt_size':user_data_row.tshirt_size,
	    'address':user_data_row.address,
	    'school':user_data_row.school,
	    'grade':user_data_row.grade,
	    'gender':user_data_row.gender,
	    'exam_centre_1':user_data_row.exam_centre_1,
	    'exam_centre_2':user_data_row.exam_centre_2,
	    'flag_workshop':user_data_row.flag_workshop,
	    'flag_mpe_student':user_data_row.flag_mpe_student,
	    'flag_exam_group':user_data_row.flag_exam_group,
	    'flag_exam_centre_1':user_data_row.flag_exam_centre_1,
	    'flag_exam_centre_2':user_data_row.flag_exam_centre_2}
	    #as
		if(payment_data.objects.get(refrence_id=str(request.user)).flag==1):
			json['payment_status']="Check Status"
		else:
			json['payment_status']="Pay Now"
		return render(request,"home/home.html",json)
	else:
		return HttpResponseRedirect('/verify_mobile/')

@login_required
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required
def logout_and_register(request):
	return render(request,"message/message.html",{'message':"Pls Logout and register again"})

def start(request):
	return render(request,'start/start.html')