

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix, precision_score,recall_score

df=pd.read_csv('Social_Network_Ads.csv')
df.head()

df.describe()

df.isnull().sum()

x=df[['Age','EstimatedSalary']]
y=df['Purchased']

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

scaler=StandardScaler()
x_train=scaler.fit_transform(x_train)
x_test=scaler.transform(x_test)
print(x_train)
print(x_test)

model=LogisticRegression()
model.fit(x_train,y_train)

y_pred=model.predict(x_test)
y_pred

cm=confusion_matrix(y_test,y_pred)
ac=accuracy_score(y_test,y_pred)
cr=classification_report(y_test,y_pred)
recall=recall_score(y_test,y_pred)
precision=precision_score(y_test,y_pred)
accuracy=accuracy_score(y_test,y_pred)
print(cm)
print(accuracy)
print(recall)
print(precision)
print(cr)

error=1-accuracy
print(error)

