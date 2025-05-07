

import numpy as np
import pandas as pd

df=pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/iris-data.csv')
df

df.head(5)

df.isnull().sum()

x=df[['sepal length',  'sepal width',  'petal length',  'petal width']]
y=df['class']

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

from sklearn.naive_bayes import GaussianNB
model=GaussianNB()
model.fit(x_train,y_train)

y_pred=model.predict(x_test)
model.score(x_test,y_test)

from sklearn.metrics import confusion_matrix,accuracy_score,precision_score,recall_score, classification_report
cm=confusion_matrix(y_test,y_pred)
ac=accuracy_score(y_test,y_pred)
p=precision_score(y_test,y_pred,average='weighted')
r=recall_score(y_test,y_pred,average='weighted')
cp=classification_report(y_test,y_pred)

print(cm,ac,p,r,cp)

error=1-ac
print(error)

