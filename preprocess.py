# Load libraries
import pandas
from pandas.plotting import scatter_matrix
#import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
url='dataset1.csv'
dataset = pandas.read_csv(url)
# Split-out validation dataset
array = dataset.values
X = array[:,1:171]
Y = array[:,171]

validation_size = 0.20
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed, stratify=Y)
# Test options and evaluation metric
seed = 7
scoring = 'accuracy'
# Spot Check Algorithms
models = []
models.append(('LR', LogisticRegression()))
# models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC()))
# evaluate each model in turn
results = []
names = []
print('Training Accuracies:- ')
for name, model in models:
	kfold = model_selection.StratifiedKFold(n_splits=10, shuffle=True, random_state=seed)
	cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
	results.append(cv_results)
	names.append(name)
	msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
	print(msg)
# Make predictions on validation dataset

print('\nValidation Scores:- ')
for name, model in models:
	clf = model.fit(X_train, Y_train)
	predictions = clf.predict(X_validation)
	print(name, ':-')
	print('Accuracy: ', accuracy_score(Y_validation, predictions))
	print('Precision: ', precision_score(Y_validation, predictions, average='micro'))
	print('Recall: ', recall_score(Y_validation, predictions, average='micro'))