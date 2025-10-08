## 🧼 Data Cleaning Summary
This file summarizes all field-level cleaning and structural fixes performed in Excel prior to Tableau analysis. Higher-level data modeling choices and assumptions (e.g., simulated payment behavior, synthetic profitability logic) are documented in the dashboard-specific README files.  

---
### `jobs.csv`

This file drives both dashboards and contains job-level fields used in volume, margin, and repeat behavior analysis.

- Sorted by `job_date` to check for missing or misaligned dates
- Verified ~3% of `crew_id` values were blank as expected (simulated nulls)
- Checked `profit` for nulls or outliers — all aligned with synthetic cost structure
- Confirmed `payment_delay_days` only appears when `payment_status` = "Paid Late"
- Recast `zip_code` as text to prevent formatting issues in joins
- Merged repeat behavior from a grouped client table (`client_job_count`)
  - Added `is_repeat_client` (boolean)
  - Added `job_count_per_client` for supporting calcs
- Created realized performance fields:
  - `realized_total_price`, `realized_job_profit`, `realized_job_profit_pct`
  - Based on paid jobs only, simulating collection-based profitability

---
### `services.csv`

This file contains individual line items for each service booked within a job, including pricing, costs, and derived profitability metrics. Used to power service-level analysis and filtering in the dashboards.

- Filled missing `cost` values with 0 to avoid null breakage in Tableau and preserve full job records in analysis
- Validated price and cost distributions per service type to confirm realistic ranges and margin consistency
- Cross-referenced `job_id` values with `jobs.csv` to ensure data joins accurately reflect multi-service jobs
- Calculated `service_profit` and `service_margin_pct` to enable profitability ranking and margin filtering
- Brought in `is_paid` and `payment_status` from `jobs.csv` to support toggling between quoted and realized profitability
- Created `realized_service_profit` field to isolate earned profit from only completed, paid jobs

---
### `clients.csv`
This file maps each client to their ZIP code and regional tier classification for segmentation analysis.

- Confirmed ZIP code formatting; converted to text for consistency across datasets
- Checked for duplicate `client_id` values — none found
- Verified `region_name` and `tier` labeling matched values in `zip_regions.csv`

---
### `zip_regions.csv`

ZIP-level lookup for assigning income tiers.

- Verified all ZIPs match those used in `clients.csv` and `jobs.csv`
- Validated `region_name` and `income_tier` labels for spelling and consistency
- No missing or duplicate ZIP codes
- Income tiers were manually assigned based on plausible segmentation logic, not actual census thresholds, designed to simulate regional differences in client behavior and job mix
