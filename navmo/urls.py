"""navmo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from register.views_register import faqs,overview,registration,home,login_check,logout_page,start,contactus
from register.views_register import logout_and_register
from otp.views import verify_mobile
from payment.views import payment,payment_faliure,payment_success
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',start),
    url(r'^accounts/login/$', login_check),
    url(r'^login/$', login_check),
    url(r'^register/$',registration ),
    url(r'^home/$',home ),
    url(r'^logout/$',logout_page ),
    url(r'^logout_and_register/$',logout_and_register),
    url(r'^payment/$',payment ),
    url(r'^verify_mobile/$',verify_mobile ),
    url(r'^payment_faliure/$',payment_faliure),
    url(r'^payment_success/$',payment_success),
    url(r'^contactus/$',contactus),
    url(r'^overview/$',overview),
    url(r'^faqs/$',faqs),

]
from django.conf import settings
from django.conf.urls.static import static
urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)