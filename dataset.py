import random
import pickle
import numpy as np
import pandas as pd
dictionary = [
  {
    'disease': 1,
    'symptoms': [
      34,
      63,
      92,
      147,
      148
    ],
    'primary': []
  },
  {
    'disease': 2,
    'symptoms': [
      12,
      17,
      24,
      44,
      62,
      75,
      80,
      84,
      107,
      163
    ],
    'primary': []
  },
  {
    'disease': 3,
    'symptoms': [
      1,
      2,
      6,
      11,
      13,
      27,
      30,
      40,
      73,
      81
    ],
    'primary': [
      150
    ]
  },
  {
    'disease': 4,
    'symptoms': [
      5,
      6,
      21,
      31,
      33,
      39,
      41,
      42,
      50,
      67,
      101,
      135,
      155,
      166
    ],
    'primary': []
  },
  {
    'disease': 5,
    'symptoms': [
      6,
      10,
      14,
      62,
      82,
      96,
      149,
      151,
      154
    ],
    'primary': [
      152
    ]
  },
  {
    'disease': 6,
    'symptoms': [
      17,
      32,
      32,
      61,
      65,
      68,
      71,
      72,
      94,
      95,
      138,
      142,
      143,
      146,
      162,
      164
    ],
    'primary': []
  },
  {
    'disease': 7,
    'symptoms': [
      9,
      17,
      149,
      160,
      165
    ],
    'primary': []
  },
  {
    'disease': 8,
    'symptoms': [
      3,
      8,
      43,
      79,
      91,
      93,
      95,
      99,
      103,
      106,
      115,
      143,
      156,
      159
    ],
    'primary': []
  },
  {
    'disease': 9,
    'symptoms': [
      25,
      59,
      134
    ],
    'primary': [
      92
    ]
  },
  {
    'disease': 10,
    'symptoms': [
      28,
      44,
      52,
      72,
      75,
      79,
      84,
      88,
      100,
      106,
      112,
      115,
      119,
      124,
      129,
      130,
      139,
      140,
      141,
      142,
      144,
      145,
      146,
      156,
      158,
      163
    ],
    'primary': [
      168
    ]
  },
  {
    'disease': 11,
    'symptoms': [
      18,
      36,
      49,
      53,
      156,
      158
    ],
    'primary': [
      168
    ]
  },
  {
    'disease': 12,
    'symptoms': [
      13,
      30,
      45,
      56,
      69,
      120,
      150
    ],
    'primary': []
  },
  {
    'disease': 13,
    'symptoms': [
      50,
      51,
      66
    ],
    'primary': []
  },
  {
    'disease': 14,
    'symptoms': [
      1,
      2,
      33,
      56
    ],
    'primary': []
  },
  {
    'disease': 15,
    'symptoms': [
      55,
      79,
      113,
      133,
      158,
      162,
      167
    ],
    'primary': []
  },
  {
    'disease': 16,
    'symptoms': [
      52,
      61,
      74,
      75,
      78,
      97
    ],
    'primary': []
  },
  {
    'disease': 17,
    'symptoms': [
      4,
      12,
      17,
      24,
      61,
      65,
      74,
      78,
      94,
      96,
      133,
      158,
      163
    ],
    'primary': []
  },
  {
    'disease': 18,
    'symptoms': [
      13,
      15,
      35,
      43,
      53,
      75,
      80,
      106,
      110,
      113,
      116,
      118,
      148
    ],
    'primary': []
  },
  {
    'disease': 19,
    'symptoms': [
      7,
      48,
      79,
      93,
      112
    ],
    'primary': []
  },
  {
    'disease': 20,
    'symptoms': [
      11,
      25,
      103,
      133
    ],
    'primary': [
      25
    ]
  },
  {
    'disease': 21,
    'symptoms': [
      11,
      12,
      17,
      25,
      32,
      44,
      50,
      161
    ],
    'primary': []
  },
  {
    'disease': 22,
    'symptoms': [
      17,
      22,
      37,
      49,
      50,
      65,
      71,
      72,
      73,
      105,
      111,
      114,
      142,
      167
    ],
    'primary': [
      32
    ]
  },
  {
    'disease': 23,
    'symptoms': [
      7,
      25,
      90,
      105
    ],
    'primary': []
  },
  {
    'disease': 24,
    'symptoms': [
      2,
      6,
      27,
      28,
      30,
      36,
      54,
      60,
      73,
      87,
      150,
      155,
      156
    ],
    'primary': [
      40
    ]
  },
  {
    'disease': 25,
    'symptoms': [
      10,
      11,
      14,
      25,
      27,
      62,
      102,
      137,
      149,
      151,
      152,
      154
    ],
    'primary': []
  },
  {
    'disease': 26,
    'symptoms': [
      53,
      69,
      113,
      120,
      121,
      159
    ],
    'primary': []
  },
  {
    'disease': 27,
    'symptoms': [
      2,
      6,
      12,
      17,
      32,
      158
    ],
    'primary': []
  },
  {
    'disease': 28,
    'symptoms': [
      5,
      6,
      21,
      31,
      39,
      42,
      43,
      76,
      110,
      123,
      131,
      135
    ],
    'primary': []
  },
  {
    'disease': 29,
    'symptoms': [
      2,
      38,
      54,
      57,
      70,
      157
    ],
    'primary': []
  },
  {
    'disease': 30,
    'symptoms': [
      14,
      19,
      20,
      22,
      23,
      25,
      32,
      59,
      62,
      64,
      77,
      134
    ],
    'primary': [
      63
    ]
  },
  {
    'disease': 31,
    'symptoms': [
      8,
      11,
      14,
      20,
      25,
      32,
      34,
      62,
      64,
      73,
      77,
      98,
      102,
      147
    ],
    'primary': []
  },
  {
    'disease': 32,
    'symptoms': [
      14,
      25,
      75,
      84,
      133
    ],
    'primary': []
  },
  {
    'disease': 33,
    'symptoms': [
      14,
      16,
      25,
      32
    ],
    'primary': []
  },
  {
    'disease': 34,
    'symptoms': [
      30,
      54,
      57
    ],
    'primary': []
  },
  {
    'disease': 35,
    'symptoms': [
      14,
      92,
      151,
      152,
      154
    ],
    'primary': []
  },
  {
    'disease': 36,
    'symptoms': [
      47,
      92
    ],
    'primary': []
  },
  {
    'disease': 37,
    'symptoms': [
      2,
      16,
      17,
      25,
      46,
      61,
      79,
      79,
      83,
      138,
      143,
      150
    ],
    'primary': []
  },
  {
    'disease': 38,
    'symptoms': [
      58,
      94,
      104,
      108,
      119,
      124,
      125,
      126,
      127,
      128,
      129,
      130
    ],
    'primary': []
  },
  {
    'disease': 39,
    'symptoms': [
      31,
      38,
      58,
      109,
      117,
      119,
      124,
      125,
      126,
      127,
      128,
      129,
      130,
      136,
      148
    ],
    'primary': []
  },
  {
    'disease': 40,
    'symptoms': [
      58,
      89
    ],
    'primary': []
  },
  {
    'disease': 41,
    'symptoms': [
      39,
      55,
      107
    ],
    'primary': []
  },
  {
    'disease': 42,
    'symptoms': [
      29,
      38,
      58,
      109,
      119,
      124,
      125,
      126,
      127,
      128,
      129,
      130,
      132,
      153
    ],
    'primary': [
      86
    ]
  },
  {
    'disease': 43,
    'symptoms': [
      12,
      85,
      138,
      143,
      163
    ],
    'primary': []
  },
  {
    'disease': 44,
    'symptoms': [
      113,
      120
    ],
    'primary': []
  },
  {
    'disease': 45,
    'symptoms': [
      25,
      32,
      97,
      98,
      164
    ],
    'primary': []
  },
  {
    'disease': 46,
    'symptoms': [
      11
    ],
    'primary': [
      25,
      39
    ]
  },
  {
    'disease': 47,
    'symptoms': [
      144,
      145
    ],
    'primary': []
  },
  {
    'disease': 48,
    'symptoms': [
      156,
      158,
      168
    ],
    'primary': []
  },
  {
    'disease': 49,
    'symptoms': [
      26,
      56,
      69,
      70,
      75
    ],
    'primary': []
  },
  {
    'disease': 50,
    'symptoms': [
      25,
      49,
      75,
      103,
      150
    ],
    'primary': []
  },
  {
    'disease': 51,
    'symptoms': [
      47,
      97
    ],
    'primary': []
  },
  {
    'disease': 52,
    'symptoms': [
      7,
      47,
      49,
      75,
      93,
      148
    ],
    'primary': []
  },
  {
    'disease': 53,
    'symptoms': [
      62,
      75,
      97,
      122,
      138,
      149,
      150
    ],
    'primary': []
  },
  {
    'disease': 54,
    'symptoms': [
      65,
      78,
      97
    ],
    'primary': []
  }
]

