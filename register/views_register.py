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
import os
from .models import exam_center_data
from django.core.urlresolvers import reverse
def login_check(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/home')
    else:
        return login(request)
@csrf_protect
def registration(request):	
	if request.user.is_authenticated():
		login_display='<li><a href="/logout">Logout</a></li>'
		login_display2=''
		json={
		'login_display':login_display,
		'login_display2':login_display2,
		}
		
		return HttpResponseRedirect('/logout_and_register/',json)
	if(request.method=="GET"):
		json={}
		list_data=''
		for o in exam_center_data.objects.all():
			list_data+='<option value="'+o.exam_center+'">'+o.exam_center+'</option>'
			print o,o.exam_center
			print list_data
		json['list_data']=list_data
		return render(request,'registration/registration.html',json)
	if(request.method=="POST"):
		
		firstname=str(request.POST.get('firstname'))
		lastname=str(request.POST.get('lastname'))
		fathername=str(request.POST.get('fathername'))
		mothername=str(request.POST.get('mothername'))
		dob=str(request.POST.get('dob'))
		gender=str(request.POST.get('gender'))
		tsize=str(request.POST.get('tsize'))
		examcenter=str(request.POST.get('exam_center'))
		print examcenter
		examcenterr=str(request.POST.get('exam_centerr'))
		email=str(request.POST.get('email'))
		pnum=str(request.POST.get('pnum'))
		address=str(request.POST.get('address'))
		school=str(request.POST.get('school'))
		sclass=str(request.POST.get('class'))
		exam_group_1=str(request.POST.get('group_exam_field1'))
		exam_group_2=str(request.POST.get('group_exam_field2'))
		first_preference=str(request.POST.getlist('first'))
		print 'First '+str(request.POST.get('first'))
		print str(request.POST.get('second_preference'))
		print str(request.POST.get('first_school'))
		print str(request.POST.get('second_school'))

		first_choice=str(request.POST.get('first_school'))
		second_choice=str(request.POST.get('second_school'))
		second_preference=str(request.POST.get('second_preference'))
		workshop=str(request.POST.get('workshop'))
		mpe=str(request.POST.get('mpe_student'))
		gender=str(request.POST.get('gender'))
		flag_group_exam1=str(request.POST.get('group_exam1'))
		flag_group_exam2=str(request.POST.get('group_exam2'))
		if flag_group_exam1 == 'None':
				flag_group_exam1='0'
		
		if flag_group_exam2 == 'None':
				flag_group_exam2='0'
		



		image=request.FILES.get('pic').name
		this_refrence_id=str(int(user_data.objects.all().last().refrence_id)+1)
		while True:
			try:
				folder = 'media/'+this_refrence_id+'/'
				os.mkdir(os.path.join(folder))
				break
			except:
				this_refrence_id=this_refrence_id+1
		# full_filename = os.path.join(folder, image)
		# print "full name",full_filename
		#fout = open(folder+image, 'wb+')
		print "image=",image
		fout = open(folder+image, 'w')
		file_content = request.FILES.get('pic').read()
		#for chunk in file_content.chunks():
		fout.write(file_content)
		fout.close()
		
		if(int(mpe)==1):
			mpe_flag=1
		else:
			mpe_flag=0
		user_data.objects.create(
			exam_group_1=exam_group_1,
			exam_group_2=exam_group_2,
			flag_exam_group_1=int(flag_group_exam1),
			flag_exam_group_2=int(flag_group_exam2),
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
            exam_centre_1=examcenter,
            exam_centre_2=examcenterr,
            flag_mpe_student=mpe_flag,
            flag_exam_centre_1=int(first_choice),
            flag_exam_centre_2=int(second_choice),
            flag_workshop=int(workshop),
            gender=gender,
            image=this_refrence_id+'/'+image
            )
		print user_data.objects.get(refrence_id=this_refrence_id)
			

		User.objects.create_user(
			username=this_refrence_id,
			password=request.POST.get('password'),
			email=email,
			)
		if request.user.is_authenticated():
			login_display='<li><a href="/logout">Logout</a></li>'
			login_display2=''
		
		else:
			login_display='<li><a href="/register">Register</a></li>'
			login_display2='<li><a href="/login">Login</a></li>'

		n=random.randint(1000,9999)
		if ((int(flag_group_exam1)==1)and(int(flag_group_exam2)==0)):
			domain_type=1
		if ((int(flag_group_exam1)==0)and(int(flag_group_exam2)==1)):
			domain_type=2
		if ((int(flag_group_exam1)==1)and(int(flag_group_exam2)==1)):
			domain_type=3
		payment_data.objects.create(refrence_id=this_refrence_id,flag=0,amount=0,domain_type=domain_type)
		otp_data.objects.create(refrence_id=this_refrence_id,otp=n,flag=0,number=pnum)
		
		message='Please note the refrence id \n this will be used for user login '+str(this_refrence_id)+'\n <a href="\login" >Please login to continue </a>'
		# ##request.flash['login_display']=login_display
		# ##request.flash['login_display2']=login_display2
		# import urllib

		# #url = reverse('/message/', kwargs={'message': message})
		# print urllib.urlencode(message)
		# print aditya
		request.session['message'] = message
		return HttpResponseRedirect('/message')

@login_required
def home(request):
	if request.user.is_authenticated():
		login_display='<li><a href="/logout">Logout</a></li>'
		login_display2=''
	else:
		login_display='<li><a href="/register">Register</a></li>'
		login_display2='<li><a href="/login">Login</a></li>'
	if(otp_data.objects.get(refrence_id=str(request.user)).flag==1):
		if(request.method=="POST"):
			return HttpResponseRedirect("/payment/")
		user_data_row=user_data.objects.get(refrence_id=str(request.user))
		json={
		'image':user_data_row.image.url,
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
	    'exam_group1':user_data_row.exam_group_1,
	    'exam_group2':user_data_row.exam_group_2,
	    'flag_exam_centre_1':user_data_row.flag_exam_centre_1,
	    'flag_exam_centre_2':user_data_row.flag_exam_centre_2,
	    'login_display':login_display,
	    'ogin_display2':login_display2,
	    }
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
	if request.user.is_authenticated():
		return HttpResponseRedirect("/home")
	else:
		login_display='<li><a href="/register">Register</a></li>'
		login_display2='<li><a href="/login">Login</a></li>'
	return render(request,'start/start.html',{"login_display":login_display,"login_display2":login_display2})

def contactus(request):
	if request.user.is_authenticated():
		login_display='<li><a href="/logout">Logout</a></li>'
		login_display2=''
	else:
		login_display='<li><a href="/register">Register</a></li>'
		login_display2='<li><a href="/login">Login</a></li>'
	return render(request,'contactus/contact_us.html',{"login_display":login_display,"login_display2":login_display2})

def overview(request):
	if request.user.is_authenticated():
		login_display='<li><a href="/logout">Logout</a></li>'
		login_display2=''
	else:
		login_display='<li><a href="/register">Register</a></li>'
		login_display2='<li><a href="/login">Login</a></li>'
	return render(request,'overview/overview.html',{"login_display":login_display,"login_display2":login_display2})

def faqs(request):
	if request.user.is_authenticated():
		login_display='<li><a href="/logout">Logout</a></li>'
		login_display2=''
	else:
		login_display='<li><a href="/register">Register</a></li>'
		login_display2='<li><a href="/login">Login</a></li>'
	return render(request,'faqs/faqs.html',{"login_display":login_display,"login_display2":login_display2})

def message(request):
	message=request.session['message']
	return render(request,'message/message.html',{'message':message})