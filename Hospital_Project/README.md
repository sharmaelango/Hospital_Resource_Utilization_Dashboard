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
✅ Step 3 Completed – FastAPI Backend

A FastAPI backend has been implemented to serve hospital KPIs such as:
- Average Length of Stay
- Bed Occupancy Rate
- Readmission Rate
- Cost per Discharge

The backend connects directly to PostgreSQL and exposes REST APIs for BI integration.



## Upcoming Steps
- Develop Power BI / Apache Superset dashboard
- Enable CSV / Excel / PDF exports

