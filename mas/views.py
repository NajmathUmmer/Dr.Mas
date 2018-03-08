from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .forms import UserForm
from .models import Symptom
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
import pandas as pd 
def logout_user(request):
	logout(request)
	form = UserForm(request.POST or None)
	context = {
		"form": form,
	}
	return render(request, 'mas/login.html', context)




	
def login_user(request):
	if request.user.is_authenticated:
		return redirect('/')
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			u = User.objects.get(username=username)
			if user.is_active:
				login(request, user)
				return redirect('/')
			else:
				return render(request, 'mas/login.html', {'error_message': 'Your account has been disabled'})
		else:
			return render(request, 'mas/login.html', {'error_message': 'Invalid login'})
	return render(request, 'mas/login.html')
@login_required(login_url='/login')
def home(request):
	user = request.user
	all_symptoms = Symptom.objects.all()
	return render(request, 'mas/user.html', {'user':user, 'all_symptoms':all_symptoms})