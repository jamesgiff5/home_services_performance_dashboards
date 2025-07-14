## 🧼 Data Cleaning Summary
This file summarizes all field-level cleaning and structural fixes performed prior to Tableau analysis. Higher-level data modeling choices and assumptions (e.g., simulated payment behavior, synthetic profitability logic) are documented in the dashboard-specific README files.
#### `jobs.csv`
- Sorted by `job_date` to verify date consistency and check for gaps or outliers
- Scanned `crew_id` for missing values (~3%) and confirmed they were expected (simulated nulls)
- Reviewed `profit` values for nulls, negatives, and outliers — all aligned with input cost structure
- Validated `payment_status` logic: `payment_delay_days` only populated for "Paid Late" jobs
- Converted `zip_code` from numeric to text to preserve formatting and support joins

#### `services.csv`
- Checked for missing or invalid `service_type` or `price` values
- Reviewed service pricing distributions by type to ensure ranges made sense
- Cross-validated `job_id` values against `jobs.csv` to confirm relationship integrity
- Added `service_profit` field for service-level analysis; replaced cost nulls with 0s to retain rows in profit calculations

#### `clients.csv`
- Confirmed ZIP code formatting; changed data type to text for consistency
- Checked for duplicate `client_id` values — none found

#### `zip_regions.csv`
- Validated ZIP codes matched those used across `jobs.csv` and `clients.csv`
- Reviewed `region_name` spelling and ensured tier labels (High / Mid / Standard) were consistent


---
### Things to add still
Scanned for duplicate service types per job_id. Issue retained to reflect realistic dirty data handling.
