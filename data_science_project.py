# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load datasets
try:
    df_1 = pd.read_csv("used_car_dataset.csv")
    df_2 = pd.read_csv("ecommerce_dataset_updated.csv")
    print("Datasets loaded successfully.")
except FileNotFoundError as e:
    print(f"Error: {e}")
    raise

# Display basic information about each dataset
print("\nDataset 1 Information:")
df_1.info()
print("\nDataset 1 Summary Statistics:")
print(df_1.describe())

print("\nDataset 2 Information:")
df_2.info()
print("\nDataset 2 Summary Statistics:")
print(df_2.describe())

# Merge datasets and reset the index
df_merge = pd.concat([df_1, df_2], axis=0, ignore_index=True)

# Display merged dataset information
print("\nMerged Dataset Information:")
df_merge.info()

# Check for missing values
print("\nMissing Values in Merged Dataset:")
print(df_merge.isnull().sum())

# Drop duplicates
df_merge = df_merge.drop_duplicates()

# Visualize histograms for numerical data
numerical_columns = df_merge.select_dtypes(include=[np.number]).columns
if not numerical_columns.empty:
    df_merge[numerical_columns].hist(figsize=(12, 10), bins=20, color='skyblue', edgecolor='black')
    plt.suptitle('Distribution of Numerical Features', fontsize=16)
    plt.tight_layout()
    plt.show()
else:
    print("No numerical columns to visualize.")

# Plot number of cars by brand if the column exists
if "Brand" in df_merge.columns:
    brand_counts = df_merge["Brand"].value_counts()
    plt.figure(figsize=(17, 6))
    brand_counts.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title('Number of Cars by Brand', fontsize=16)
    plt.xlabel('Brand', fontsize=14)
    plt.ylabel('Count', fontsize=14)
    plt.xticks(rotation=45, fontsize=12)
    plt.tight_layout()
    plt.show()
else:
    print("'Brand' column not found in the merged dataset.")

# Visualize correlations if numerical data exists
if len(numerical_columns) > 1:
    correlation_matrix = df_merge[numerical_columns].corr()
    plt.figure(figsize=(12, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
    plt.title('Correlation Matrix', fontsize=16)
    plt.show()
else:
    print("Not enough numerical columns for correlation analysis.")

# Save cleaned dataset
output_file = "merged_cleaned_data.csv"
df_merge.to_csv(output_file, index=False)
print(f"\nCleaned dataset saved to {output_file}.")
