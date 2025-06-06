
import pandas as pd
import numpy as np
df=pd.read_csv('https://www.stats.govt.nz/assets/Uploads/Annual-enterprise-survey/Annual-enterprise-survey-2023-financial-year-provisional/Download-data/annual-enterprise-survey-2023-financial-year-provisional.csv')
df

df.info()

df.head(5)

df.tail(5)

df.describe()

print(df.size)

df.shape

df.isnull()

df.notnull()

df.isnull().sum()

df.fillna(0.1)

df.ffill()

df.bfill()

df.dropna()

df.drop_duplicates()
df.dtypes

df['Value'] = pd.to_numeric(df['Value'],errors='coerce')

df['Value'] = (
    df['Value'] - df['Value'].min()
) / (
    df['Value'].max() - df['Value'].min()
)

df.head()

df['Value']=(
    df['Value']-df['Value'].mean()
)/ df['Value'].std()

df

data={'Name':['Jeetu','Rohan','Sanket','Arjun'],'Education':['D','UG','PG','G']}
ds=pd.DataFrame(data)
ds

ds['Education']=ds['Education'].replace(['D','UG','PG','G'],[1,2,3,4])
ds


