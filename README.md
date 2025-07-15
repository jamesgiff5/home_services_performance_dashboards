# 💧 Home Services Performance Dashboards (Data Project)

A data-driven look at how a service business runs at scale, from pricing and profitability to scheduling and repeat clients. Modeled from real-world field ops experience.

---

## 🧭 Project Context

Before transitioning into data analytics, I ran an exterior cleaning business in Central Florida. This project builds on that experience by simulating the financial and operational questions I dealt with firsthand.

🧾 [How real-world field experience shaped this dataset →](3_Documentation/real_world_background.md)

The dataset and dashboards reflect real service patterns: seasonal demand, bundling behavior, crew capacity, and client retention. I generated the data from scratch, then scaled it to simulate a multi-crew operation. Every element supports practical decisions, like where margin comes from, when teams are underused, and how repeat work flows back in.

All financials are based on quoted job values (not collected payments), which better reflects pricing strategy than cash-based accounting.

---

## 📊 Dashboards

| Name         | Focus       | Link |
|--------------|-------------|------|
| **Financial**    | Revenue, profit, costs, late payment behavior     | [**View →**](./Financial_Dashboard) |
| **Operational**  | Crew capacity, service mix, repeat client patterns | [**View →**](./Operational_Dashboard) |

---

## 📁 Data & Generation Logic

- 📘 [Dataset Overview](./data/data_description.md)  
  Describes the structure and fields in each CSV

- 🧼 [Data Cleaning Summary](./data/data_cleaning_summary.md)  
  Outlines Power Query transformations and fixes

- 🛠️ [Data Generation Script](./data/generate_dataset_v9.py)  
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

## ⚠️ Known Quirk: Service Duplication
Some jobs include multiple instances of the same service under a single `job_id` (for example, two rows labeled “Paver Sealing”). This slightly inflates service-level totals when summed and creates a mismatch between:

- Job-level metrics (based on unique `job_id`s)
- Service-level charts (which sum all rows, including duplicates)

This mirrors the kind of structure you'd see in CRM exports or billing systems. Instead of rebuilding the logic, I flagged the issue clearly in the dashboards to reflect real-world analyst tradeoffs.

---

## 📌 Versioning Notes

- `generate_dataset_v9.py` creates the raw synthetic data
- `home_services_data_v10.xlsx` holds the cleaned data via Power Query, used by Tableau
- Dashboards connect directly to `v10.xlsx` and will break if renamed or moved
- Earlier versions were iterated to improve operational realism and profit logic. Some imperfections remain, but the goal was to build a useful dataset for analysis and dashboarding, not simulate a perfect accounting system.