instances = []
header = np.arange(1, 169, dtype=int)
header = np.append(header, 'Disease')
header = np.append('Sex', header)
header = np.append('Age', header)
sex=[0,1]
female=[7,12,26,27]
twfo=[26,27,29]
tf=[4,7,10,49]
f=[12,43,44,49]
for dicti in dictionary:
	for i in range(0,100):
		symptom_count = len(dicti['symptoms'])
		minimum_rand = 3 if symptom_count >= 3 else 1
		n=random.randrange(minimum_rand,symptom_count + 1)
		if dicti['disease'] in twfo:
			limit=random.randrange(20,40)
		elif dicti['disease'] in tf:
			limit=random.randrange(35,45)
		elif dicti['disease'] in f:
			limit=random.randrange(49,80)
		else:
			limit=random.randrange(10,80)
		    
		s=0 if dicti['disease'] in female else random.choice(sex)
		symptomArr = random.sample(dicti['symptoms'],n)
		array=np.zeros(168, dtype=int)
		symptomArr = [x - 1 for x in symptomArr]
		primary=dicti['primary']
		primary=[x - 1 for x in primary]
		array[symptomArr]=1
		array[primary]=1
		array = np.append(array, dicti['disease'])
		array = np.append(s, array)
		array = np.append(limit, array)
		instances.append(array)
instanceArray = np.asarray(instances)
# pickle.dump(instances, open( 'save.p', 'wb' ) )
dataset = pd.DataFrame(data=instances, columns=header)

#np.savetxt('dataset.csv', dataset, delimiter=',')
dataset.to_csv("dataset1.csv", sep=',', encoding='utf-8')
