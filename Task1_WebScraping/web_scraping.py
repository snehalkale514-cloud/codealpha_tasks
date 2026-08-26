import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from urllib.parse import urljoin


# ============================================================
# CodeAlpha Internship - Task 1: Web Scraping
# ============================================================

# Website URLs
base_url = "https://books.toscrape.com/"
page_url = "https://books.toscrape.com/catalogue/page-{}.html"


# Browser-like header
headers = {
    "User-Agent": "Mozilla/5.0"
}


# List to store all book information
books = []


# Convert rating words into numbers
rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}


print("Starting Web Scraping...")
print("-" * 50)


# ============================================================
# Scrape all 50 pages
# ============================================================

for page in range(1, 51):

    url = page_url.format(page)

    try:

        response = requests.get(
            url,
            headers=headers,
            timeout=10
        )

        response.raise_for_status()

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        # Find all books on the current page
        book_items = soup.select(
            "article.product_pod"
        )

        # Extract information from each book
        for book in book_items:

            # ------------------------------------------------
            # Book Title
            # ------------------------------------------------

            title = book.h3.a["title"]


            # ------------------------------------------------
            # Book Price
            # ------------------------------------------------

            price_text = book.select_one(
                ".price_color"
            ).text.strip()

            # Remove currency symbols and encoding character
            price_text = (
                price_text
                .replace("£", "")
                .replace("Â", "")
                .strip()
            )

            price = float(price_text)


            # ------------------------------------------------
            # Book Rating
            # ------------------------------------------------

            rating_name = book.select_one(
                "p.star-rating"
            )["class"][1]

            rating = rating_map[rating_name]


            # ------------------------------------------------
            # Availability
            # ------------------------------------------------

            availability = book.select_one(
                ".availability"
            ).get_text(strip=True)


            # ------------------------------------------------
            # Book URL
            # ------------------------------------------------

            relative_url = book.h3.a["href"]

            book_url = urljoin(
                url,
                relative_url
            )


            # ------------------------------------------------
            # Store book information
            # ------------------------------------------------

            books.append({
                "Title": title,
                "Price": price,
                "Rating": rating,
                "Availability": availability,
                "Book_URL": book_url
            })


        print(
            f"Page {page}/50 completed - "
            f"{len(books)} books collected"
        )


        # Small delay between requests
        time.sleep(0.5)


    except requests.exceptions.RequestException as error:

        print(
            f"Error while scraping page {page}: {error}"
        )


# ============================================================
# Create DataFrame
# ============================================================

df = pd.DataFrame(books)


# ============================================================
# Clean the dataset
# ============================================================

# Remove duplicate rows
df = df.drop_duplicates()


# Remove rows with missing important information
df = df.dropna(
    subset=[
        "Title",
        "Price",
        "Rating"
    ]
)


# Reset index
df = df.reset_index(drop=True)


# ============================================================
# Save dataset
# ============================================================

df.to_csv(
    "books_dataset.csv",
    index=False
)


# ============================================================
# Display Results
# ============================================================

print("\n" + "=" * 60)
print("WEB SCRAPING COMPLETED")
print("=" * 60)


print(
    "\nTotal books collected:",
    len(df)
)


print(
    "\nDataset shape:",
    df.shape
)


print("\nFirst 5 rows:")
print(df.head())


# ============================================================
# Missing Values
# ============================================================

print("\nMissing values:")
print(df.isnull().sum())


# ============================================================
# Duplicate Records
# ============================================================

print(
    "\nDuplicate rows:",
    df.duplicated().sum()
)


# ============================================================
# Dataset Statistics
# ============================================================

print("\nPrice statistics:")
print(df["Price"].describe())


print("\nRating distribution:")
print(
    df["Rating"]
    .value_counts()
    .sort_index()
)


print("\nAvailability:")
print(
    df["Availability"]
    .value_counts()
)


# ============================================================
# Final Message
# ============================================================

print("\n" + "=" * 60)
print("Dataset successfully saved as books_dataset.csv")
print("Task 1 Web Scraping completed successfully! 🎉")
print("=" * 60)