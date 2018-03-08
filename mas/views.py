from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .forms import UserForm
from .models import Symptom,Disease
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import BernoulliNB
import pandas
import json
import numpy as np

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
	diseases=Disease.objects.all()
	all_symptoms = Symptom.objects.all()
	return render(request, 'mas/user.html', {'user':user, 'all_symptoms':all_symptoms, 'diseases':diseases})

def accept(request):
	
	user = request.user
	diseases=Disease.objects.all()
	all_symptoms = Symptom.objects.all()
	states=request.POST.getlist('states')
	states=list(map(int,states))
	url='dataset.csv'
	dataset = pandas.read_csv(url, index_col=0)
	clf = LogisticRegression(random_state=5)
	array = dataset.values
	X = array[:,0:193]
	Y = array[:,193]
	clf = clf.fit(X, Y)
	index_array = np.array(states)
	index_array = [val-1 for val in index_array]
	mask_array = np.zeros(193, dtype=int)
	mask_array[index_array] = 1
	prob_array = clf.predict_proba([mask_array])

	# Convert probability array into a list of dictionaries, with disease id and probability keys
	prob_dicts = [{'disease': index + 1, 'probability': value} for index, value in enumerate(prob_array[0]) if value > 0.00999999999]

	# Sort the list of dictionaries based on probability to get our list of possible diagnoses
	sorted_probs = sorted(prob_dicts, key=lambda dict: dict['probability'], reverse=True)
	#print(json.dumps(sorted_probs, indent=2))
	a=clf.predict([mask_array])
	return render(request, 'mas/user.html', {'user':user, 'all_symptoms':all_symptoms, 'diseases':diseases, 'a':a})