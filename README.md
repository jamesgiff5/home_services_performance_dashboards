# 💧 Home Services Performance Project

A data-driven look at how a service business runs at scale: profitability, scheduling, and operations, modeled from experience.


## 🧭 Project Context

Before transitioning into data analytics, I ran an exterior cleaning business in Central Florida. This project builds on that experience by simulating the kinds of operational and financial questions I faced as an owner, reimagined at the scale of a growing team.

The dashboards and dataset reflect real-world service patterns: seasonal demand, bundling strategy, workload constraints, and customer retention. I built the data from scratch to support decisions that would matter in a real business, like profitability, capacity, and performance over time.

I built a realistic financial and operational dashboard to support smarter decisions around pricing, capacity, and performance.

## Exec Summary
All revenue and profit figures are based on quoted job values, not actual payments collected. This better reflects pricing strategy, not cash flow accounting.

## 📊 Dashboards

| Name         | Description                                     | Link |
|--------------|-------------------------------------------------|------|
| Financial    | Revenue, cost, profit, payment behavior         | [View →](./Financial_Dashboard) |
| Operational  | Crew capacity, job volume, service mix by day   | [View →](./Operational_Dashboard) |

---

## 📁 Data & Generation Logic

- 📘 [Dataset Overview](./data/data_description.md)  
  Covers what each CSV contains and how it was generated

- 🧼 [Data Cleaning Summary](./data/data_cleaning_log.md)  
  Step-by-step of what was transformed in Power Query (v10)

- 🛠️ [Data Generation Script](./data/generate_dataset_v9.py)  
  Python script that produced the base synthetic data

---

## 🏗️ How the Data Was Modeled

This project simulates realistic operations and finance flows for a home services business. Core logic was built in Python, with additional reshaping in Power Query. Imperfections (like payment delays and partial cost data) were added intentionally to reflect messy real-world conditions.
- Costs were modeled using realistic estimates based on my prior field experience.
- Some cost assumptions (e.g., crew travel) were simplified to prioritize analytical clarity.
- The dataset reflects job quotes, not accounting ledgers—this aligns with how service businesses forecast ops performance, not just bookkeep.

---



### ⚠️ Known Limitation (Simulated Data Behavior)

In this simulated dataset, some jobs contain multiple instances of the same service type under a single job_id (e.g., two or three “Paver Sealing” entries). This inflates service-level totals when summed and creates a mismatch between:
- Job-level KPIs (like total revenue/profit, which use unique job_ids)
- Service-level visualizations (which can overstate totals due to duplication)

This issue stems from the data generation logic and wouldn’t typically occur in real operational systems, where service entries are cleaner and linked by line-item IDs or timestamps.

*Rather than re-engineering the dataset at this stage, I preserved the structure and clearly documented the behavior. This mirrors the kind of integrity note you’d find in internal dashboards handling imperfect data sources.*

---
## 📌 Notes on Versioning

- `generate_dataset_v9.py` produces the base synthetic data as CSVs
- `home_services_data_v10.xlsx` contains Power Query transformations for analysis and Tableau
- Tableau dashboards are directly connected to `v10.xlsx` and will break if the file is renamed or moved
- Earlier versions were iterated to improve operational realism and financial modeling