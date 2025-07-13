# 🧼 Home Services Business Dataset (Synthetic)

This dataset simulates a real-world operational environment for a residential home services company based in Central Florida. It includes job records, service-level financials, client geography, and payment behavior—designed for realistic analysis, not just technical demos.

## 📄 jobs_v9.csv

Each row represents a completed job, with aggregated costs and metadata.

| Column               | Description                                                              |
|----------------------|--------------------------------------------------------------------------|
| `job_id`             | Unique ID for the job                                                    |
| `job_date`           | Service date (weekdays only, holidays excluded)                          |
| `client_id`          | FK to clients_v9.csv                                                     |
| `zip_code`           | ZIP where job was performed                                              |
| `crew_id`            | Crew assigned (1–4, max 3 jobs per day per crew)                         |
| `job_status`         | Always 'Completed' (placeholder for future status expansion)             |
| `total_price`        | Sum of all service prices for this job                                   |
| `material_cost`      | Combined material costs                                                  |
| `labor_cost`         | Combined labor costs                                                     |
| `travel_cost`        | Combined travel costs                                                    |
| `profit`             | Net profit (total - costs)                                               |
| `payment_status`     | Paid / Paid Late / Unpaid                                                |
| `payment_delay_days` | Days late, if applicable (max capped to year-end)                        |
| `num_services`       | Number of services performed in this job                                 |

---

## 📄 services_v9.csv

Each row represents an individual service within a job.

| Column           | Description                                               |
|------------------|-----------------------------------------------------------|
| `job_id`         | FK to jobs_v9.csv                                         |
| `service_type`   | One of 7 types (e.g., Roof Cleaning, Window Cleaning)     |
| `price`          | Quoted price for the service                              |
| `material_cost`  | Materials used (calculated via service-specific % rules)  |
| `labor_cost`     | Random labor cost ($50–$200)                              |
| `travel_cost`    | Random travel cost ($10–$30)                              |
| `service_profit` | Net profit per service                                    |

---

## 📄 clients_v9.csv

Client-level lookup table including geographic targeting dimensions.

| Column         | Description                              |
|----------------|------------------------------------------|
| `client_id`    | Unique client ID                         |
| `zip_code`     | Where client is located                  |
| `region_name`  | Mapped region name (e.g., Lake Nona)     |
| `tier`         | Market tier: High / Mid / Standard       |

---

## 📄 zip_regions_v9.csv

Reference table used for ZIP → Region → Tier lookup.

| Column        | Description                                |
|----------------|--------------------------------------------|
| `zip_code`     | ZIP code in Central Florida                |
| `region_name`  | Region or neighborhood (marketing label)   |
| `tier`         | Customer segment: High / Mid / Standard    |

---

## 🧪 Generation Logic Summary (v9)

- **Date range**: Jan 1, 2023 – Dec 31, 2024  
- **Weekdays only**: Saturdays included, Sundays excluded  
- **US Holidays excluded**: New Year's, July 4th, Thanksgiving, Christmas  
- **Job volume**: Poisson-distributed (avg ~5 jobs/day)  
- **Crew capacity**: Max 3 jobs per crew per day  
- **Service types**: 7 categories with weighted probabilities  
- **Payment status**: 85% Paid, 12% Paid Late, 3% Unpaid  
- **Repeat clients**: ~30% chance per job  
- **Profit logic**: Explicit material, labor, and travel costs per service

---

## ✅ Suggested Use Cases

- Pricing & margin optimization  
- Crew workload & ops planning  
- Late payment modeling  
- Regional strategy (by ZIP/region tier)

---

## ⚠️ Known Constraints

- No cancellations or reschedules (yet)
- All jobs are marked as “Completed”
- No price variation by region tier (no uplift logic implemented)
- No `service_id` generated in this version

---

## 📌 Version

**generate_dataset_v9.py**  
Last updated: July 2025  
Maintainer: [Your Name]
