import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("Corrected_Data.csv")

# Filter for a specific year, e.g., 2020
year = 2020
filtered_df = df[df["Year"] == year]

# Sort and select top 10 countries by population
top_countries = filtered_df.sort_values(by="Value", ascending=False).head(10)

# Bar chart
plt.figure(figsize=(12, 6))
plt.bar(top_countries["Country Name"], top_countries["Value"], color='skyblue', edgecolor='black')
plt.title(f"Top 10 Countries by Population in {year}")
plt.xlabel("Country")
plt.ylabel("Population")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.grid(axis='y')

# Save chart
plt.savefig("top10_population_bar_chart.png")
plt.show()
