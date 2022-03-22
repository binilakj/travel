
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        a=request.POST['username']
        b=request.POST['password']
        c=auth.authenticate(username=a,password=b)
        if c is not None:
            auth.login(request,c)
            return redirect('/')
        else:
            messages.info(request,"invalid")
            return redirect('login')

    return render(request,"log.html")

def register(request):
    if request.method=='POST':
        a=request.POST['username']
        b = request.POST['first_name']
        c = request.POST['last_name']
        d= request.POST['email']
        e = request.POST['password']
        f = request.POST['password1']
        if e==f:
            if User.objects.filter(username=a).exists():
                messages.info(request,"username taken")
                return redirect('register')
            elif User.objects.filter(email=d).exists():
                  messages.info(request,"email taken")
                  return redirect('register')
            else:
                 g=User.objects.create_user(username=a,password=e,first_name=b,last_name=c,email=d)
                 g.save()
                 return redirect('login')
        else:
           messages.info(request,"password not matching")
           return redirect('register')
           return redirect('/')


    return render(request,"reg.html")

def logout(request):
    auth.logout(request)
    return redirect('/')