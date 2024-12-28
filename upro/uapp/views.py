from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
# Create your views here.
def main(request):
    return render(request,'welcome.html')
def login_user(request):
    if request.POST:
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect(main)
        messages.error(request,"wrong credentials")
        return redirect(login_user)
    return render(request,'index.html')
def signup(request):
    if request.POST:
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirmpassword=request.POST.get('confirmpassword')
        if password==confirmpassword:
            User.objects.create_user(username=username,email=email,password=password)
            return redirect(login_user)
        messages.error(request,"password doesnot match")
        return redirect(signup)
    return render(request,'signup.html')
