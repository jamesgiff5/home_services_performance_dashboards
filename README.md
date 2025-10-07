# 💧 Home Services Performance Dashboards

A data-driven look at how a service business runs at scale, from pricing and profitability to scheduling and repeat clients. Modeled from real-world field ops experience.  

![Dashboards Preview](4_Assets/Combined_Dashboards.png)
---

## 🧭 Project Context

Before transitioning into data analytics, I ran an exterior cleaning business in Central Florida. This project builds on that experience by simulating the financial and operational questions I dealt with firsthand.

🧾 [How real-world field experience shaped this dataset →](3_Documentation/real_world_background.md)

The dataset and dashboards reflect real service patterns: seasonal demand, bundling behavior, crew capacity, and client retention. I generated the data from scratch, then scaled it to simulate a multi-crew operation. Every element supports practical decisions, like where margin comes from, when teams are underused, and how repeat work flows back in.

All financials are based on quoted job values (not collected payments), which better reflects pricing strategy than cash-based accounting.

---

## 📊 Interactive Dashboards & Insights

| Name         | Focus       | Link |
|--------------|-------------|------|
| **Financial**    | Revenue, profit, costs, late payment behavior     | [**View Dashboard & Analysis →**](./Financial_Dashboard) |
| **Operational**  | Crew capacity, service mix, repeat client patterns | [**View Dashboard & Analysis →**](./Operational_Dashboard) |

---

## 📁 Data & Generation Logic

- 📘 [Dataset Overview](./3_Documentation/data_description.md)  
  Describes the structure and fields in each CSV

- 🧼 [Data Cleaning Summary](./3_Documentation/data_cleaning_summary.md)  
  Outlines Power Query transformations and fixes

- 🛠️ [Data Generation Script](./generate_dataset_v9.py)  
  Python logic that creates the raw synthetic data

---

## 🏗️ How the Data Was Modeled

This project simulates a functioning service business with realistic operational and financial logic. The dataset was generated in Python, then reshaped in Power Query to reflect how real teams analyze job-level performance.

Key modeling notes:
- Direct costs (materials, labor, travel) were estimated from past field experience
- Overhead costs (equipment, admin, marketing) were excluded to isolate per-job margins
- Imperfections like payment delays, partial cost data, and over-100% margins were kept to reflect common reporting issues in service operations
- Metrics are based on job quotes, not cash collections, to align with how service teams forecast performance

---

## ⚠️ Known Quirk: Duplicate Service Lines  

Some jobs include multiple rows of the **same service type** under a single `job_id` (for example, two instances of “Roof Cleaning”).  
This duplication wasn’t intentional, it likely appeared during the Python data generation process after several revisions to the randomization logic.  

However, the key financial fields (**price, material cost, labor cost, travel cost, and profit**) still **reconcile perfectly** between the job-level and service-level tables.  
In other words, while a few service names appear more than once per job, **the totals at both levels match exactly**, so the dataset remains accurate for analysis and visualization.  

This minor inconsistency was left in place to reflect the kinds of structural imperfections analysts often encounter in real operational data, without affecting the reliability of the metrics or insights displayed in the Tableau dashboards.  

---

## 📌 Versioning Notes

- `generate_dataset_v9.py` creates the raw synthetic data
- `home_services_data_v10.xlsx` holds the cleaned data via Power Query, used by Tableau
- Dashboards connect directly to `v10.xlsx` and will break if renamed or moved
- Earlier versions were iterated to improve operational realism and profit logic. Some imperfections remain, but the goal was to build a useful dataset for analysis and dashboarding, not simulate a perfect accounting system.
