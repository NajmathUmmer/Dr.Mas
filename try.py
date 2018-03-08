'''from sklearn.naive_bayes import GaussianNB
import pandas
import numpy as np
url='C:/Users/Najmath Ummer/Desktop/dataset.csv'
dataset = pandas.read_csv(url,index_col=0)
clf = GaussianNB()
array = dataset.values
X = array[:,0:193]
Y = array[:,193]
clf.fit(X, Y)
index_array = np.array([82,174,53,26])
index_array = [val-1 for val in index_array]
mask_array = np.zeros(193, dtype=int)
mask_array[index_array] = 1
print(clf.predict([mask_array]))'''
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import BernoulliNB
import pandas
import json
import numpy as np
url='dataset.csv'
dataset = pandas.read_csv(url, index_col=0)
clf = LogisticRegression(random_state=5)
array = dataset.values
X = array[:,0:193]
Y = array[:,193]
clf = clf.fit(X, Y)
index_array = np.array([9, 185, 18, 66])
index_array = [val-1 for val in index_array]
mask_array = np.zeros(193, dtype=int)
mask_array[index_array] = 1
prob_array = clf.predict_proba([mask_array])

# Convert probability array into a list of dictionaries, with disease id and probability keys
prob_dicts = [{'disease': index + 1, 'probability': value} for index, value in enumerate(prob_array[0]) if value > 0.00999999999]

# Sort the list of dictionaries based on probability to get our list of possible diagnoses
sorted_probs = sorted(prob_dicts, key=lambda dict: dict['probability'], reverse=True)
print(json.dumps(sorted_probs, indent=2))
print('Most probable diagnosis: ', clf.predict([mask_array])[0])