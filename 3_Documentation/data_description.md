# 🧼 Home Services Business Dataset (Synthetic)

Two-year dataset modeled after a real home services business. Tracks pricing, costs, payments, and geography across thousands of jobs. Built to support operational and financial analysis like margin optimization, workload balancing, and revenue risk assessment.

---

## 📄 jobs_v9.csv

Each row = one completed job, with total costs and metadata.

| Column               | Description                                                              |
|----------------------|--------------------------------------------------------------------------|
| `job_id`             | Unique identifier for each job                                           |
| `job_date`           | Service date (weekdays only, holidays excluded)                          |
| `client_id`          | Foreign key to `clients_v9.csv`                                          |
| `zip_code`           | Location of service                                                      |
| `crew_id`            | Assigned crew (1–4, max 3 jobs/day per crew)                             |
| `job_status`         | Always 'Completed' (placeholder for future status logic)                 |
| `total_price`        | Combined quoted value of all services in this job                        |
| `material_cost`      | Aggregated material costs                                                |
| `labor_cost`         | Aggregated labor costs                                                   |
| `travel_cost`        | Aggregated travel costs                                                  |
| `profit`             | Total price minus costs                                                  |
| `payment_status`     | Paid / Paid Late / Unpaid                                                |
| `payment_delay_days` | Days late if applicable (capped at year-end)                             |
| `num_services`       | Number of services included in this job                                  |

---

## 📄 services_v9.csv

Each row = one service performed within a job.

| Column           | Description                                               |
|------------------|-----------------------------------------------------------|
| `job_id`         | Foreign key to `jobs_v9.csv`                              |
| `service_type`   | One of 7 core offerings (e.g., Roof Cleaning, House Wash) |
| `price`          | Quoted price for this individual service                  |
| `material_cost`  | Estimated based on service-specific rules                 |
| `labor_cost`     | Randomized between $50–$200                               |
| `travel_cost`    | Randomized between $10–$30                                |
| `service_profit` | Net profit per service                                    |

- ⚠️ *Note: A few jobs contain duplicate rows for the same service type due to the randomization process. This can slightly increase record counts at the service level, but all job-level financials and reconciliations remain correct.*

---

## 📄 clients_v9.csv

Client-level lookup table including ZIP and income segmentation.

| Column         | Description                                         |
|----------------|-----------------------------------------------------|
| `client_id`    | Unique identifier                                   |
| `zip_code`     | Client location                                     |
| `region_name`  | Neighborhood or marketing region                    |
| `tier`         | ZIP income tier (Standard / Mid / High)             |

---

## 📄 zip_regions_v9.csv

Lookup for ZIP → Region → Tier mapping used in geographic analysis.

| Column        | Description                                              |
|----------------|----------------------------------------------------------|
| `zip_code`     | ZIP code in Central Florida                              |
| `region_name`  | Region or neighborhood label used in maps and charts     |
| `tier`         | Income tier: Standard / Mid / High, based on relative census estimates |

---

## 🧪 Generation Logic Summary (v9)

- **Date range**: Jan 1, 2023 – Dec 31, 2024  
- **Weekdays only**: Includes Saturdays, excludes Sundays  
- **Holidays excluded**: New Year's, July 4, Thanksgiving, Christmas  
- **Job volume**: Poisson-distributed (~5 jobs/day average)  
- **Crew logic**: Max 3 jobs per day per crew  
- **Services**: 7 types, assigned via weighted probability  
- **Payment behavior**: 85% Paid, 12% Paid Late, 3% Unpaid  
- **Repeat clients**: ~30% likelihood modeled per job  
- **Profit model**: Line-item costs (materials, labor, travel) at service level

---

## ✅ Suggested Use Cases

- Analyze profit by service and client tier  
- Monitor crew load and underutilization  
- Explore geographic expansion based on ZIP performance  
- Quantify revenue risk from unpaid or delayed jobs

---

## ⚠️ Known Constraints

- No cancellations or reschedules in this version  
- All jobs marked as “Completed” (status logic placeholder)  
- Uniform pricing across ZIPs (no income-tier-based uplift yet)  
- No line-item `service_id` included  
- Some duplicated service rows per job (documented in cleaning summary)

---

## 📎 Notes

- All data fully simulated in Python  
- 3,000+ jobs across two years, 40+ ZIPs  
- Nulls added intentionally to mimic messy real-world data  
- Revenue = quoted value unless explicitly filtered to "Realized"