# Hospital Resource Utilization & Patient Outcomes Dashboard

## Problem Statement

Hospitals generate large volumes of operational and clinical data, but decision-makers often lack a unified, easy-to-understand view of how resources are being utilized and how patients are performing across departments and branches.

Operational challenges such as bed shortages, uneven doctor workloads, delayed discharges, rising treatment costs, and readmissions require data-driven monitoring and planning. However, most hospital administrators are non-technical users and need interpretable dashboards rather than raw data or complex analytics tools.

The goal of this project is to design and build an interactive analytics dashboard that provides hospital operations teams with clear visibility into resource utilization, patient outcomes, and cost efficiency across a multi-specialty hospital network.

## Solution Architecture

The solution follows a modular analytics architecture that simulates a real-world hospital analytics system while respecting healthcare data privacy constraints.

**Architecture Flow:**

  <img width="127" height="585" alt="Solution_Architecture drawio" src="https://github.com/user-attachments/assets/c533c983-b191-439b-845c-49086466dc69" />

- Synthetic datasets are generated to simulate hospital operations data such as patients, admissions, beds, billing, doctors, and outcomes.
- PostgreSQL acts as the centralized relational database.
- A FastAPI backend serves as the data access and API layer.
- Power BI connects to the backend/database to create interactive dashboards for analysis and visualization.

This architecture ensures separation of data storage, processing, and visualization, making the system scalable and production-oriented.


## Tech Stack

**Database**
- PostgreSQL

**Backend**
- FastAPI
- Python
- SQLAlchemy
- Pandas

**Visualization**
- Power BI Desktop

**Deployment**
- Render (for FastAPI backend)

**Data Format**
- CSV (synthetic datasets)
- API responses (JSON)


## Dashboard Pages Overview

The Power BI dashboard is organized into three logical pages to support different levels of decision-making.

### Page 1: Executive Overview
This page provides a high-level snapshot of hospital performance for leadership and administrators.

Key insights include:
- Average Length of Stay (ALOS)
- Bed Occupancy Rate
- Total Admissions and Discharges
- Readmission Rate
- High-level trends across departments and branches

This page focuses on KPIs and summary metrics with simple visuals for quick decision-making.

<img width="1357" height="782" alt="Page-1" src="https://github.com/user-attachments/assets/3e3b78a1-cc93-4ecd-ba17-72570f3d99df" />


### Page 2: Resource Utilization
This page focuses on operational efficiency and capacity planning.

Key insights include:
- Bed occupancy by department
- ICU vs General bed utilization
- Doctor utilization percentage
- Admission patterns by day of the week

This page is intentionally kept free of slicers to act as a stable operational snapshot for hospital operations teams.

<img width="1357" height="787" alt="Page-2" src="https://github.com/user-attachments/assets/b320d0e9-c46a-4ad3-a963-145365e495ac" />


### Page 3: Patient Outcomes & Cost
This page enables deeper analytical exploration of outcomes and financial performance.

Key insights include:
- Distribution of patient outcomes (Recovered, Improved, Transferred, Deceased)
- Readmission Rate (KPI)
- Average Length of Stay (KPI)
- Total treatment cost by hospital branch
- Patient outcome mix by insurance type

Interactive slicers are provided for:
- Department
- Insurance Type

This page supports quality-of-care analysis, cost control, and policy-level insights.

<img width="1353" height="782" alt="page-3" src="https://github.com/user-attachments/assets/0cb70b88-6dba-4cf8-8ffe-ddedc5d18ee8" />


## Live Deployment

The FastAPI backend for this project is deployed and publicly accessible at:

**[https://hospital-resource-utilization-dashboard-1.onrender.com<MY-RENDER-URL>](https://hospital-resource-utilization-dashboard-1.onrender.com)**

The deployed API demonstrates live system availability and simulates an on-prem hospital analytics backend.

Due to healthcare data privacy constraints and competition rules that restrict the use of public cloud BI SaaS platforms, the Power BI dashboard is demonstrated locally using Power BI Desktop.

---

## How to Run the Project

### 1. Clone the Repository
```
git clone https://github.com/sharmaelango/Hospital_Resource_Utilization_Dashboard.git
cd Hospital_Resource_Utilization_Dashboard
```
### 2. Set Up the Database

Install PostgreSQL

Create a database (e.g., hospital_db)

Import the CSV files from the datasets/ folder into PostgreSQL

### 3. Run the Backend Locally

```
cd Hospital_Project/Backend
pip install -r requirements.txt
uvicorn app:app --reload
```
API will be available at:
```
http://127.0.0.1:8000
```

### 4. Open the Dashboard

Open Dashboard/Hospital_Dashboard.pbix using Power BI Desktop

Connect to the PostgreSQL database or backend API as configured


## Demo Video

A complete walkthrough video demonstrating:

- Problem context

- Solution architecture

- Dashboard functionality

- Key insights

- Live backend deployment

will be added here before final submission.


with your **actual Render URL**

2️⃣ Commit and push:
```
git add README.md
git commit -m "Add complete project documentation"
git push origin main
```
