from django.contrib.auth import authenticate,login,get_user_model,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages

@login_required
def Timetable_view(request):
    print("Reached")
    return render(request,"table/timetable.html")

# Create your views here.
