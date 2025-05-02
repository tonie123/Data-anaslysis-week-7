import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Task 1: Load and Explore the Dataset
def load_and_explore_data():
    try:
        # Load the Iris dataset
        iris = load_iris()
        df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
        df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

        print("\nFirst few rows of the dataset:")
        print(df.head())

        print("\nDataset information:")
        print(df.info())

        print("\nChecking for missing values:")
        print(df.isnull().sum())

        return df

    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None

# Task 2: Basic Data Analysis
def perform_basic_analysis(df):
    if df is None:
        return

    try:
        print("\nBasic statistics of numerical columns:")
        print(df.describe())

        print("\nMean values grouped by species:")
        print(df.groupby('species').mean())

    except Exception as e:
        print(f"Error performing basic analysis: {e}")

# Task 3: Data Visualization
def create_visualizations(df):
    if df is None:
        return

    try:
        # Set the style and color palette for all plots
        sns.set_style("whitegrid")
        sns.set_palette("husl")

        # Create a figure with subplots
        fig = plt.figure(figsize=(16, 12))

        # 1. Line chart - trends of sepal length by species
        plt.subplot(2, 2, 1)
        for species in df['species'].unique():
            species_data = df[df['species'] == species]['sepal length (cm)'].values
            plt.plot(species_data, marker='o', label=species, linewidth=2, markersize=6)
        plt.title('Sepal Length Trends by Species', fontsize=12, pad=15)
        plt.xlabel('Sample Index', fontsize=10)
        plt.ylabel('Sepal Length (cm)', fontsize=10)
        plt.legend(title='Species', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.grid(True, linestyle='--', alpha=0.7)

        # 2. Bar chart - average measurements by species with error bars
        plt.subplot(2, 2, 2)
        species_means = df.groupby('species')['petal length (cm)'].agg(['mean', 'std']).reset_index()
        bar_plot = plt.bar(species_means['species'], species_means['mean'], 
                          yerr=species_means['std'], capsize=5)
        plt.title('Average Petal Length by Species (with Standard Deviation)', fontsize=12, pad=15)
        plt.xlabel('Species', fontsize=10)
        plt.ylabel('Average Petal Length (cm)', fontsize=10)
        plt.xticks(rotation=45)
        
        # Add value labels on top of bars
        for bar in bar_plot:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height,
                     f'{height:.2f}', ha='center', va='bottom')

        # 3. Enhanced histogram - distribution of sepal width
        plt.subplot(2, 2, 3)
        for species in df['species'].unique():
            species_data = df[df['species'] == species]['sepal width (cm)']
            plt.hist(species_data, bins=15, alpha=0.5, label=species, edgecolor='black')
        plt.title('Distribution of Sepal Width by Species', fontsize=12, pad=15)
        plt.xlabel('Sepal Width (cm)', fontsize=10)
        plt.ylabel('Frequency', fontsize=10)
        plt.legend(title='Species')
        plt.grid(True, linestyle='--', alpha=0.7)

        # 4. Scatter plot with regression lines
        plt.subplot(2, 2, 4)
        sns.scatterplot(data=df, x='sepal length (cm)', y='petal length (cm)',
                        hue='species', style='species', s=100)
        for species in df['species'].unique():
            species_data = df[df['species'] == species]
            sns.regplot(data=species_data, x='sepal length (cm)', y='petal length (cm)',
                        scatter=False, label=f'{species} trend')
        plt.title('Sepal Length vs Petal Length with Trend Lines', fontsize=12, pad=15)
        plt.legend(title='Species', bbox_to_anchor=(1.05, 1), loc='upper left')

        # Adjust layout and display
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"Error creating visualizations: {e}")

def main():
    try:
        # Load and explore data
        print("Loading and exploring the Iris dataset...")
        df = load_and_explore_data()

        # Perform basic analysis
        print("\nPerforming basic data analysis...")
        perform_basic_analysis(df)

        # Create visualizations
        print("\nCreating visualizations...")
        create_visualizations(df)

    except Exception as e:
        print(f"Error in main execution: {e}")

if __name__ == "__main__":
    main()