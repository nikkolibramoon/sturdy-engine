import pandas as pd

def analyze_data(df):
    summary = df.describe()
    return summary

if __name__ == "__main__":
    processed_data_path = 'data/processed/ecommerce_data_cleaned.csv'
    
    data = pd.read_csv(processed_data_path)
    summary = analyze_data(data)
    print(summary)
