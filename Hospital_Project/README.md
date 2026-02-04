# Hospital Resource Utilization & Patient Outcomes Dashboard

## Current Progress
✅ Step 1 Completed – Synthetic Dataset Generation

## Project Overview
This project aims to build an interactive analytics dashboard for hospital operations teams to monitor and optimize resource utilization, patient flow, and outcomes across departments and branches.

Due to healthcare data privacy constraints, all datasets used in this project are fully synthetic and generated using realistic hospital operational assumptions.

## Available Datasets
- patients.csv
- admissions.csv
- doctors.csv
- doctor_schedule.csv
- procedures.csv
- billing.csv
- outcomes.csv
- beds.csv

## Progress Update
✅ Step 2 Completed – PostgreSQL Database Setup

All synthetic datasets have been successfully loaded into a PostgreSQL database.  
The database now serves as the single source of truth for analytics and dashboard development.


## Upcoming Steps

- Build FastAPI backend for ETL & KPIs
- Develop Power BI / Apache Superset dashboard
- Enable CSV / Excel / PDF exports
