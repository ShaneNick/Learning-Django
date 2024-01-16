from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request, 'authentication/index.html')

def signup(request):
    if request.method == "POST":
        #username = request.POST.get('username')
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, 'You account has been successfully created')

        return redirect('signup')
    return render(request, 'authentication/signup.html')

def login(request):
    return render(request, 'authentication/login.html')

def logout(request):
    pass



