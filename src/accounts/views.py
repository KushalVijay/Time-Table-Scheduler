from django.contrib.auth import authenticate,login,get_user_model,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail
from .forms import RegisForm,LoginForm,AdminLoginForm
# Create your views here.

User = get_user_model()
@login_required
def Admin_home(request):
    return render(request,"accounts/admin_home.html")
@login_required
def Faculty_home(request):
    # send_mail('Hello','Kushal Vijay','kushvijay38@gmail',
    #           ['vijaykushal8118@gmail.com'],
    #           fail_silently=False)
    return render(request,"accounts/faculty_home.html")
def Login_View(request):
    form =  LoginForm(request.POST or None)




    context = {'next': request.GET['next'] if request.GET and 'next' in request.GET else ''}

    if form.is_valid():
        redir = request.POST['next']
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request,
                            username=username,
                            password=password)
        if user:
            login(request,user)
            if redir:
                return redirect(redir)
            return redirect("/faculty_home")
        else:
            print("Error1")
    return render(request,"accounts/login.html",context)

def Admin_Login_View(request):
    form =  AdminLoginForm(request.POST or None)

    context = {'next': request.GET['next'] if request.GET and 'next' in request.GET else ''}
    if form.is_valid():
        redir = request.POST['next']
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request,
                            username=username,
                            password=password)
        if user is not None:

            login(request,user)
            if redir:
                return redirect(redir)
            messages.info(request,"Successfully Logged In")
            return redirect("/admin_home")  #To be changed ,where we need to be redirected after the process
        else:
            print("Error2")
    return render(request,"accounts/login.html")


def FRegister_View(request):
    form =  RegisForm(request.POST or None)

    if form.is_valid():

        username = form.cleaned_data.get("username")
        email    = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username,email,password)
        return redirect("/login")

    return render(request,"accounts/facultyregister.html")

def ARegister_View(request):
    form =  RegisForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get("username")
        email    = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username,email,password)
        return redirect("/login")

    return render(request,"accounts/adminregister.html")

def Logout_view(request):

    logout(request)
    messages.info(request,"Succefully Logged Out")
    return redirect("/")


