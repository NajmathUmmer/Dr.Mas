import pandas as pd
url='C:/Users/Najmath Ummer/Desktop/main project/dia_t2.csv'
urli='C:/Users/Najmath Ummer/Desktop/main project/one.csv'
a=pd.read_csv(url)
b=pd.read_csv(urli)
new=pd.merge(left=a,right=b,left_on='did',right_on='did')
i=pd.DataFrame(new)
new.to_csv("two.csv", sep=',', encoding='utf-8')
'''urlj='C:/Users/Najmath Ummer/Desktop/weka/Weka datasets/symptoms/sdsort/sym_t.csv'
new='C:/Users/Najmath Ummer/Desktop/pandaram2.csv'
c=pd.read_csv(urlj)
new='C:/Users/Najmath Ummer/Desktop/new.csv'
d=pd.read_csv(new)
pandaram2=pd.merge(left=d,right=a,left_on='syd',right_on='syd')''

new='C:/Users/Najmath Ummer/Desktop/pandaram2.csv'
j=pd.DataFrame(pandaram2)
pandaram2.to_csv("pandaram2.csv", sep=',', encoding='utf-8')'''

