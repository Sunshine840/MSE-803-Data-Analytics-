import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("messy_dataset_Mukesh.csv")

print("Original Dataset")
print(df)

# ----------------------------
# DATA CLEANING
# ----------------------------

# Remove duplicates
df = df.drop_duplicates()

# Standardize Country names
df["Country"] = df["Country"].replace({"AU": "AUS"})

# Convert Age column
df["Age"] = df["Age"].replace({"thirty-eight": 38})

df["Age"] = pd.to_numeric(df["Age"], errors="coerce")

# Convert Salary column
df["Salary"] = df["Salary"].replace({"sixty five thousand": 65000})

df["Salary"] = pd.to_numeric(df["Salary"], errors="coerce")

# Convert dates
df["Join Date"] = pd.to_datetime(df["Join Date"], errors="coerce", dayfirst=True)

# Fill missing values
df["Age"].fillna(df["Age"].median(), inplace=True)
df["Salary"].fillna(df["Salary"].median(), inplace=True)

df["Country"].fillna(df["Country"].mode()[0], inplace=True)
df["Name"].fillna("Unknown", inplace=True)

# Remove rows with missing ID
df = df.dropna(subset=["ID"])

print("\nCleaned Dataset")
print(df)

# ----------------------------
# CORRELATION HEATMAP
# ----------------------------

numeric_df = df[["Age", "Salary"]]

correlation = numeric_df.corr(method="pearson")

plt.figure(figsize=(6, 4))
sns.heatmap(correlation, annot=True, cmap="coolwarm")
plt.title("Pearson Correlation Heatmap")
plt.show()

# ----------------------------
# OUTLIER DETECTION
# ----------------------------

plt.figure(figsize=(6, 4))
sns.boxplot(y=df["Salary"])
plt.title("Salary Outlier Detection")
plt.show()

plt.figure(figsize=(6, 4))
sns.boxplot(y=df["Age"])
plt.title("Age Outlier Detection")
plt.show()
