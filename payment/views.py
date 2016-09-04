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
	if (request.method=="GET"):
		if(payment_data_row.flag==0):
			return render(request,'payment/payment.html')
		else:
			return HttpResponseRedirect("/home")
	if(request.method=="POST"):
		n=random.randint(11,99) 
		domain_type=payment_data_row.domain_type
		amount=domain_data.objects.get(domain_type=domain_type).amount
		setattr(payment_data_row,'last_transaction_id',str(request.user)+str(n))
		payment_data_row.save()
		key='YSLeH0'		
		test_key="JBZaLc"
		txnid=str(request.user)+str(n)
		amount=str(float(amount))
		productinfo="domain_type"+str(domain_type)
		firstname="aditya"
		email="aditya999123@gmail.com"
		phone="7587485272"
		surl="http://127.0.0.1:8000/home/"
		furl="http://127.0.0.1:8000/home/"
		service_provider="payu_paisa"
		udf1="a"
		udf2="b"
		udf3="c"
		udf4="d"
		udf5="e"
		salt="wErVRybo"
		test_salt='GQs7yium'
		to_encode=key+'|'+txnid+'|'+amount+'|'+productinfo+'|'+firstname+'|'+email+'|||||||||||'+salt
		hex_dig=hashlib.sha512(to_encode).hexdigest().lower()
		print to_encode
		json={
		"key":key,
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
		return HttpResponse(requests.post(url,json=json,data=json,headers=head))#HttpResponse ('aa')
'''		
def Home(request):
	MERCHANT_KEY = "JBZaLc"
	key="JBZaLc"
	SALT = "GQs7yium"
	PAYU_BASE_URL = "https://test.payu.in/_payment"
	action = ''
	posted={}
	for i in request.POST:
		posted[i]=request.POST[i]
	hash_object = hashlib.sha256(b'randint(0,20)')
	txnid=hash_object.hexdigest()[0:20]
	hashh = ''
	posted['txnid']=txnid
	hashSequence = "key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10"
	posted['key']=key
	hash_string=''
	hashVarsSeq=hashSequence.split('|')
	for i in hashVarsSeq:
		try:
			hash_string+=str(posted[i])
		except Exception:
			hash_string+=''
		hash_string+='|'
	hash_string+=SALT
	hashh=hashlib.sha512(hash_string).hexdigest().lower()
	action =PAYU_BASE_URL
	if(posted.get("key")!=None and posted.get("txnid")!=None and posted.get("productinfo")!=None and posted.get("firstname")!=None and posted.get("email")!=None):
		return render_to_response('current_datetime.html',RequestContext(request,{"posted":posted,"hashh":hashh,"MERCHANT_KEY":MERCHANT_KEY,"txnid":txnid,"hash_string":hash_string,"action":"https://test.payu.in/_payment" }))
	else:
		return render_to_response('current_datetime.html',RequestContext(request,{"posted":posted,"hashh":hashh,"MERCHANT_KEY":MERCHANT_KEY,"txnid":txnid,"hash_string":hash_string,"action":"." }))
		'''