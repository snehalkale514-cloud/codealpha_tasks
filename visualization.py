import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# CodeAlpha Internship - Task 3: Data Visualization
# ============================================================

# Load dataset
df = pd.read_csv("books_dataset.csv")

print("Dataset loaded successfully!")
print("Number of rows:", len(df))
print("Number of columns:", len(df.columns))


# ============================================================
# Basic Information
# ============================================================

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 rows:")
print(df.head())


# ============================================================
# 1. Book Price Distribution
# ============================================================

plt.figure(figsize=(10, 6))

plt.hist(
    df["Price"],
    bins=20,
    edgecolor="black"
)

plt.title("Distribution of Book Prices")
plt.xlabel("Price (£)")
plt.ylabel("Number of Books")

plt.tight_layout()

plt.savefig(
    "price_distribution.png",
    dpi=300
)

plt.show()


# ============================================================
# 2. Book Rating Distribution
# ============================================================

rating_counts = df["Rating"].value_counts().sort_index()

plt.figure(figsize=(8, 5))

plt.bar(
    rating_counts.index,
    rating_counts.values,
    edgecolor="black"
)

plt.title("Distribution of Book Ratings")
plt.xlabel("Rating")
plt.ylabel("Number of Books")

plt.xticks([1, 2, 3, 4, 5])

plt.tight_layout()

plt.savefig(
    "rating_distribution.png",
    dpi=300
)

plt.show()


# ============================================================
# 3. Price vs Rating
# ============================================================

plt.figure(figsize=(10, 6))

plt.scatter(
    df["Rating"],
    df["Price"],
    alpha=0.6
)

plt.title("Book Price vs Rating")
plt.xlabel("Rating")
plt.ylabel("Price (£)")

plt.xticks([1, 2, 3, 4, 5])

plt.tight_layout()

plt.savefig(
    "price_vs_rating.png",
    dpi=300
)

plt.show()


# ============================================================
# 4. Top 10 Most Expensive Books
# ============================================================

top_10_expensive = df.nlargest(10, "Price")

plt.figure(figsize=(12, 7))

plt.barh(
    top_10_expensive["Title"],
    top_10_expensive["Price"],
    edgecolor="black"
)

plt.title("Top 10 Most Expensive Books")
plt.xlabel("Price (£)")
plt.ylabel("Book Title")

plt.gca().invert_yaxis()

plt.tight_layout()

plt.savefig(
    "top_10_expensive_books.png",
    dpi=300
)

plt.show()


# ============================================================
# Task Completed
# ============================================================

print("\n" + "=" * 50)
print("DATA VISUALIZATION COMPLETED SUCCESSFULLY!")
print("=" * 50)