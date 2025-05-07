
import numpy as np
import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv")

df.groupby('species').describe()

df.groupby('species').mean()

df.groupby('species').std()

set1 = (df['species'] == 'virginica')
print(df[set1].describe())

set1 = (df['species'] == 'versicolor')
print(df[set1].describe())

set1 = (df['species'] == 'setosa')
print(df[set1].describe())

df['species'].unique()

df = pd.read_csv('3.Mall_Customers.csv')
df

df.describe()

df.min()

df.groupby(['Gender'])['Age'].mean()

df.groupby(['Gender'])['Age'].median()

df.groupby(['Gender'])['Age'].std()

df.groupby(['Gender'])['Annual Income (k$)'].mean()

df.groupby(['Gender'])['Annual Income (k$)'].median()

df.groupby(['Gender'])['Annual Income (k$)'].std()


df.groupby(['Gender'])['Age'].median()

df.groupby(['Gender']).mean()

df.groupby(['Gender']).median()

df.groupby(['Gender']).min()

df.groupby(['Gender']).max()

