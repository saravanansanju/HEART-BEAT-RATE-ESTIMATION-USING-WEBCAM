# LEVEL 1 DATA ANALYSIS

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Dataset.csv")

# -----------------------------
# Task 1: Top Cuisines
# -----------------------------
cuisines = df['Cuisines'].str.split(', ').explode()
top_cuisines = cuisines.value_counts().head(3)
percentages = (top_cuisines / len(df) * 100).round(2)

print("Top 3 Cuisines (% of restaurants):")
print(percentages)

# -----------------------------
# Task 2: City Analysis
# -----------------------------
city_counts = df['City'].value_counts()
highest_city = city_counts.index[0]

print("\nCity with most restaurants:")
print(f"{highest_city} ({city_counts.iloc[0]} restaurants)")

city_avg_rating = df.groupby('City')['Aggregate rating'].mean().round(2)

print("\nAverage rating by city:")
print(city_avg_rating)

highest_rated_city = city_avg_rating.idxmax()
print(f"\nCity with highest average rating: {highest_rated_city}")

# -----------------------------
# Task 3: Price Range Distribution
# -----------------------------
price_counts = df['Price range'].value_counts().sort_index()

plt.bar(price_counts.index, price_counts.values)
plt.xlabel('Price Range')
plt.ylabel('Number of Restaurants')
plt.title('Price Range Distribution')
plt.show()

# -----------------------------
# Task 4: Online Delivery
# -----------------------------
delivery_percentage = (df['Has Online delivery'] == 'Yes').mean() * 100
print(f"\nPercentage with online delivery: {delivery_percentage:.2f}%")

delivery_ratings = df.groupby('Has Online delivery')['Aggregate rating'].mean()
print("\nAverage ratings by online delivery:")
print(delivery_ratings)