from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.core.mail import send_mail
from django.conf import settings
import random

def index(request):
    return render(request, 'index.html')

def usersignup(request):
    if request.POST:
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confpassword')

        # Validate form fields
        if not username or not email or not password or not confirmpassword:
            messages.error(request, 'All fields are required.')
        elif confirmpassword != password:
            messages.error(request, "Passwords do not match.")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
        else:
            # Create the user
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, "Account created successfully!")
            return redirect('userlogin')  # Redirect to login page

    return render(request, "register.html")

def userlogin(request):
    if 'username' in request.session:
        return redirect('index')  
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            request.session['username'] = username
            return redirect('index')  # Redirect to the home page
        else:
            messages.error(request, "Invalid credentials.")

    return render(request, 'userlogin.html')

def verifyotp(request):
    if request.POST:
        otp = request.POST.get('otp')
        otp1 = request.session.get('otp')
        if otp == otp1:
            del request.session['otp']
            return redirect('passwordreset')
        else:
            messages.error(request, 'Invalid OTP. Please try again.')

    # Generate OTP and send email
    otp = ''.join(random.choices('123456789', k=6))
    request.session['otp'] = otp
    message = f'Your email verification code is: {otp}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [request.session.get('email')]
    send_mail('Email Verification', message, email_from, recipient_list)

    return render(request, "otp.html")

def getusername(request):
    if request.POST:
        username = request.POST.get('username')
        try:
            user = User.objects.get(username=username)
            request.session['email'] = user.email
            return redirect('verifyotp')
        except User.DoesNotExist:
            messages.error(request, "Username does not exist.")
            return redirect('getusername')

    return render(request, 'getusername.html')

def passwordreset(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confpassword')

        # Check if the passwords match
        if confirmpassword != password:
            messages.error(request, "Passwords do not match.")
        else:
            email = request.session.get('email')
            try:
                user = User.objects.get(email=email)

                # Set the new password
                user.set_password(password)
                user.save()

                # After resetting password, clear the session email
                del request.session['email']
                messages.success(request, "Your password has been reset successfully.")
                
                # Optionally, log the user in automatically after resetting the password
                user = authenticate(username=user.username, password=password)
                if user is not None:
                    login(request, user)

                return redirect('userlogin')  # Redirect to the login page after password reset
            except User.DoesNotExist:
                messages.error(request, "No user found with that email address.")
                return redirect('getusername')  # Redirect to username input form

    return render(request, "passwordreset.html")

def logoutuser(request):
    logout(request)
    request.session.flush()
    return redirect(userlogin)