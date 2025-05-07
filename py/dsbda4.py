
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

df=pd.read_csv('HousingData.csv')
df

df = df.dropna()

df.columns

x=df[['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX',
       'PTRATIO', 'B', 'LSTAT']]

y=df["MEDV"]

df = df.dropna()
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

model=LinearRegression()
print(x_train.isnull().sum())

model.fit(x_train,y_train)

y_pred=model.predict(x_test)

y_pred

model.score(x_test,y_test)

np.sqrt(mean_squared_error(y_test,y_pred))
