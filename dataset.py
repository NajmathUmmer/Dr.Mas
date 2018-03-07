import random
import pickle
import numpy as np
import pandas as pd
dictionary = [
  {
    'disease': 1,
    'symptoms': [
      38,
      68,
      106,
      171,
      172
    ]
  },
  {
    'disease': 2,
    'symptoms': [
      12,
      48,
      82,
      88,
      93,
      124,
      18,
      25,
      67,
      188
    ]
  },
  {
    'disease': 3,
    'symptoms': [
      2,
      90,
      174,
      1,
      6,
      11,
      13,
      29,
      33,
      44,
      79
    ]
  },
  {
    'disease': 4,
    'symptoms': [
      6,
      22,
      31,
      34,
      37,
      45,
      73,
      165,
      116,
      5,
      46,
      54,
      180,
      191
    ]
  },
  {
    'disease': 5,
    'symptoms': [
      67,
      6,
      91,
      110,
      173,
      10,
      14,
      176,
      179,
      175
    ]
  },
  {
    'disease': 6,
    'symptoms': [
      18,
      66,
      70,
      74,
      78,
      77,
      97,
      108,
      109,
      160,
      164,
      166,
      170,
      35,
      187,
      189
    ]
  },
  {
    'disease': 7,
    'symptoms': [
      18,
      173,
      9,
      185,
      190
    ]
  },
  {
    'disease': 8,
    'symptoms': [
      38,
      48,
      82,
      88,
      93,
      165,
      116,
      164,
      28,
      47,
      87,
      119,
      122,
      127,
      132,
      142,
      113,
      15,
      154,
      155,
      162,
      161,
      115,
      163,
      167
    ]
  },
  {
    'disease': 9,
    'symptoms': [
      109,
      166,
      47,
      87,
      132,
      113,
      49,
      105,
      107,
      118,
      123,
      133,
      8,
      3,
      184,
      181
    ]
  },
  {
    'disease': 10,
    'symptoms': [
      63,
      104
    ]
  },
  {
    'disease': 11,
    'symptoms': [
      48,
      82,
      93,
      188,
      78,
      164,
      170,
      87,
      162,
      161,
      115,
      163,
      123,
      133,
      181,
      101,
      30,
      56,
      129,
      145,
      146,
      137,
      151,
      152,
      168,
      169,
      193,
      183
    ]
  },
  {
    'disease': 12,
    'symptoms': [
      181,
      193,
      183,
      19,
      40,
      53,
      57
    ]
  },
  {
    'disease': 13,
    'symptoms': [
      174,
      13,
      33,
      60,
      75,
      139
    ]
  },
  {
    'disease': 14,
    'symptoms': [
      54,
      55,
      72
    ]
  },
  {
    'disease': 15,
    'symptoms': [
      2,
      1,
      37
    ]
  },
  {
    'disease': 16,
    'symptoms': [
      172,
      188,
      187,
      119,
      183,
      36,
      130,
      138,
      192
    ]
  },
  {
    'disease': 17,
    'symptoms': [
      82,
      66,
      56,
      80,
      111,
      85
    ]
  },
  {
    'disease': 18,
    'symptoms': [
      12,
      18,
      25,
      188,
      110,
      66,
      70,
      108,
      155,
      183,
      80,
      85,
      4,
      86
    ]
  },
  {
    'disease': 19,
    'symptoms': [
      172,
      12,
      82,
      88,
      93,
      188,
      13,
      166,
      47,
      127,
      132,
      123,
      133,
      184,
      57,
      130,
      39,
      16,
      134,
      136
    ]
  },
  {
    'disease': 20,
    'symptoms': [
      87,
      119,
      107,
      129,
      7,
      52
    ]
  },
  {
    'disease': 21,
    'symptoms': [
      11,
      132,
      118,
      26,
      27
    ]
  },
  {
    'disease': 22,
    'symptoms': [
      12,
      48,
      18,
      188,
      90,
      11,
      54,
      66,
      70,
      74,
      97,
      160,
      35,
      189,
      85,
      26,
      32,
      89,
      95,
      103,
      186
    ]
  },
  {
    'disease': 23,
    'symptoms': [
      18,
      79,
      54,
      70,
      78,
      77,
      164,
      35,
      122,
      53,
      192,
      23,
      128,
      131,
      41
    ]
  },
  {
    'disease': 24,
    'symptoms': [
      122,
      7,
      64,
      65
    ]
  },
  {
    'disease': 25,
    'symptoms': [
      2,
      174,
      1,
      6,
      29,
      33,
      44,
      79,
      180,
      181,
      30,
      40,
      64,
      58,
      100
    ]
  },
  {
    'disease': 26,
    'symptoms': [
      27
    ]
  },
  {
    'disease': 27,
    'symptoms': [
      18,
      67,
      1,
      6,
      11,
      29,
      44,
      180,
      110,
      173,
      10,
      14,
      176,
      179,
      175,
      9,
      104,
      26,
      89,
      98,
      114,
      117,
      159
    ]
  },
  {
    'disease': 28,
    'symptoms': [
      184,
      193,
      57,
      75,
      139,
      130,
      135,
      140
    ]
  },
  {
    'disease': 29,
    'symptoms': [
      12,
      18,
      2,
      6,
      35,
      183,
      57
    ]
  },
  {
    'disease': 30,
    'symptoms': [
      60
    ]
  },
  {
    'disease': 31,
    'symptoms': [
      6,
      22,
      34,
      5,
      46,
      47,
      127,
      43,
      83,
      143,
      153,
      157
    ]
  },
  {
    'disease': 32,
    'symptoms': [
      60
    ]
  },
  {
    'disease': 33,
    'symptoms': [
      2,
      58,
      61,
      42,
      76,
      182
    ]
  },
  {
    'disease': 34,
    'symptoms': [
      68,
      171,
      18,
      67,
      11,
      14,
      35,
      122,
      63,
      104,
      52,
      26,
      95,
      23,
      24,
      156,
      20,
      21,
      69,
      84,
      177
    ]
  },
  {
    'disease': 35,
    'symptoms': [
      160,
      166,
      19,
      103,
      92,
      94
    ]
  },
  {
    'disease': 36,
    'symptoms': [
      38,
      171,
      67,
      11,
      79,
      14,
      35,
      8,
      26,
      117,
      21,
      69,
      84,
      112
    ]
  },
  {
    'disease': 37,
    'symptoms': [
      82,
      93,
      14,
      155,
      27
    ]
  },
  {
    'disease': 38,
    'symptoms': [
      14,
      97,
      189,
      104,
      27,
      103,
      94,
      17
    ]
  },
  {
    'disease': 39,
    'symptoms': [
      33,
      30,
      58,
      61
    ]
  },
  {
    'disease': 40,
    'symptoms': [
      14,
      176,
      179,
      175,
      104
    ]
  },
  {
    'disease': 41,
    'symptoms': [
      106,
      63,
      104,
      95,
      114,
      51
    ]
  },
  {
    'disease': 42,
    'symptoms': [
      18,
      2,
      174,
      66,
      160,
      166,
      87,
      87,
      119,
      132,
      26,
      103,
      92,
      17,
      50
    ]
  },
  {
    'disease': 43,
    'symptoms': [
      108,
      145,
      146,
      137,
      151,
      152,
      103,
      120,
      125,
      144,
      147,
      148,
      149,
      150,
      62
    ]
  },
  {
    'disease': 44,
    'symptoms': [
      172,
      34,
      145,
      146,
      137,
      151,
      152,
      135,
      42,
      144,
      147,
      148,
      149,
      150,
      62,
      126,
      158
    ]
  },
  {
    'disease': 45,
    'symptoms': [
      62,
      102
    ]
  },
  {
    'disease': 46,
    'symptoms': [
      124,
      43,
      59
    ]
  },
  {
    'disease': 47,
    'symptoms': [
      154,
      145,
      146,
      137,
      151,
      152,
      32,
      42,
      144,
      147,
      148,
      149,
      150,
      62,
      126,
      99,
      178
    ]
  },
  {
    'disease': 48,
    'symptoms': [
      12,
      188,
      160,
      166,
      96
    ]
  },
  {
    'disease': 49,
    'symptoms': [
      12,
      18,
      13,
      79,
      110,
      108,
      160,
      166,
      166,
      187,
      190,
      142,
      155,
      115,
      163,
      133,
      181,
      145,
      146,
      137,
      151,
      152,
      168,
      169,
      193,
      40,
      53,
      57,
      139,
      130,
      192,
      85,
      4,
      134,
      136,
      41,
      140,
      17,
      144,
      147,
      148,
      149,
      150,
      62,
      71
    ]
  },
  {
    'disease': 50,
    'symptoms': [
      130
    ]
  },
  {
    'disease': 51,
    'symptoms': [
      180,
      142,
      192,
      42
    ]
  },
  {
    'disease': 52,
    'symptoms': [
      97,
      189,
      112
    ]
  },
  {
    'disease': 53,
    'symptoms': [
      27
    ]
  },
  {
    'disease': 54,
    'symptoms': [
      168,
      169
    ]
  },
  {
    'disease': 55,
    'symptoms': [
      19,
      192,
      81
    ]
  },
  {
    'disease': 56,
    'symptoms': [
      181,
      193,
      183
    ]
  },
  {
    'disease': 57,
    'symptoms': [
      82,
      28,
      60,
      75,
      76
    ]
  },
  {
    'disease': 58,
    'symptoms': [
      82,
      174,
      118,
      53,
      26
    ]
  },
  {
    'disease': 59,
    'symptoms': [
      172,
      67,
      4,
      134,
      136,
      121,
      121
    ]
  },
  {
    'disease': 60,
    'symptoms': [
      181,
      193,
      135
    ]
  },
  {
    'disease': 61,
    'symptoms': [
      111,
      51
    ]
  },
  {
    'disease': 62,
    'symptoms': [
      172,
      82,
      107,
      53,
      7,
      51
    ]
  },
  {
    'disease': 63,
    'symptoms': [
      82,
      67,
      174,
      173,
      160,
      111,
      141
    ]
  },
  {
    'disease': 64,
    'symptoms': [
      70,
      111,
      85
    ]
  }
]

instances = []
header = np.arange(1, 194, dtype=int)
header = np.append(header, 'Disease')
for dicti in dictionary:
	for i in range(0,100):
		symptom_count = len(dicti['symptoms'])
		minimum_rand = 3 if symptom_count >= 3 else 1
		n=random.randrange(minimum_rand,symptom_count + 1)
		symptomArr = random.sample(dicti['symptoms'],n)
		array=np.zeros(193, dtype=int)
		symptomArr = [x - 1 for x in symptomArr]
		array[symptomArr]=1
		array = np.append(array, dicti['disease'])
		instances.append(array)
instanceArray = np.asarray(instances)
# pickle.dump(instances, open( "save.p", "wb" ) )
dataset = pd.DataFrame(data=instances, columns=header)
print(dataset)
#np.savetxt("dataset.csv", dataset, delimiter=",")
#dataset.to_csv("dataset.csv", sep=',', encoding='utf-8')
