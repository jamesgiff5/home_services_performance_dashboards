# This script generates a synthetic dataset for a home services business.
# It simulates real-world fields like service type, date, ZIP code, income tier, pricing, costs, crews, and payment status.
# Includes logic for margin simulation, repeat client tagging, and light random variation to simulate real-world messiness in dates and costs.
# Useful for prototyping Tableau dashboards focused on ops, finance, or retention.
# Output is a CSV file with realistic messiness (nulls, cost gaps) to support downstream data prep steps.

import pandas as pd
import numpy as np
import random
from datetime import datetime

np.random.seed(42)
random.seed(42)

zip_regions_data = [{'zip_code': '32751', 'region_name': 'Maitland', 'tier': 'High'}, {'zip_code': '32779', 'region_name': 'Wekiva Springs', 'tier': 'High'}, {'zip_code': '32789', 'region_name': 'Winter Park', 'tier': 'High'}, {'zip_code': '32801', 'region_name': 'Downtown Orlando', 'tier': 'High'}, {'zip_code': '32804', 'region_name': 'College Park', 'tier': 'High'}, {'zip_code': '32806', 'region_name': 'SoDo', 'tier': 'High'}, {'zip_code': '32819', 'region_name': 'Universal Area', 'tier': 'High'}, {'zip_code': '32827', 'region_name': 'Lake Nona', 'tier': 'High'}, {'zip_code': '32836', 'region_name': 'Dr. Phillips', 'tier': 'High'}, {'zip_code': '34786', 'region_name': 'Windermere', 'tier': 'High'}, {'zip_code': '34787', 'region_name': 'Winter Garden', 'tier': 'High'}, {'zip_code': '32708', 'region_name': 'Winter Springs', 'tier': 'Mid'}, {'zip_code': '32835', 'region_name': 'MetroWest', 'tier': 'Mid'}, {'zip_code': '32837', 'region_name': "Hunter's Creek", 'tier': 'Mid'}, {'zip_code': '32714', 'region_name': 'Altamonte Springs', 'tier': 'Mid'}, {'zip_code': '32750', 'region_name': 'Longwood', 'tier': 'Mid'}, {'zip_code': '32765', 'region_name': 'Oviedo', 'tier': 'Mid'}, {'zip_code': '32766', 'region_name': 'Chuluota', 'tier': 'Mid'}, {'zip_code': '32792', 'region_name': 'Goldenrod', 'tier': 'Mid'}, {'zip_code': '32803', 'region_name': 'Colonialtown', 'tier': 'Mid'}, {'zip_code': '32821', 'region_name': 'Seaworld Area', 'tier': 'Mid'}, {'zip_code': '32825', 'region_name': 'East Orlando', 'tier': 'Mid'}, {'zip_code': '32828', 'region_name': 'Waterford Lakes', 'tier': 'Mid'}, {'zip_code': '34747', 'region_name': 'Celebration', 'tier': 'Mid'}, {'zip_code': '32730', 'region_name': 'Fern Park', 'tier': 'Standard'}, {'zip_code': '32771', 'region_name': 'Sanford', 'tier': 'Standard'}, {'zip_code': '32817', 'region_name': 'Union Park', 'tier': 'Standard'}, {'zip_code': '32839', 'region_name': 'Pine Castle', 'tier': 'Standard'}, {'zip_code': '34761', 'region_name': 'Ocoee', 'tier': 'Standard'}, {'zip_code': '32701', 'region_name': 'Altamonte East', 'tier': 'Standard'}, {'zip_code': '32703', 'region_name': 'Apopka', 'tier': 'Standard'}, {'zip_code': '32707', 'region_name': 'Casselberry', 'tier': 'Standard'}, {'zip_code': '32712', 'region_name': 'Apopka North', 'tier': 'Standard'}, {'zip_code': '32773', 'region_name': 'Sanford South', 'tier': 'Standard'}, {'zip_code': '32805', 'region_name': 'Paramore', 'tier': 'Standard'}, {'zip_code': '32807', 'region_name': 'Azalea Park', 'tier': 'Standard'}, {'zip_code': '32808', 'region_name': 'Pine Hills', 'tier': 'Standard'}, {'zip_code': '32809', 'region_name': 'Sky Lake', 'tier': 'Standard'}, {'zip_code': '32810', 'region_name': 'Lockhart', 'tier': 'Standard'}, {'zip_code': '32811', 'region_name': 'Millenia', 'tier': 'Standard'}, {'zip_code': '32812', 'region_name': 'Dover Shores', 'tier': 'Standard'}, {'zip_code': '32818', 'region_name': 'Hiawassee', 'tier': 'Standard'}, {'zip_code': '32822', 'region_name': 'Conway', 'tier': 'Standard'}, {'zip_code': '32824', 'region_name': 'Meadow Woods', 'tier': 'Standard'}, {'zip_code': '32829', 'region_name': 'Vista Lakes', 'tier': 'Standard'}, {'zip_code': '34741', 'region_name': 'Kissimmee', 'tier': 'Standard'}, {'zip_code': '34743', 'region_name': 'Buenaventura Lakes', 'tier': 'Standard'}, {'zip_code': '34744', 'region_name': 'East Kissimmee', 'tier': 'Standard'}]

