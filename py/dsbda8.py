
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=sns.load_dataset('titanic')

df.isnull().sum()

sns.catplot(x="sex",hue="survived",kind="count",data=df)

group=df.groupby(['pclass','survived']).size().unstack()
sns.heatmap(group,annot=True,fmt="d")

sns.violinplot(x="sex",y="age",hue="survived",data=df,split=True)

df['age']=df['age'].fillna(df['age'].mean())

sns.violinplot(x="sex",y="age",hue="survived",data=df,split=True)

sns.distplot(df['fare'])

sns.distplot(df['fare'],kde=True)

sns.distplot(df['fare'],kde = False)

