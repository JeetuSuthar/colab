
import pandas as pd
import numpy as np

data = [
    {"RollNo": 1, "FirstName": "John", "LastName": "Doe", "Gender": "Male", "Div": "A", "Grade": "A", "Attendance": 90.0},
    {"RollNo": 2, "FirstName": "Jane", "LastName": "Smith", "Gender": "Female", "Div": "B", "Grade": "B+", "Attendance": 85.0},
    {"RollNo": 3, "FirstName": "Mike", "LastName": "Johnson", "Gender": "Male", "Div": "C", "Grade": "B", "Attendance": 78.0},
    {"RollNo": 4, "FirstName": "Amy", "LastName": "Williams", "Gender": "Female", "Div": "A", "Grade": "A", "Attendance": 95.0},
    {"RollNo": 5, "FirstName": "Chris", "LastName": "Brown", "Gender": "Male", "Div": "B", "Grade": "C", "Attendance": 88.0},
    {"RollNo": 6, "FirstName": "Anna", "LastName": "Wilson", "Gender": "Female", "Div": "1", "Grade": "A", "Attendance": 85.0},
    {"RollNo": 7, "FirstName": "David", "LastName": "Moore", "Gender": "Male", "Div": "A", "Grade": "B", "Attendance": 130.0},
    {"RollNo": 8, "FirstName": "Susan", "LastName": "Taylor", "Gender": "Female", "Div": "B", "Grade": "C", "Attendance": 70.0},
    {"RollNo": 9, "FirstName": "James", "LastName": "Anderson", "Gender": "Male", "Div": "C", "Grade": "A", "Attendance": 80.0},
    {"RollNo": 10, "FirstName": "Linda", "LastName": "Harris", "Gender": "Female", "Div": "A", "Grade": "B+", "Attendance": 75.0},
    {"RollNo": 11, "FirstName": "Patricia", "LastName": "Martin", "Gender": "Female", "Div": "C", "Grade": "C", "Attendance": 93.0},
    {"RollNo": 12, "FirstName": "Robert", "LastName": "Lee", "Gender": "Male", "Div": "A", "Grade": "A", "Attendance": 85.0},
    {"RollNo": 13, "FirstName": "Lisa", "LastName": "Walker", "Gender": "Female", "Div": "B", "Grade": "B", "Attendance": 4.0},
    {"RollNo": 14, "FirstName": "Michael", "LastName": "Young", "Gender": "Male", "Div": "C", "Grade": "C", "Attendance": 90.0},
    {"RollNo": 15, "FirstName": "Sarah", "LastName": "King", "Gender": "Female", "Div": "A", "Grade": "A", "Attendance": 88.0},
    {"RollNo": 16, "FirstName": "Daniel", "LastName": "Scott", "Gender": "Male", "Div": "B", "Grade": "B", "Attendance": None},
    {"RollNo": 17, "FirstName": "Thomas", "LastName": "Jackson", "Gender": "Female", "Div": "C", "Grade": "A", "Attendance": 98.0},
    {"RollNo": 18, "FirstName": "Jessica", "LastName": "White", "Gender": "Female", "Div": "A", "Grade": "B", "Attendance": 10.0},
    {"RollNo": 19, "FirstName": "William", "LastName": "Hernandez", "Gender": "Male", "Div": "C", "Grade": "C", "Attendance": 72.0},
    {"RollNo": 20, "FirstName": "Emily", "LastName": "Brown", "Gender": "Female", "Div": "A", "Grade": "A", "Attendance": 85.0}
]
df=pd.DataFrame(data)
df

df.isnull().sum()

df.dtypes

df.bfill()

df.isnull().sum()

df['Div'].value_counts()

df['Div'].replace({'1':'A'})

Q1 = df['Attendance'].quantile(0.25)
Q3 = df['Attendance'].quantile(0.75)
IQR = Q3 - Q1

outliers = df[
    ((df['Attendance'] < (Q1 - 1.5 * IQR)) |
      (df['Attendance'] > (Q3 + 1.5 * IQR)))
]

print(outliers)



df['RollNo'] = (df['RollNo']- df['RollNo'].min()) / (df['RollNo'].max()-df['RollNo'].min())

df['RollNo'] = (df['RollNo']- df['RollNo'].min()) / (df['RollNo'].max()-df['RollNo'].min())

df

df['Attendance'] = (df['Attendance']- df['Attendance'].mean()) /(df['Attendance'].std())

df

outliers = df[abs(df['Attendance']) > 1]
outliers