service_price_ranges = {
    'Roof Cleaning': [450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1100, 1200, 1300, 1400, 1500, 1600],
    'Paver Sealing': [800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2200, 2400, 2600, 2800, 3000],
    'House Wash': [300, 350, 400, 450, 500, 550, 600, 650, 700],
    'Patio/Pool Deck Cleaning': [200, 250, 300, 350, 400, 450, 500],
    'Driveway Cleaning': [200, 250, 300, 350, 400, 450, 500],
    'Solar Panel Cleaning': [200, 250, 300, 350, 400, 450, 500],
    'Window Cleaning': [200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700]
}

# Date range excluding weekends and hard-coded holidays
date_range = pd.date_range(start='2023-01-01', end='2024-12-31', freq='D')
HOLIDAYS_MMDD = {'01-01', '07-04', '11-23', '12-25'}
date_range = [d for d in date_range if d.strftime('%m-%d') not in HOLIDAYS_MMDD and d.weekday() < 6]

service_types = [
    {'type': 'Roof Cleaning', 'prob': 0.3},
    {'type': 'Paver Sealing', 'prob': 0.25},
    {'type': 'House Wash', 'prob': 0.15},
    {'type': 'Driveway Cleaning', 'prob': 0.10},
    {'type': 'Patio/Pool Deck Cleaning', 'prob': 0.10},
    {'type': 'Window Cleaning', 'prob': 0.07},
    {'type': 'Solar Panel Cleaning', 'prob': 0.03}
]

jobs, services, clients = [], [], []
client_id = 1000
job_id = 1000
crew_daily_capacity = {1: 3, 2: 3, 3: 3, 4: 3}
HOLIDAYS = ['2023-07-04', '2023-11-23', '2023-12-25', '2024-07-04', '2024-11-28', '2024-12-25']

zip_regions_df = pd.DataFrame(zip_regions_data)

for job_date in date_range:
    if job_date.strftime('%Y-%m-%d') in HOLIDAYS:
        continue

    num_jobs_today = np.random.poisson(5)
    if num_jobs_today == 0:
        continue

    crew_jobs_today = {1: 0, 2: 0, 3: 0, 4: 0}

    for _ in range(min(num_jobs_today, 10)):
        zip_choice = random.choice(zip_regions_data)
        zip_code = zip_choice['zip_code']

        if clients and random.random() < 0.3:
            client = random.choice(clients)
            cid = client['client_id']
            zip_code = client['zip_code']
        else:
            client_id += 1
            cid = client_id
            clients.append({'client_id': cid, 'zip_code': zip_code})

        eligible_crews = [c for c in crew_jobs_today if crew_jobs_today[c] < crew_daily_capacity[c]]
        if not eligible_crews:
            continue
        crew_id = random.choice(eligible_crews)
        crew_jobs_today[crew_id] += 1

        job_status = 'Completed'
        payment_status = random.choices(['Paid', 'Paid Late', 'Unpaid'], weights=[0.85, 0.12, 0.03])[0]
        delay = 0 if payment_status == 'Paid' else np.random.randint(1, 21)
        delay = min(delay, (datetime(2024, 12, 31) - job_date).days)

        num_services = np.random.choice([1, 2, 3], p=[0.5, 0.3, 0.2])
        job_material = job_labor = job_travel = job_price = 0

        for _ in range(num_services):
            svc_choice = random.choices(service_types, weights=[s['prob'] for s in service_types])[0]
            svc_type = svc_choice['type']

            base_price = random.choice(service_price_ranges[svc_type])

            if svc_type == 'Paver Sealing':
                material_pct = 0.40
            elif svc_type == 'Roof Cleaning':
                material_pct = 0.10
            elif svc_type in ['Window Cleaning', 'Solar Panel Cleaning']:
                material_pct = 0.03
            else:
                material_pct = np.random.uniform(0.10, 0.15)

            s_material = round(base_price * material_pct, 2)
            s_labor = round(np.random.uniform(50, 200), 2)
            s_travel = round(np.random.uniform(10, 30), 2)
            markup = np.random.uniform(1.10, 1.30)
            s_price = base_price
            s_profit = round(s_price - (s_material + s_labor + s_travel), 2)


            services.append({
                'job_id': job_id,
                'service_type': svc_type,
                'price': s_price,
                'material_cost': s_material,
                'labor_cost': s_labor,
                'travel_cost': s_travel,
                'service_profit': s_profit
            })

            job_material += s_material
            job_labor += s_labor
            job_travel += s_travel
            job_price += s_price

        job_profit = round(job_price - (job_material + job_labor + job_travel), 2)

        jobs.append({
            'job_id': job_id,
            'job_date': job_date.strftime('%Y-%m-%d'),
            'client_id': cid,
            'zip_code': zip_code,
            'crew_id': crew_id,
            'job_status': job_status,
            'total_price': round(job_price, 2),
            'material_cost': round(job_material, 2),
            'labor_cost': round(job_labor, 2),
            'travel_cost': round(job_travel, 2),
            'profit': job_profit,
            'payment_status': payment_status,
            'payment_delay_days': delay,
            'num_services': num_services
        })

        job_id += 1

# Save CSVs
pd.DataFrame(jobs).to_csv("jobs_v9.csv", index=False)
pd.DataFrame(services).to_csv("services_v9.csv", index=False)
pd.DataFrame(clients).merge(pd.DataFrame(zip_regions_data), on='zip_code', how='left').to_csv("clients_v9.csv", index=False)
pd.DataFrame(zip_regions_data).to_csv("zip_regions_v9.csv", index=False)
