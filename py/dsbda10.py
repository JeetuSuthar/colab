import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df=sns.load_dataset('iris')
print(df)

df.isnull().sum()

df.dtypes

df.hist()
plt.show()

sns.histplot(df['sepal_length'],kde=True)

sns.histplot(df['sepal_width'])

sns.histplot(df['petal_length'])

sns.histplot(df['petal_width'])

df.boxplot()
plt.show()

sns.boxplot(x='species',y='sepal_length',data=df)
plt.title('Distribution of sepal length')
plt.show()

sns.boxplot(x='species',y='sepal_width',data=df)
plt.title('Distribution of sepal width')
plt.show()

sns.boxplot(x='species',y='petal_length',data=df)
plt.title('Distribution of petal_length')
plt.show()

sns.boxplot(x='species',y='petal_width',data=df)
plt.title('Distribution of petal width')
plt.show()

Q1 = df['sepal_width'].quantile(0.25)   # 25th percentile (lower quartile)
Q3 = df['sepal_width'].quantile(0.75)   # 75th percentile (upper quartile)
IQR = Q3 - Q1                           # Interquartile Range

outliers = df[
    (df['sepal_width'] < (Q1 - 1.5 * IQR)) |
    (df['sepal_width'] > (Q3 + 1.5 * IQR))
]

print(outliers)

Q1 = df['sepal_width'].quantile(0.25)   # 25th percentile (lower quartile)
Q3 = df['sepal_width'].quantile(0.75)   # 75th percentile (upper quartile)
IQR = Q3 - Q1                           # Interquartile Range

outliers = df[
    ~((df['sepal_width'] < (Q1 - 1.5 * IQR)) |
    (df['sepal_width'] > (Q3 + 1.5 * IQR)))
]

print(outliers)

sns.boxplot(x='species',y='sepal_width',data=outliers)
plt.title('Distribution of Sepal Width')
plt.show()

