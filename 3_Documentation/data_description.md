## 📘 Dataset Overview: Synthetic Home Services Data

This document outlines the structure, logic, and intent of the generated dataset used in the home services business simulation project.

---

### 🗂️ Output Files

| File              | Description                                                                    | Approx. Rows |
|-------------------|--------------------------------------------------------------------------------|--------------|
| `jobs.csv`        | One row per completed, cancelled, or rescheduled job                          | ~3,100       |
| `services.csv`    | One row per service line item within each job (e.g., roof, pavers)            | ~5,400       |
| `clients.csv`     | Client ID, ZIP, region name, and tier (used to simulate regional targeting)   | ~2,300       |
| `zip_regions.csv` | Reference table for ZIP codes, region names, and tier classification          | ~40          |

---

### 📄 jobs.csv

| Column               | Description                                                                 |
|----------------------|-----------------------------------------------------------------------------|
| `job_id`             | Unique identifier per job                                                   |
| `job_date`           | Scheduled date (excludes Sundays and major holidays)                        |
| `client_id`          | Foreign key linking to `clients.csv`                                       |
| `zip_code`           | ZIP code of job location                                                    |
| `crew_id`            | Crew assigned (nulls in ~3% of jobs for realism)                        |
| `job_status`         | Completed / Cancelled / Rescheduled (88% / 8% / 4%)                         |
| `total_price`        | Quoted price for all services (whole dollars, tier-adjusted)                |
| `material_cost`      | Sum of materials across all services (nulls in ~5% of jobs)              |
| `labor_cost`         | Sum of labor costs (nulls in ~3%)                                       |
| `travel_cost`        | Fixed travel cost per job (nulls in ~3%)                                |
| `profit`             | `total_price - material - labor - travel`, using safe fallback if null      |
| `payment_status`     | Paid / Paid Late / Unpaid (80% / 15% / 5%)                                  |
| `payment_delay_days` | Days late, if applicable (nulls in ~5% of Paid jobs)                     |
| `num_services`       | Number of services performed within the job                                |

---

### 📄 services.csv

| Column          | Description                                                   |
|------------------|---------------------------------------------------------------|
| `job_id`         | Foreign key linking to `jobs.csv`                            |
| `service_type`   | Type of service (e.g., Roof Cleaning, Paver Sealing)         |
| `price`          | Price quoted for that individual service                     |
| `material_cost`  | Cost of materials for the service (nulls for small jobs)  |
| `labor_cost`     | Labor cost (nulls in ~3%)                                 |
| `travel_cost`    | Travel cost contribution (nulls in ~3%)                  |
| `service_profit` | Profit for each service based on service price - expenses   |
| `service_id`     | Unique ID composed of job ID and service type abbreviation   |

---

### 📄 clients.csv

| Column          | Description                                      |
|------------------|--------------------------------------------------|
| `client_id`      | Unique identifier per client                    |
| `zip_code`       | ZIP where the client resides                    |
| `region_name`    | Neighborhood or city (e.g., Lake Nona, Oviedo)  |
| `region_tier`    | High / Mid / Standard - pricing varies by tier  |

---

### 📄 zip_regions.csv

| Column        | Description                                 |
|----------------|---------------------------------------------|
| `zip_code`     | ZIP code in service area                   |
| `region_name`  | Common name for the ZIP (e.g. Windermere)  |
| `tier`         | Market segment: High / Mid / Standard      |

---

### ⚙️ Data Generation Summary

- Jobs generated between Jan 1, 2023 and Dec 31, 2024  
- Sundays and major US holidays excluded from job scheduling (to reflect typical residential service schedules)  
- Job volume simulated daily using a Poisson distribution  
- Each job assigned 1-4 services, priced by type and ZIP-tier multiplier:  
  - High ZIPs: +15% price  
  - Mid ZIPs: +5% price  
  - These increases simulate larger properties and higher service demands in premium neighborhoods  
- Service pricing ranges:  
  - Paver Sealing: $800-$3000  
  - Roof Cleaning: $300-$1500  
  - Others: $100-$800  
- Profit calculated per job using internal cost breakdowns  
- Nulls injected for realism:  
  - ~3-5% missing `crew_id`, `payment_delay_days`, `labor_cost`, `travel_cost`, `material_cost`  


---

### 🎯 Why This Matters
This dataset is engineered to support operational and financial analysis across:
- Regional pricing and performance
- Crew workload and capacity
- Service-level profitability
- Payment behavior and financial health

Perfect for simulation of real-world dashboards and scenario modeling.
