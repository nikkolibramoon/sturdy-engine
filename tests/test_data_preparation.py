import pytest
import pandas as pd
from src.data_preparation import clean_data

def test_clean_data():

    data = {
        'Customer ID': [1, 2, 3],
        'Gender': ['Male', 'Female', 'Male'],
        'Age': [25, 35, 45],
        'City': ['New York', 'Los Angeles', 'Chicago'],
        'Membership Type': ['Silver', 'Gold', 'Platinum'],
        'Total Spend': [100, None, 300],
        'Items Purchased': [10, 20, 30],
        'Average Rating': [4.5, 4.0, 5.0],
        'Discount Applied': [10, 20, 30],
        'Days Since Last Purchase': [5, 10, 15],
        'Satisfaction Level': [4, 3, 5]
    }
    df = pd.DataFrame(data)
    

    cleaned_df = clean_data(df)

    assert cleaned_df.isnull().sum().sum() == 0
    assert len(cleaned_df) == 2  

if __name__ == "__main__":
    pytest.main()
