__author__ = 'Anubhav'

import pandas as pd
import numpy as np


#df = pd.read_csv('Berkeley.csv')

#print df
#print df[['Admit','Dept','Freq','Gender']][(df['Gender'] == 'Male') & (df['Dept'] == 'A')]

df = pd.read_csv('train.csv')

#print df[['PassengerId','Sex']]


predictions = {}
passenger_id_list = list()
passenger_survived_list = list()
for index,row in df.iterrows():
    #print row['Sex'],row['PassengerId']
    passengerid = row['PassengerId']
    passengerclass = row['Pclass']
    passengerage = row['Age']
    passengersib = row['SibSp']
    passengerpar = row['Parch']
    if row['Sex'] == 'male':
        if (passengersib == 0 ) and (passengerpar == 0):
            predictions[passengerid] = 1
        elif (passengerclass == 3) and (passengersib != 0) and (passengerpar != 0):
            predictions[passengerid] = 0
        elif (passengerclass == 3) and ((passengersib != 0) or (passengerpar != 0)):
            predictions[passengerid] = 0
    elif row['Sex'] == 'female':
        if (passengersib == 0 ) and (passengerpar == 0):
            predictions[passengerid] = 1
        elif (passengerclass == 3) and (passengersib != 0) and (passengerpar != 0):
            predictions[passengerid] = 0
        elif (passengerclass == 3) and ((passengersib != 0) or (passengerpar != 0)):
            predictions[passengerid] = 0




#predictions.update()
print len(predictions)


print predictions




