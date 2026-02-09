import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("student_performance.csv")

# Data Exploration
df.head()
df.info()
df.describe()
df.isnull().sum()
df.duplicated().sum()
df=df.drop_duplicates()

# Handling Missing Vvalues - using numpy practice
# num_arr = df.select_dtypes(include=np.number)
# arr = num_arr.to_numpy()
# arr=np.nan_to_num(arr,nan=np.nanmean(arr))
# print(np.mean(arr))
# print(np.median(arr))
# print(np.std(arr))
# sleeps = arr[arr[:,-4]>=6]
# print(sleeps)


#  Handling Missing Values
numeric_col = [
    "Student_ID",
    "Age",
    "Attendance",
    "Study_Hours",
    "Sleep_Hours",
    "Screen_Hours",
    "Previous_Grade",
    "Final_Grade"
]

for cols in numeric_col:
    if cols  in df.columns:
        median_val = df[cols].median()
        df[cols]=df[cols].fillna(median_val)


# simpler way to fill missing numeric values with median
# num_cols = df.select_dtypes(include=np.number).columns
# df[num_cols] = df[num_cols].fillna(df[num_cols].median())


df.isnull().sum()
df["Gender"] = df["Gender"].fillna("Unknown")
df["Gender"] = df["Gender"].map({
    "Male":0,
    "Female":1,
    "Unknown":2
})




# Data Visualization

df.corr()["Final_Grade"].sort_values(ascending=False)


df=df.drop(["Student_ID","Gender"],axis =1)
df.head()

sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.show()

plt.figure(figsize=(7,5))
sns.scatterplot(
    x="Sleep_Hours",
    y="Final_Grade",
    data=df,
    alpha=0.7
)
sns.regplot(
    x="Sleep_Hours",
    y="Final_Grade",
    data=df,
    scatter=False,
    color="red",
)
plt.title("Final Grade vs Sleep Hours")
plt.show()



plt.figure(figsize=(8,5))
sns.scatterplot(
    x="Study_Hours",
    y="Final_Grade",
    data=df,
    alpha=0.8
)
sns.regplot(
    x="Study_Hours",
    y="Final_Grade",
    data=df,
    scatter=False,
    color="Yellow"
)
plt.title("How Study Hours affects Final Grade")
plt.show()



df["Improvement"] = df["Final_Grade"] - df["Previous_Grade"]


plt.figure(figsize=(8,5))
sns.scatterplot(
    x="Improvement",
    y="Study_Hours",
    data=df,
    alpha=0.8
)
sns.regplot(
    x="Improvement",
    y="Study_Hours",
    data=df,
    scatter=False,
    color="Green"
)
plt.title("Study Hours Impact on Improvement")
plt.show()
