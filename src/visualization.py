import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def plot_spend_distribution(df, save_path='reports/figures/spend_distribution.png'):
    """Plot and save the distribution of Total Spend."""
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Total Spend'], kde=True)
    plt.title('Total Spend Distribution')
    plt.xlabel('Total Spend')
    plt.ylabel('Frequency')
    

    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    

    plt.savefig(save_path)
    plt.close()  

if __name__ == "__main__":
    processed_data_path = 'data/processed/ecommerce_data_cleaned.csv'
    
    data = pd.read_csv(processed_data_path)
    plot_spend_distribution(data)
