from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect,csrf_exempt
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
		setattr(payment_data_row,'amount',str(amount))
		payment_data_row.save()
		key='YSLeH0'		
		test_key="JBZaLc"
		txnid=str(request.user)+str(n)
		amount=str(float(amount))
		productinfo="domain_type"+str(domain_type)
		firstname=str(user_data_row.first_name)
		email=str(user_data_row.email)
		phone=str(user_data_row.number)
		surl=request.scheme+"://"+request.get_host()+"/"+"payment_success/"
		furl=request.scheme+"://"+request.get_host()+"/"+"payment_faliure/"
		service_provider="payu_paisa"
		salt="wErVRybo"
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
		"url":"https://secure.payu.in/_payment",
		}
		head={"Authorization": "Egmegr2N2HD0Y7rBRcU3GQRuzMH9BZ0z05HZIkex/lo="}
		print json
		url_test = 'https://test.payu.in/_payment'
		url="https://secure.payu.in/_payment"
		return render(request,'payment/payment.html',json)
	else:
		url='https://www.payumoney.com/payment/payment/chkMerchantTxnStatus?'
		key='YSLeH0'
		txnid=payment_data_row.last_transaction_id
		json_sent={
		'merchantTransactionIds':txnid,
		'merchantKey':key
		}
		
		head={"Authorization": "Egmegr2N2HD0Y7rBRcU3GQRuzMH9BZ0z05HZIkex/lo="}
		result=requests.request('post',url,json=json_sent,headers=head)
		json={'message':str(HttpResponse(result))}
		return render(request,'message/message.html',json)
@login_required
@csrf_exempt
def payment_success(request):
	status=request.POST["status"]
	firstname=request.POST["firstname"]
	amount=request.POST["amount"]
	txnid=request.POST["txnid"]
	posted_hash=request.POST["hash"]
	key=request.POST["key"]
	productinfo=request.POST["productinfo"]
	email=request.POST["email"]
	salt="wErVRybo"
	try:
		additionalCharges=request.POST["additionalCharges"]
		retHashSeq=additionalCharges+'|'+salt+'|'+status+'|||||||||||'+email+'|'+firstname+'|'+productinfo+'|'+amount+'|'+txnid+'|'+key
	except Exception:
		retHashSeq = salt+'|'+status+'|||||||||||'+email+'|'+firstname+'|'+productinfo+'|'+amount+'|'+txnid+'|'+key
	hashh=hashlib.sha512(retHashSeq).hexdigest().lower()
	if(hashh !=posted_hash):
		status='Invalid Transaction'
	payment_data_row=payment_data.objects.get(refrence_id=str(request.user))

	if(status==1):
		setattr(payment_data_row,'flag',1)
		payment_data_row.save()	
	return render(request,'payment/success.html',{"txnid":txnid,"status":status,"amount":amount})


@login_required
@csrf_exempt
def payment_faliure(request):
	status=request.POST["status"]
	firstname=request.POST["firstname"]
	amount=request.POST["amount"]
	txnid=request.POST["txnid"]
	posted_hash=request.POST["hash"]
	key=request.POST["key"]
	productinfo=request.POST["productinfo"]
	email=request.POST["email"]
	salt="wErVRybo"
	try:
		additionalCharges=request.POST["additionalCharges"]
		retHashSeq=additionalCharges+'|'+salt+'|'+status+'|||||||||||'+email+'|'+firstname+'|'+productinfo+'|'+amount+'|'+txnid+'|'+key
	except Exception:
		retHashSeq = salt+'|'+status+'|||||||||||'+email+'|'+firstname+'|'+productinfo+'|'+amount+'|'+txnid+'|'+key
	hashh=hashlib.sha512(retHashSeq).hexdigest().lower()
	if(hashh !=posted_hash):
		status='Invalid Transaction. Please try again'
	return render(request,"payment/failure.html",{"txnid":txnid,"status":status,"amount":amount})

	