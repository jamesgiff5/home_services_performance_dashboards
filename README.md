# 💧 Home Services Performance Project

A data-driven look at how a service business runs at scale, from pricing and profitability to scheduling and repeat clients. Modeled from real-world experience running field ops.

---

## 🧭 Project Context

Before transitioning into data analytics, I ran an exterior cleaning business in Central Florida. This project builds on that experience by simulating the financial and operational questions I dealt with daily.

The dataset and dashboards reflect real service patterns: seasonal demand, bundling behavior, crew capacity, and client retention. I generated the data from scratch, then scaled it up to simulate a multi-crew operation. Every element was designed to answer decisions that matter, like where margin comes from, when teams are underused, and how repeat work flows back in.

All financials are based on quoted job values (not collected payments), which better reflects pricing strategy than cash-based accounting.

---

## 📊 Dashboards

| Name         | Focus       | Link |
|--------------|-------------|------|
| Financial    | Revenue, profit, costs, late payment behavior     | [View →](./Financial_Dashboard) |
| Operational  | Crew capacity, service mix, repeat client patterns | [View →](./Operational_Dashboard) |

---

## 📁 Data & Generation Logic

- 📘 [Dataset Overview](./data/data_description.md)  
  Overview of the data tables and structure  

- 🧼 [Data Cleaning Log](./data/data_cleaning_log.md)  
  Step-by-step record of Power Query transformations  

- 🛠️ [Data Generation Script](./data/generate_dataset_v9.py)  
  Python script that creates the raw synthetic data  

---

## 🏗️ How the Data Was Modeled

This project simulates a functioning service business with realistic operational and financial logic. The dataset was generated in Python, then reshaped in Power Query to match how real-world teams analyze job-level performance.

Key modeling choices:
- Direct costs (materials, labor, travel) were estimated from past field experience
- Overhead costs (equipment, admin, marketing) were excluded to isolate per-job margins
- Imperfections like payment delays, partial cost tracking, and over-100% margins were kept to reflect common reporting challenges in real operations
- Metrics are based on job quotes, not cash collections, to match how most service teams forecast and manage performance

---

## ⚠️ Note on Duplicate Service Entries

Some jobs in the dataset include multiple instances of the same service under a single `job_id` (e.g., two rows labeled “Paver Sealing”). This slightly inflates service-level totals when summed and creates a mismatch between:

- Job-level metrics (based on unique `job_id`s)
- Service-level charts (which sum all rows, including duplicates)

This mirrors real-world issues you’d find in CRM exports or line-item billing reports. Rather than rebuild the structure, I flagged it clearly in the dashboards, just like you would in production.

---

## 📌 Versioning Notes

- `generate_dataset_v9.py` creates the raw synthetic data
- `home_services_data_v10.xlsx` holds the cleaned data via Power Query, used by Tableau
- Dashboards connect directly to `v10.xlsx` and will break if renamed or moved
- Earlier versions were iterated to improve operational realism and profit logic. Some imperfections remain, but the focus was on building a useful dataset for analysis and dashboard design, not simulating a perfect accounting system.