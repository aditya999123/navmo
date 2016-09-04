from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from importlib import import_module
from django.core.urlresolvers import clear_url_caches
from django.db import models
from django.apps import apps
from django.contrib import admin
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.views import login,logout
# Create your views here.
from register.models import user_data
from .models import payment_data,domain_data
import requests
import random

import hashlib

from django.core.urlresolvers import reverse
@login_required
def payment(request):
	payment_data_row=payment_data.objects.get(refrence_id=str(request.user))
	if(payment_data_row.flag==0):
		n=random.randint(11,99)
		user_data_row=user_data.objects.get(refrence_id=str(request.user))
		domain_type=payment_data_row.domain_type
		amount=domain_data.objects.get(domain_type=domain_type).amount
		setattr(payment_data_row,'last_transaction_id',str(request.user)+str(n))
		payment_data_row.save()
		key='YSLeH0'		
		test_key="JBZaLc"
		txnid=str(request.user)+str(n)
		amount=str(float(amount))
		productinfo="domain_type"+str(domain_type)
		firstname=str(user_data_row.first_name)
		email=str(user_data_row.email)
		phone=str(user_data_row.number)
		surl=request.scheme+"://"+request.get_host()+"/"+"payment_success"
		furl=request.scheme+"://"+request.get_host()+"/"+"payment_faliure"
		service_provider="payu_paisa"
		salt="wErVRybo"
		test_salt='GQs7yium'
		test_key="fB7m8s"
		test_salt="eRis5Chv"
		to_encode=test_key+'|'+txnid+'|'+amount+'|'+productinfo+'|'+firstname+'|'+email+'|||||||||||'+test_salt
		hex_dig=hashlib.sha512(to_encode).hexdigest().lower()
		print to_encode
		json={
		"key":test_key,
		'txnid':txnid,
		"amount":amount,
		"productinfo":productinfo,
		"firstname":firstname,
		"email":email,
		"phone":phone,
		"surl":surl,
		"furl":furl,
		"service_provider":service_provider,
		"hash":str(hex_dig),
		}
		head={"Authorization": "Egmegr2N2HD0Y7rBRcU3GQRuzMH9BZ0z05HZIkex/lo="} 
		print json
		url_test = 'https://test.payu.in/_payment'
		url="https://secure.payu.in/_payment"
		return render(request,'payment/payment.html',json)
	else:
		return HttpResponseRedirect("/home")
@login_required
def payment_success(request):
	return "payment succesful"

@login_required
def payment_faliure(request):
	return "payment failed"	
