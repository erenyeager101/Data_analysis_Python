# This was my dataset for Heart disease detection uisng ML so this is how we can do data analysis on it
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_and_inspect_data():
    """Load the dataset and perform initial inspection"""
    print("=== Initial Data Inspection ===")
    # Load the dataset
    heart_df = pd.read_csv('heart.csv') 
    print("\nFirst 5 rows:")
    display(heart_df.head())
    
    print("\nDataset info:")
    print(heart_df.info())
    
    print("\nDescriptive statistics:")
    print(heart_df.describe())
     
    print("\nMissing values per column:")
    print(heart_df.isnull().sum())
    
    return heart_df

def visualize_target_distribution(df):
    """Visualize the distribution of the target variable"""
    print("\n=== Target Variable Analysis ===")
    if 'target' in df.columns:
        plt.figure(figsize=(6, 4))
        sns.countplot(x='target', data=df)
        plt.title('Distribution of Target Variable')
        plt.show()
         
        class_dist = df['target'].value_counts(normalize=True) * 100
        print("\nClass distribution (%):")
        print(class_dist)
    else:
        print('No target column found.')

def clean_data(df):
    """Perform data cleaning operations"""
    print("\n=== Data Cleaning ===")
    # 1. Check for duplicates
    num_duplicates = df.duplicated().sum()
    print('Number of duplicate rows:', num_duplicates)
    if num_duplicates > 0:
        df = df.drop_duplicates()
        print('Duplicates dropped.')
    else:
        print('No duplicates found.')
    
    return df

def detect_outliers(df):
    """Detect outliers in numerical columns"""
    print("\n=== Outlier Detection ===")
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    outlier_summary = {}
    
    for col in numeric_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR
        outliers = ((df[col] < lower) | (df[col] > upper)).sum()
        outlier_summary[col] = outliers
    
    print('Outlier count per column:')
    print(outlier_summary)
    
    return outlier_summary

def analyze_categorical_features(df):
    """Analyze categorical features in the dataset"""
    print("\n=== Categorical Feature Analysis ===")
    for col in df.columns:
        unique_vals = df[col].unique()
        if df[col].dtype == 'object' or len(unique_vals) < 10:
            print(f'Column {col: <10} | Unique values ({len(unique_vals)}):', unique_vals)

def visualize_distributions(df):
    """Visualize distributions of key features"""
    print("\n=== Feature Distributions ===")
    # Select numerical features for visualization
    numerical_features = [col for col in df.columns if df[col].dtype in ['int64', 'float64']]
    
    plt.figure(figsize=(15, 10))
    for i, col in enumerate(numerical_features):
        plt.subplot(4, 4, i+1)
        sns.histplot(df[col], kde=True)
        plt.title(col)
        plt.tight_layout()
    plt.show()

def plot_correlation_heatmap(df):
    """Plot correlation heatmap for numerical features"""
    print("\n=== Feature Correlations ===")
    plt.figure(figsize=(12, 10))
    sns.heatmap(df.corr(), annot=True, fmt='.2f', cmap='coolwarm', center=0)
    plt.title('Correlation Heatmap')
    plt.show()

def main():
    # Load and inspect data
    heart_df = load_and_inspect_data() 
    visualize_target_distribution(heart_df) 
    heart_df = clean_data(heart_df) 
    detect_outliers(heart_df) 
    analyze_categorical_features(heart_df) 
    visualize_distributions(heart_df) 
    plot_correlation_heatmap(heart_df)
    
    print("\n=== Analysis Complete ===")
    return heart_df

# Execute the analysis
processed_data = main()
