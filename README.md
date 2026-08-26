# CodeAlpha Internship – Task 2: Exploratory Data Analysis

## Project Overview

This project was completed as part of the CodeAlpha Data Analytics Internship.

The objective of this task is to perform Exploratory Data Analysis (EDA) on a book dataset collected through web scraping.

The analysis helps understand the structure of the dataset, identify patterns, check data quality, and generate useful insights.

## Dataset

The dataset contains information about books collected from the Books to Scrape website.

### Columns

- Title
- Price
- Rating
- Availability
- Book_URL

## Technologies Used

- Python
- Pandas

## EDA Performed

The following analysis was performed:

1. Loaded the dataset using Pandas.
2. Displayed the first few records.
3. Checked the number of rows and columns.
4. Checked column names and data types.
5. Checked for missing values.
6. Checked for duplicate records.
7. Calculated descriptive statistics.
8. Calculated average, minimum, and maximum prices.
9. Analyzed book ratings.
10. Identified the cheapest and most expensive books.
11. Identified books above the average price.
12. Detected price outliers using the IQR method.
13. Calculated the correlation between price and rating.
14. Generated final insights from the analysis.

## Key Findings

- The dataset contains information about books, including their title, price, rating, availability, and URL.
- The dataset was checked for missing values and duplicate records.
- Book prices vary considerably across the dataset.
- Books have ratings ranging from 1 to 5.
- Some books have unusually high prices and can be considered price outliers.
- The correlation between price and rating is 0.028.
- This indicates almost no linear relationship between book price and rating.
- Therefore, a higher-priced book does not necessarily have a higher rating.

## Project Structure

CodeAlpha_EDA/

├── eda_analysis.py  
├── books_dataset.csv  
└── README.md

## Conclusion

The Exploratory Data Analysis provided a better understanding of the book dataset and identified important patterns related to price, rating, availability, and outliers.

The analysis shows that book price and rating have almost no linear relationship in this dataset.

## Internship Information

Program: CodeAlpha Data Analytics Internship

Task: Task 2 – Exploratory Data Analysis