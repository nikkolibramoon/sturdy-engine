import pytest
import pandas as pd
from unittest.mock import patch, MagicMock
from src.visualization import plot_spend_distribution

@pytest.fixture
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

@patch('src.visualization.plt.show')
@patch('src.visualization.sns.histplot')
@patch('src.visualization.plt.figure')
def test_plot_spend_distribution(mock_figure, mock_histplot, mock_show, sample_data):
    """Test the plot_spend_distribution function."""

    mock_figure.return_value = MagicMock()
    mock_histplot.return_value = MagicMock()
    

    plot_spend_distribution(sample_data)
    

    assert mock_figure.call_count > 0
    

    call_args_list = mock_figure.call_args_list
    figure_calls = [call for call in call_args_list if call[1].get('figsize') == (10, 6)]
    assert len(figure_calls) > 0, "plt.figure was not called with figsize=(10, 6)"
    

    mock_histplot.assert_called_once_with(sample_data['Total Spend'], kde=True)
    

    mock_show.assert_called_once()

if __name__ == "__main__":
    pytest.main()
