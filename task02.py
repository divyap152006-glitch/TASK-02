
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Optional: display plots inline if using Jupyter Notebook
# %matplotlib inline

# Step 2: Load Dataset
file_path = (r"C:\Users\Divya P\Downloads\Titanic-Dataset (16).csv") # Update path
try:
    df = pd.read_csv(file_path)
    print("CSV loaded successfully!")
except Exception as e:
    print("Error loading CSV:", e)

# Step 3: Basic Information & Summary Statistics
print("\n--- First 5 Rows ---")
print(df.head())

print("\n--- Dataset Info ---")
print(df.info())

print("\n--- Statistical Summary ---")
print(df.describe())

# Step 4: Check for Missing Values
print("\n--- Missing Values ---")
print(df.isnull().sum())

# Step 5: Handle Missing Values (simple approach)
for col in df.columns:
    if df[col].dtype == 'object':
        df[col].fillna(df[col].mode()[0], inplace=True)
    else:
        df[col].fillna(df[col].median(), inplace=True)

# Step 6: Exploratory Data Analysis (EDA)

# 6a: Histograms for numeric features
numeric_cols = df.select_dtypes(include=np.number).columns
df[numeric_cols].hist(figsize=(12,10), bins=20)
plt.suptitle("Histograms of Numeric Features")
plt.show()

# 6b: Boxplots to detect outliers
for col in numeric_cols:
    plt.figure(figsize=(6,4))
    sns.boxplot(x=df[col])
    plt.title(f"Boxplot of {col}")
    plt.show()

# 6c: Correlation matrix
plt.figure(figsize=(10,6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Matrix")
plt.show()

# 6d: Pairplot using Seaborn
sns.pairplot(df[numeric_cols])
plt.suptitle("Pairplot of Numeric Features", y=1.02)
plt.show()

# 6e: Optional: Interactive Plotly visualization
fig = px.histogram(df, x='Age', nbins=20, color='Survived', title="Age Distribution by Survival")
fig.show()

# Step 7: Basic Feature-Level Inferences
print("\n--- Feature-Level Insights ---")
for col in df.select_dtypes(include='object').columns:
    print(f"\nValue counts for {col}:")
    print(df[col].value_counts())