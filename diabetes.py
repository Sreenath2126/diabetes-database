# -*- coding: utf-8 -*-
"""diabetes.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NkL5GrWFVRPCKMCvZmymMdQuzZk74lHw
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
dataset = pd.read_csv('Diabetes Database.csv')
#print(dataset.head())
#df=pd.DataFrame(dataset)
#df.isnull().sum()
X = dataset.iloc[:, [0,1,2,3,4,5,6,7]].values
y = dataset.iloc[:, 8].values
Xcol = dataset.iloc[:, [0,1,2,3,4,5,6,7]]
ycol = dataset.iloc[:, 8]

#smote
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
os = SMOTE(random_state=0)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
columns = Xcol.columns
os_data_X,os_data_y=os.fit_sample(X_train, y_train)
os_data_X = pd.DataFrame(data=os_data_X,columns=columns )
os_data_y= pd.DataFrame(data=os_data_y,columns=['y'])
# we can Check the numbers of our data
print("length of oversampled data is ",len(os_data_X))
print("Number of non-diabetic in oversampled data",len(os_data_y[os_data_y['y']==0]))
print("Number of diabetic",len(os_data_y[os_data_y['y']==1]))
print("Proportion of non-diabetic data in oversampled data is ",len(os_data_y[os_data_y['y']==0])/len(os_data_X))
print("Proportion of diabetic data in oversampled data is ",len(os_data_y[os_data_y['y']==1])/len(os_data_X))

#feature scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
#print(X_train)
#print(X_test)

#MLP model fit
from sklearn.neural_network import MLPClassifier
classifier = MLPClassifier(hidden_layer_sizes=(5,5,5), max_iter=1000,activation = 'relu',solver='adam',random_state=1)
#fitting training data
classifier.fit(X_train, y_train)

#logistic regression model fit
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
logreg = LogisticRegression()
logreg.fit(X_train, y_train)

#predicting
y_pred = logreg.predict(X_test)
print(y_pred)

#predicting
y_pred = classifier.predict(X_test)
print(y_pred)

#accuracy
c=0
for i in range(0,len(y_pred)):
    if(y_pred[i]==y_test[i]):
        c=c+1
accuracy=c/len(y_pred)
print("Accuracy is")
print(accuracy)

#confusion matrix
from sklearn.metrics import confusion_matrix
confusion_matrix = confusion_matrix(y_test, y_pred)
print(confusion_matrix)

#Compute precision, recall, F-measure and support
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))

