import pandas as pd

# Load the dataset
df = pd.read_csv("books_dataset.csv")

print("Dataset loaded successfully!")
print()

# Display first 5 rows
print("First 5 rows:")
print(df.head())
# --------------------------------------------------
# Basic Information About the Dataset
# --------------------------------------------------

print("\n" + "=" * 50)
print("DATASET INFORMATION")
print("=" * 50)

# Number of rows and columns
print("\nDataset shape:")
print(df.shape)

# Column names
print("\nColumn names:")
print(df.columns.tolist())

# Data types
print("\nData types:")
print(df.dtypes)

# Complete dataset information
print("\nDataset info:")
df.info()
# --------------------------------------------------
# Check Missing Values
# --------------------------------------------------

print("\n" + "=" * 50)
print("MISSING VALUES")
print("=" * 50)

missing_values = df.isnull().sum()

print(missing_values)
# --------------------------------------------------
# Check Duplicate Records
# --------------------------------------------------

print("\n" + "=" * 50)
print("DUPLICATE RECORDS")
print("=" * 50)

duplicates = df.duplicated().sum()

print("Number of duplicate rows:", duplicates)
# --------------------------------------------------
# Statistical Analysis
# --------------------------------------------------

print("\n" + "=" * 50)
print("STATISTICAL ANALYSIS")
print("=" * 50)

# Price statistics
print("\nPrice Statistics:")
print(df["Price"].describe())

# Average price
print("\nAverage book price:")
print(df["Price"].mean())

# Median price
print("\nMedian book price:")
print(df["Price"].median())

# Minimum price
print("\nMinimum book price:")
print(df["Price"].min())

# Maximum price
print("\nMaximum book price:")
print(df["Price"].max())

# Average rating
print("\nAverage book rating:")
print(df["Rating"].mean())
# --------------------------------------------------
# Meaningful Questions and Answers
# --------------------------------------------------

print("\n" + "=" * 50)
print("MEANINGFUL QUESTIONS")
print("=" * 50)


# Question 1
print("\n1. What is the cheapest book?")

cheapest_book = df.loc[df["Price"].idxmin()]

print("Title:", cheapest_book["Title"])
print("Price:", cheapest_book["Price"])


# Question 2
print("\n2. What is the most expensive book?")

most_expensive_book = df.loc[df["Price"].idxmax()]

print("Title:", most_expensive_book["Title"])
print("Price:", most_expensive_book["Price"])


# Question 3
print("\n3. Which rating is most common?")

most_common_rating = df["Rating"].mode()[0]

print("Most common rating:", most_common_rating)


# Question 4
print("\n4. How many books have each rating?")

rating_counts = df["Rating"].value_counts().sort_index()

print(rating_counts)


# Question 5
print("\n5. What percentage of books are in stock?")

in_stock = (
    df["Availability"]
    .str.contains("In stock", case=False)
    .sum()
)

total_books = len(df)

percentage = (in_stock / total_books) * 100

print(
    f"Books in stock: {in_stock}/{total_books}"
)

print(
    f"Percentage in stock: {percentage:.2f}%"
)
# --------------------------------------------------
# Books Above Average Price
# --------------------------------------------------

average_price = df["Price"].mean()

expensive_books = df[
    df["Price"] > average_price
]

print("\n" + "=" * 50)
print("BOOKS ABOVE AVERAGE PRICE")
print("=" * 50)

print(
    "Number of books above average price:",
    len(expensive_books)
)

print("\nTop 10 expensive books:")

print(
    expensive_books[
        ["Title", "Price", "Rating"]
    ]
    .sort_values(
        by="Price",
        ascending=False
    )
    .head(10)
)
# --------------------------------------------------
# Outlier Detection using IQR
# --------------------------------------------------

print("\n" + "=" * 50)
print("OUTLIER DETECTION")
print("=" * 50)

Q1 = df["Price"].quantile(0.25)
Q3 = df["Price"].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = df[
    (df["Price"] < lower_limit) |
    (df["Price"] > upper_limit)
]

print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)

print("\nLower limit:", lower_limit)
print("Upper limit:", upper_limit)

print("\nNumber of price outliers:", len(outliers))

print("\nOutlier books:")

print(
    outliers[
        ["Title", "Price", "Rating"]
    ].sort_values(
        by="Price",
        ascending=False
    )
)
# --------------------------------------------------
# Correlation Analysis
# --------------------------------------------------

print("\n" + "=" * 50)
print("CORRELATION ANALYSIS")
print("=" * 50)

correlation = df["Price"].corr(df["Rating"])

print(
    "Correlation between Price and Rating:",
    round(correlation, 3)
)
if abs(correlation) < 0.1:
    print("There is almost no relationship between price and rating.")
elif correlation > 0:
    print("There is a positive relationship between price and rating.")
else:
    print("There is a negative relationship between price and rating.")
# --------------------------------------------------
# Final EDA Insights
# --------------------------------------------------

print("\n" + "=" * 50)
print("FINAL EDA INSIGHTS")
print("=" * 50)

print("""
1. The dataset contains information about books including
   title, price, rating, availability, and book URL.

2. The dataset was checked for missing values and duplicate
   records.

3. Book prices vary considerably across the dataset.

4. The rating distribution shows that books are available
   across different rating levels from 1 to 5.

5. Some books have prices significantly higher than the
   average price and can be considered price outliers.

6. The correlation between price and rating is 0.028,
   which indicates almost no linear relationship between
   book price and rating.

7. Therefore, a higher-priced book does not necessarily
   have a higher rating in this dataset.
""")

print("=" * 50)
print("EDA ANALYSIS COMPLETED SUCCESSFULLY!")
print("=" * 50)