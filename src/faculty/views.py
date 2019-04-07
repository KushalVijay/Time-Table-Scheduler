from django.shortcuts import render
from django.http import  HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here

from .forms import Infoform

@login_required
def facultyinfo(request):
    form  = Infoform(request.POST or None)

    if form.is_valid():
        form.save()
    return render(request,"faculty/faculty.html")




