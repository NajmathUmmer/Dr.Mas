import pandas as pd
import json

file = 'C:/Users/Najmath Ummer/djangogirls/mas/diffsydiw3.csv'

df = pd.read_csv(file)
df = df.sort_values(['did', 'syd'])

diseaseArr = []

for row in df.values:
	dict_index = [key for key,value in enumerate(diseaseArr) if value['disease'] == int(row[0])]
	if len(dict_index):
		if row[2] == 1:
			diseaseArr[dict_index[0]]['primary'].append(int(row[1]))
		else:
			diseaseArr[dict_index[0]]['symptoms'].append(int(row[1]))
	else:
		dict = {
			'disease': int(row[0]),
			'symptoms': [],
			'primary': []
		}
		if row[2] == 1:
			dict['primary'].append(int(row[1]))
		else:
			dict['symptoms'].append(int(row[1]))
		diseaseArr.append(dict)
print(json.dumps(diseaseArr, indent=2))