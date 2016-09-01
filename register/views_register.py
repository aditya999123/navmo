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

def login_check(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/home')
    else:
        return login(request)

@csrf_protect
def registration(request):	
	if(request.method=="GET"):
		if request.user.is_authenticated():
			return render(request,'registration/logoutandregistration.html')
		else:
			return render(request,'registration/registration.html')
	if(request.method=="POST"):
		this_refrence_id=str(int(user_data.objects.all().last().refrence_id)+1)
		user_data.objects.create(refrence_id=this_refrence_id,
			first_name=request.POST.get('first_name'),
			last_name=request.POST.get('last_name'),
			number=request.POST.get('number'),
			)
		user = User.objects.create_user(
            username=this_refrence_id,
            password=request.POST.get('password'),
            email=request.POST.get('email'),
            )

		return render(request,
			'registration/continue.html',
			{
			'refrence_id':str(int(user_data.objects.all().last().refrence_id))
			}
			)
@login_required
def home(request):
	return(render(request,"home/home.html"))

@login_required
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
