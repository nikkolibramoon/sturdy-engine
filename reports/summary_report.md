# Summary Report

## 1. Introduction

In this report, we analyze the e-commerce customer behavior dataset. The objective is to gain insights into customer spending patterns and identify key factors affecting their behavior.

## 2. Data Overview

The dataset includes the following columns:
- **Customer ID**: Unique identifier for each customer.
- **Gender**: Gender of the customer.
- **Age**: Age of the customer.
- **City**: City where the customer resides.
- **Membership Type**: Type of membership the customer holds.
- **Total Spend**: Total amount spent by the customer.
- **Items Purchased**: Number of items purchased by the customer.
- **Average Rating**: Average rating given by the customer.
- **Discount Applied**: Discount applied to the customer's purchase.
- **Days Since Last Purchase**: Number of days since the customer last made a purchase.
- **Satisfaction Level**: Customer's satisfaction level.

## 3. Data Preparation

The raw data was loaded and cleaned using the following steps:
- Missing values were removed.
- Data types were ensured to be correct.

**Data Cleaning Process:**
- Removed rows with missing values.
- Ensured that all columns have the correct data types.

## 4. Analysis

### 4.1 Summary Statistics

The summary statistics of the cleaned data provide an overview of key metrics:

| Metric               | Value     |
|----------------------|-----------|
| Mean Total Spend     | 847.79    |
| Median Total Spend   | 780.20    |
| Standard Deviation   | 361.69    |
| Minimum Total Spend  | 410.80    |
| Maximum Total Spend  | 1520.10   |



### 4.2 Distribution of Total Spend

The distribution of total spend among customers is visualized below:

![Total Spend Distribution](reports/figures/spend_distribution.png)

This histogram shows the frequency distribution of total spend, indicating the spread and central tendencies in customer expenditure.

## 5. Insights

- **Spending Patterns**: From the distribution plot, we observe that a significant number of customers have high spending, which may indicate a skewed distribution.
- **Customer Segmentation**: By analyzing the total spend and other factors such as membership type and age, we can segment customers into different categories based on their spending behavior.

## 6. Conclusion

This analysis provides valuable insights into customer behavior, highlighting spending patterns and factors that influence spending. The findings can help in developing targeted marketing strategies and improving customer satisfaction.

## 7. Future Work

- Explore more detailed segments by combining age, city, and membership type.
- Analyze trends over time if historical data is available.

## 8. References

- [Dataset Source](URL to the dataset source)
- [Additional Resources](Links to any other relevant resources)

---


