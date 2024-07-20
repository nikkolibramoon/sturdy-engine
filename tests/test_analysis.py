import pandas as pd
import pytest
from src.analysis import analyze_data

@pytest.fixture(scope="module")
def sample_data():
    """Fixture to provide sample data for testing."""
    data = {
        'Customer ID': [1, 2, 3, 4],
        'Gender': ['Male', 'Female', 'Female', 'Male'],
        'Age': [25, 30, 22, 40],
        'City': ['CityA', 'CityB', 'CityA', 'CityB'],
        'Membership Type': ['Gold', 'Silver', 'Gold', 'Silver'],
        'Total Spend': [1200, 800, 1500, 600],
        'Items Purchased': [5, 3, 7, 2],
        'Average Rating': [4.5, 4.0, 5.0, 3.5],
        'Discount Applied': [0.1, 0.2, 0.1, 0.3],
        'Days Since Last Purchase': [30, 45, 20, 60],
        'Satisfaction Level': [8, 7, 9, 6]
    }
    return pd.DataFrame(data)

def test_analyze_data(sample_data):
    result = analyze_data(sample_data)
    expected = sample_data.describe()
    
    # Check if the result is a DataFrame and has the same content as the expected DataFrame
    assert isinstance(result, pd.DataFrame)
    pd.testing.assert_frame_equal(result, expected)

if __name__ == "__main__":
    pytest.main()
