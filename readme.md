# 🏅 Olympic Medal Analysis (1896 - 2024)

This project analyzes Olympic Games data from **1896 to 2024** using Python.  
It provides insights into **top medal-winning countries**, **medal distribution (Gold/Silver/Bronze)**, and **trends in medals over time**.  

---

## 📌 Project Overview
The goal of this project is to:
1. Load Olympic data (`athlete_events.csv` and `noc_regions.csv`) directly from a ZIP file.  
2. Merge athlete data with country information.  
3. Analyze medal counts and trends.  
4. Visualize results using **Matplotlib**.

---

## 📂 Dataset
The dataset contains:
- `athlete_events.csv` → Olympic athletes, events, and medals (1896–2016 + extended till 2024).  
- `noc_regions.csv` → Mapping of National Olympic Committee (NOC) codes to regions (countries).  

Source: [Kaggle - 120 Years of Olympic History Dataset](https://www.kaggle.com/heesoo37/120-years-of-olympic-history-athletes-and-results)

---

## 🛠️ Technologies Used
- **Python 3.12+**
- **pandas** (Data analysis)  
- **matplotlib** (Data visualization)  
- **zipfile** (To read multiple CSVs from ZIP file)  

---

## 📊 Analysis Performed
1. **Top 10 Countries by Total Medals**  
   - Shows overall Olympic dominance.  

2. **Gold/Silver/Bronze Distribution (Top 5 Countries)**  
   - Stacked bar chart to compare medal types.  

3. **Overall Medal Trend Over Time (1896–2024)**  
   - Line chart showing how total medals have grown with Olympics expansion.  

4. **Country-Specific Medal Trend (Example: India)**  
   - Line chart for a single country’s performance.  

---

## ▶️ How to Run

1. Clone this repository or download the project.  
2. Place the dataset `archive.zip` in the `Project 1/` folder.  
3. Install dependencies:  
   ```bash
   pip install pandas matplotlib
