import pandas as pd
from src.utils import read_csv, save_csv, ensure_directory_exists

def load_data(filepath):
    return read_csv(filepath)

def clean_data(df):
    df.dropna(inplace=True)
    return df

if __name__ == "__main__":
    raw_data_path = 'data/raw/EcommerceCustomerBehavior.csv'
    processed_data_path = 'data/processed/ecommerce_data_cleaned.csv'
    
    ensure_directory_exists('data/processed')
    
    try:
        data = load_data(raw_data_path)
        cleaned_data = clean_data(data)
        save_csv(cleaned_data, processed_data_path)
    except Exception as e:
        print(f"An error occurred: {e}")
