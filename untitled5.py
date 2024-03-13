# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1A522FC0Lya2QOraUOEH5bdPwRdS8XG4_

Import Necessary **Libraries**
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

"""**Load the Iris dataset**"""

data=pd.read_csv('iris.csv')

"""**Split data into features (X) and target variable (y)**"""

X=data.iloc[:,:-1].values
y=data.iloc[:,-1].values

"""**Split data into training and testing sets**"""

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.30,random_state=1)

"""**Create and train a decision tree classifier (default parameters):**"""

#with default PRAMETER = to predict and accuracy
clf=DecisionTreeClassifier()
clf.fit(X_train,y_train)

"""**Make predictions and evaluate accuracy (default model)**"""

# Predict the dependent variable for the test set
pred=clf.predict(X_test)
acc=accuracy_score(y_test,pred)
print('prediction',pred)
print('accuracy',acc*100)

"""**Create and train a decision tree classifier (specific parameters):**"""

#another with criterion='entropy',max_depth=3 - to predict and accuracy
clf1=DecisionTreeClassifier(criterion='entropy',max_depth=3)
clf1.fit(X_train,y_train)

"""** Make predictions and evaluate accuracy (specific model)**"""

pred1=clf1.predict(X_test)
acc1=accuracy_score(y_test,pred1)
print('prediction',pred1)
print('accuracy',acc1*100)

"""**Visualize the decision tree (default model)**"""

plt.figure(figsize=(20,16))
tree.plot_tree(clf,fontsize=14,rounded=True,filled=True,max_depth=True)
plt.show()