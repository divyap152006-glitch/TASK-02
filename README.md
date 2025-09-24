# TASK-02
# Titanic Dataset Analysis

This project performs **Exploratory Data Analysis (EDA)** on the Titanic
dataset using Python. It includes loading the dataset, handling missing
values, performing statistical analysis, and generating multiple
visualizations to extract insights.

------------------------------------------------------------------------

## **Project Steps**

1.  Load the dataset\
2.  Display basic dataset information\
3.  Handle missing values\
4.  Perform Exploratory Data Analysis (EDA):
    -   Histograms for numeric features\
    -   Boxplots for outlier detection\
    -   Correlation matrix heatmap\
    -   Pairplot for numeric features\
    -   Interactive Plotly visualizations\
5.  Analyze feature-level value counts

------------------------------------------------------------------------

## **Requirements**

Install the required Python libraries before running the code:

``` bash
pip install pandas numpy matplotlib seaborn plotly
```

------------------------------------------------------------------------

## **Code Workflow**

### **1. Import Libraries**

``` python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
```

### **2. Load Dataset**

``` python
file_path = r"C:\Users\Divya P\Downloads\Titanic-Dataset (21).csv"
df = pd.read_csv(file_path)
```

### **3. Basic Info & Statistics**

-   View first 5 rows with `df.head()`\
-   Dataset info with `df.info()`\
-   Statistical summary with `df.describe()`

### **4. Missing Values**

-   Identify missing values using `df.isnull().sum()`\
-   Handle missing values:
    -   Categorical → Fill with **mode**\
    -   Numeric → Fill with **median**

### **5. Exploratory Data Analysis (EDA)**

#### **a. Histograms**

Visualize the distribution of numeric features.

#### **b. Boxplots**

Detect outliers in numeric columns.

#### **c. Correlation Matrix**

Show correlations between numeric variables using a heatmap.

#### **d. Pairplot**

Explore relationships among numeric variables.

#### **e. Interactive Plotly Visualization**

Use Plotly for dynamic visualizations (e.g., Age vs Survival).

------------------------------------------------------------------------

## **Usage**

1.  Save the Python code in a file, e.g., `titanic_analysis.py`\
2.  Update the `file_path` with your dataset location\
3.  Run the script:

``` bash
python titanic_analysis.py
```

4.  Visualizations will be displayed automatically

------------------------------------------------------------------------

## **Outputs**

-   **Histograms** for numeric features\
-   **Boxplots** for outlier detection\
-   **Correlation heatmap**\
-   **Pairplots** for relationships\
-   **Interactive Age vs Survival plot**\
-   **Value counts** for categorical features
 

