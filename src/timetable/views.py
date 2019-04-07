from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail,send_mass_mail
from django.shortcuts import render
from django.http import  HttpResponse
# Create your views here


# After we save the form , then
# send_mail(subject,message,from_email,
#           recipient_list,fail_silently=True)
def home_page(request):
    return render(request,"homepage.html",{})

