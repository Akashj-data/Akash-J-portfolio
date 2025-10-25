# 🍿 Netflix Data Analysis using SQL

## Overview
This project focuses on analyzing Netflix’s global content library using SQL to uncover business insights such as top countries, genres, most common ratings, and viewing trends.  
It includes 15 practical business problems solved using PostgreSQL queries.

---

## Files Included
```
Netflix-Data-Analysis/
├── README.md
├── Technical_Approach.pdf
├── sql/
│   ├── Schemas.sql
│   ├── Business_Problems_Netflix.sql
│   ├── Solutions_of_15_Business_Problems.sql
├── data/
│   └── netflix_titles.csv
└── assets/
```
---

## SQL Environment Setup
1. Open PostgreSQL or MySQL Workbench.
2. Execute `Schemas.sql` to create the `netflix` table.
3. Import `netflix_titles.csv` into the table.
4. Run `Solutions_of_15_Business_Problems.sql` for detailed analysis.

---

## Business Problems Covered
- Content type distribution (Movies vs TV Shows)
- Most common ratings
- Longest movie
- Top producing countries
- Yearly content trends by country
- Genre-based content count
- Keyword-based classification (Good vs Bad content)

---

## Dataset
- **File:** `netflix_titles.csv`
- **Source:** Kaggle – Netflix Movies and TV Shows dataset
- **Columns:** show_id, type, title, director, cast, country, date_added, release_year, rating, duration, listed_in, description

---

## Outcome
This project demonstrates how SQL can be used to generate valuable data-driven insights for business intelligence and content strategy decisions at Netflix.