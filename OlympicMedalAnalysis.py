# Olympic Medal Analysis (1896 - 2024)


import pandas as pd
import matplotlib.pyplot as plt
import zipfile

# Load Data from ZIP 
zip_path = "Project 1/archive.zip"  

with zipfile.ZipFile(zip_path) as z:
    with z.open("athlete_events.csv") as f:
        athletes = pd.read_csv(f)
    with z.open("noc_regions.csv") as f:
        regions = pd.read_csv(f)

# Step 2: Merge Data
df = athletes.merge(regions, how="left", on="NOC")

# Filter medals only
medals_df = df.dropna(subset=["Medal"])

# Step 3: Top 10 Countries by Total Medals 
total_medals = medals_df.groupby("region")["Medal"].count().sort_values(ascending=False)

print("🏅 Top 10 Countries by Total Medals:")
print(total_medals.head(10))

plt.figure(figsize=(10,6))
total_medals.head(10).plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("Top 10 Countries by Olympic Medals (1896–2024)", fontsize=14)
plt.xlabel("Country")
plt.ylabel("Total Medals")
plt.xticks(rotation=45)
plt.show()

#  Step 4: Gold/Silver/Bronze Distribution for Top 5 
top5 = total_medals.head(5).index
medal_distribution = medals_df[medals_df["region"].isin(top5)]
medal_counts = medal_distribution.groupby(["region", "Medal"]).size().unstack(fill_value=0)

medal_counts.plot(kind="bar", stacked=True, figsize=(10,6), 
                  color=["gold", "silver", "brown"], edgecolor="black")
plt.title("Gold/Silver/Bronze Distribution (Top 5 Countries)", fontsize=14)
plt.xlabel("Country")
plt.ylabel("Number of Medals")
plt.xticks(rotation=45)
plt.show()

# Step 5: Overall Medal Trend Over Time 
yearly_medals = medals_df.groupby("Year")["Medal"].count()

plt.figure(figsize=(12,6))
plt.plot(yearly_medals.index, yearly_medals.values, marker="o", linestyle="-", color="blue")
plt.title("Total Olympic Medals Over Time (1896–2024)", fontsize=14)
plt.xlabel("Year")
plt.ylabel("Number of Medals Awarded")
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()

#  Step 6: Medal Trend for Specific Country
country = "India"   
country_trend = medals_df[medals_df["region"] == country].groupby("Year")["Medal"].count()

plt.figure(figsize=(10,6))
plt.plot(country_trend.index, country_trend.values, marker="o", color="green")
plt.title(f"{country} Olympic Medal Trend (1896–2024)", fontsize=14)
plt.xlabel("Year")
plt.ylabel("Number of Medals")
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()
