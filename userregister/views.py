from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import logout
from .models import DataUser


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect('home')
        else:
            return redirect('login')
    return render(request, 'userregister/login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        re_password = request.POST['re_password']
        er = 1
        for i in phone:
            if i < "0" and i > "9":
                er = 0
                break
        if password == re_password and phone.count("+") == 1 and er:
            num=0
            phone_a = 0
            if phone[0:4]=='+996':
                phone_a = 1
            telData = DataUser.objects.create(username=username, email=email, tel=phone,telInfo = phone_a, password = password)
            telData.save()
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email,
                                            password=password)
            user.save()

            return redirect('login')
        else:
            return redirect('register')

    return render(request, 'userregister/register.html')
