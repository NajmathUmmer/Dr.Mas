from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
#from .forms import UserForm
from .models import Symptom,Disease,Allusers
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import BernoulliNB
import pandas
import json
import numpy as np
import pickle
with open('dictionary.pickle', 'rb') as f:
    	
    	dictionary = pickle.load(f)

url='dataset1.csv'
dataset = pandas.read_csv(url, index_col=0)
clf = LogisticRegression()
array = dataset.values
X = array[:,0:170]
Y = array[:,170]
clf = clf.fit(X, Y)

def logout_user(request):
	logout(request)
	return render(request, 'mas/login.html')



	
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
def signup(request):
	if request.method == "POST":
		username = request.POST['username']
		if request.POST['psw'] == request.POST['psw-repeat']:
			password = request.POST['psw']
			usera = authenticate(username=username, password=password)
			if usera is not None:
				return render(request, 'mas/login.html', {'error_message': 'Already a member'})
			firstname=request.POST['firstname']
			lastname=request.POST['lastname']
			user = User.objects.create_user(username=username, password=password, first_name=firstname, last_name=lastname)
			age=request.POST['age']
			sex=request.POST['sex']
			alluser = Allusers(user=user,age=age,sex=sex)
			alluser.save()
			return render(request, 'mas/login.html')
	return render(request, 'mas/login.html')
	
def diagnose(request):
	states=request.POST.getlist('symptoms[]')
	states=list(map(int,states))
	age=request.user.allusers.age
	sex=request.user.allusers.sex
	a={'Female':0,'Male':1}
	index_array = np.array(states)
	index_array = [val-1 for val in index_array]
	mask_array = np.zeros(168,dtype=int)
	mask_array[index_array] = 1
	mask_array=np.append(a[sex],mask_array)
	mask_array=np.append(age,mask_array)
	prob_array = clf.predict_proba([mask_array])
	# Convert probability array into a list of dictionaries, with disease id and probability keys
	prob_dicts = [{'disease': index + 1, 'probability': value} for index, value in enumerate(prob_array[0]) if value > 0.5]
	# Sort the list of dictionaries based on probability to get our list of possible diagnoses
	sorted_probs = sorted(prob_dicts, key=lambda dict: dict['probability'], reverse=True)
	#sorted_probs=sorted_probs[0:3]
	for dis in sorted_probs:
		diseases=Disease.objects.get(did=dis['disease'])
		dis['name']=diseases.diagnose
		dis['des']=diseases.description
	#print(json.dumps(sorted_probs, indent=2))
	a=clf.predict([mask_array])
	return JsonResponse(sorted_probs,safe=False)
def predict(request):
 	sym=request.POST.getlist('symptoms[]')
 	sym=list(map(int,sym))
 	diseaseArray=[]
 	diseaseArray=np.array(diseaseArray)
 	dictArray=[]
 	for dicti in dictionary:
 		if (set(sym)<= set((dicti['symptoms']+dicti['primary'])) and len(sym)!= 0):
 			diseaseArray=np.append(diseaseArray,dicti['primary'])
 			diseaseArray=np.append(diseaseArray,dicti['symptoms'])
 	diseaseArray=list(set(diseaseArray))
 	print(diseaseArray)
 	for i in diseaseArray:
 		if i not in sym:
 			dict={'id':i}
 			dictArray.append(dict)
 			print(dictArray)
 	for j in dictArray:
 		symptoms=Symptom.objects.get(syd=j['id'])
 		j['name']=symptoms.symptoms
 		j['sex']=symptoms.sex
 		j['user']=request.user.allusers.sex
 		print(j['name'])
 	print(len(dictArray))
 	return JsonResponse(dictArray,safe=False)
