from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
# Create your views here.

def register(request):
	if request.method=='POST':
		first_name=request.POST['first_name']
		last_name=request.POST['last_name']
		username=request.POST['username']
		email=request.POST['email']
		password=request.POST['passw']
		repassword=request.POST['repass']
		user=User.objects.create_user(username=username, first_name=first_name, last_name=last_name, password=password,email=email)
		user.save();
		print("user created")
		return redirect('/')
	else:
		return render(request,'register.html')
