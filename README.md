# CodeAlpha Internship – Task 3: Data Visualization

## Project Overview

This project was completed as part of the CodeAlpha Data Analytics Internship.

The objective of this task is to transform the book dataset into meaningful visualizations using Python and Matplotlib.

The visualizations help identify patterns in book prices, ratings, and the relationship between price and rating.

## Dataset

The dataset contains information about books collected from the Books to Scrape website.

### Columns Used

- Title
- Price
- Rating
- Availability
- Book_URL

## Technologies Used

- Python
- Pandas
- Matplotlib

## Visualizations Created

### 1. Book Price Distribution

A histogram was created to show how book prices are distributed across the dataset.

**File:** `price_distribution.png`

### 2. Book Rating Distribution

A bar chart was created to show the number of books for each rating from 1 to 5.

**File:** `rating_distribution.png`

### 3. Price vs Rating

A scatter plot was created to examine the relationship between book price and rating.

**File:** `price_vs_rating.png`

### 4. Top 10 Most Expensive Books

A horizontal bar chart was created to identify the 10 most expensive books in the dataset.

**File:** `top_10_expensive_books.png`

## Key Insights

- Book prices vary considerably across the dataset.
- Books are available across rating levels from 1 to 5.
- The price vs rating visualization shows no strong visible relationship between price and rating.
- The calculated correlation between price and rating was approximately 0.028, indicating almost no linear relationship.
- A small number of books have considerably higher prices than most other books.
- The top 10 visualization makes it easier to identify the most expensive books.

## Project Structure

CodeAlpha_DataVisualization/

├── books_dataset.csv  
├── visualization.py  
├── price_distribution.png  
├── rating_distribution.png  
├── price_vs_rating.png  
├── top_10_expensive_books.png  
└── README.md

## Conclusion

The visualizations provide a clear understanding of the book dataset and make important patterns easier to interpret.

The analysis shows that book price and rating have almost no linear relationship in this dataset.

## Internship Information

Program: CodeAlpha Data Analytics Internship

Task: Task 3 – Data Visualization