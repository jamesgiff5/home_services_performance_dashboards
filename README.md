# 💧 Home Services Performance Project

A data-driven look at how a service business runs at scale: profitability, scheduling, and operations, modeled from experience.


## 🧭 Project Context

Before transitioning into data analytics, I ran an exterior cleaning business in Central Florida. This project builds on that experience by simulating the kinds of operational and financial questions I faced as an owner, reimagined at the scale of a growing team.

The dashboards and dataset reflect real-world service patterns: seasonal demand, bundling strategy, workload constraints, and customer retention. I built the data from scratch to support decisions that would matter in a real business, like profitability, capacity, and performance over time.

The result is a realistic operations model built to surface insights, not just trends.


## 📊 Dashboards

| Name         | Description                                     | Link |
|--------------|-------------------------------------------------|------|
| Financial    | Revenue, cost, profit, payment behavior         | [View →](./dashboards/financial_dashboard/README.md) |
| Operational  | Crew capacity, job volume, service mix by day   | [View →](./dashboards/operational_dashboard/README.md) |

---

## 📁 Data & Generation Logic

- 📘 [Dataset Overview](./data/data_description.md)  
  Covers what each CSV contains and how it was generated

- 🧼 [Data Cleaning Summary](./data/data_cleaning_log.md)  
  Step-by-step of what was transformed in Power Query (v10)

- 🛠️ [Data Generation Script](./data/generate_dataset_v9.py)  
  Python script that produced the base synthetic data

---

## 📌 Notes on Versioning

- `generate_dataset_v9.py` produces the base synthetic data as CSVs
- `home_services_data_v10.xlsx` contains Power Query transformations for analysis and Tableau
- Tableau dashboards are directly connected to `v10.xlsx` and will break if the file is renamed or moved
- Earlier versions were iterated to improve operational realism and financial modeling
