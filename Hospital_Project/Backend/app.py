from fastapi import FastAPI
from .db import get_connection


app = FastAPI(title="Hospital Analytics API")

# -----------------------------
# Health check
# -----------------------------
@app.get("/")
def root():
    return {"status": "Hospital Analytics API is running"}

# -----------------------------
# KPI 1: Average Length of Stay
# -----------------------------
@app.get("/kpi/average-length-of-stay")
def average_length_of_stay():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT department,
               AVG(discharge_datetime - admission_datetime) AS avg_stay
        FROM admissions
        GROUP BY department
    """)
    data = cur.fetchall()
    conn.close()

    return [{"department": d, "average_stay_days": float(a.days)} for d, a in data]

# -----------------------------
# KPI 2: Bed Occupancy Rate
# -----------------------------
@app.get("/kpi/bed-occupancy")
def bed_occupancy():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT department,
               ROUND(AVG(occupied_flag) * 100, 2) AS occupancy_rate
        FROM beds
        GROUP BY department
    """)
    data = cur.fetchall()
    conn.close()

    return [{"department": d, "occupancy_rate_percent": r} for d, r in data]

# -----------------------------
# KPI 3: Readmission Rate
# -----------------------------
@app.get("/kpi/readmission-rate")
def readmission_rate():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT
          ROUND(AVG(readmitted_30_days) * 100, 2)
        FROM outcomes
    """)
    rate = cur.fetchone()[0]
    conn.close()

    return {"readmission_rate_percent": rate}

# -----------------------------
# KPI 4: Cost per Discharge
# -----------------------------
@app.get("/kpi/cost-per-discharge")
def cost_per_discharge():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT department,
               ROUND(AVG(total_cost), 2)
        FROM admissions a
        JOIN billing b ON a.admission_id = b.admission_id
        GROUP BY department
    """)
    data = cur.fetchall()
    conn.close()

    return [{"department": d, "avg_cost": c} for d, c in data]
