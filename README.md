# E-commerce Customer Behavior Analysis

This project analyzes customer behavior data from an e-commerce platform. 
It includes data preparation, analysis, and visualization steps to provide insights into customer spending patterns, product preferences, and overall satisfaction levels.

## Table of Contents

- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Data Description](#data-description)
- [Analysis and Visualizations](#analysis-and-visualizations)
- [Testing](#testing)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Setup Instructions

1. **Clone the repository**:
   ```sh
   git clone https://github.com/your-username/ecommerce-analysis.git
   cd ecommerce-analysis
   ```

2. **Create and activate a virtual environment:**:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. **Install the dependencies:**:
   ```sh
   pip install -r requirements.txt
   ```
4. **Prepare the data:**:
- Place the raw data file EcommerceCustomerBehavior.csv in the data/raw/ directory.

## Usage

### Data Preparation
**Prepare the data:**
Run the data preparation script to clean and preprocess the raw data:
```sh
python src/data_preparation.py
```

### Data Analysis

Perform analysis on the cleaned data:
```sh
python src/analysis.py
```

### Visualization

Generate visualizations for the data:
```sh
python src/visualization.py
```

## Data Description

The dataset contains the following columns:

- Customer ID: Unique identifier for each customer
- Gender: Gender of the customer
- Age: Age of the customer
- City: City where the customer resides
- Membership Type: Type of membership the customer has
- Total Spend: Total amount spent by the customer
- Items Purchased: Number of items purchased by the customer
- Average Rating: Average rating given by the customer
- Discount Applied: Discount applied on purchases
- Days Since Last Purchase: Number of days since the customer's last purchase
- Satisfaction Level: Satisfaction level of the customer

 ## Analysis and Visualizations
 
 ### Spend Distribution
 The distribution of total spend among customers is visualized below:
 
![spend_distribution](https://github.com/user-attachments/assets/85772779-0661-4d2a-be6f-47292b56bb8e)

This histogram shows the frequency distribution of total spending, indicating the spread and central tendencies in customer expenditure.

 ## Testing
 
 To run the tests, use the following command:
 ```sh
pytest
```

## Results

The cleaned dataset provides insights into customer behaviour, including spending patterns, product preferences, and satisfaction levels. 
Key metrics and visualizations are included in the reports/summary_report.md.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Make your changes.
4. Commit your changes (git commit -m 'Add some feature').
5. Push to the branch (git push origin feature-branch).
6. Create a pull request.

## License

[MIT](https://choosealicense.com/licenses/mit/)




