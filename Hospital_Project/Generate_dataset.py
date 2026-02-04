import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

# -------------------------
# Common values
# -------------------------
departments = ["Cardiology", "Oncology", "Orthopedics", "Pediatrics", "Emergency", "General Medicine"]
branches = ["Chennai", "Coimbatore", "Bangalore"]
insurance_types = ["Private", "Govt", "Self"]
outcomes_list = ["Recovered", "Improved", "Transferred", "Deceased"]

# -------------------------
# 1. patients.csv
# -------------------------
patients = []
for i in range(3000):
    patients.append({
        "patient_id": f"P{i+1}",
        "age": np.random.randint(1, 90),
        "gender": np.random.choice(["Male", "Female"]),
        "insurance_type": np.random.choice(insurance_types)
    })

patients_df = pd.DataFrame(patients)

# -------------------------
# 2. doctors.csv
# -------------------------
doctors = []
for i in range(150):
    doctors.append({
        "doctor_id": f"D{i+1}",
        "department": np.random.choice(departments),
        "specialization": "General"
    })

doctors_df = pd.DataFrame(doctors)

# -------------------------
# 3. admissions.csv
# -------------------------
admissions = []
start_date = datetime(2025, 1, 1)

for i in range(5000):
    admit_time = start_date + timedelta(days=np.random.randint(0, 365))
    discharge_time = admit_time + timedelta(days=np.random.randint(1, 10))

    admissions.append({
        "admission_id": f"A{i+1}",
        "patient_id": np.random.choice(patients_df["patient_id"]),
        "branch": np.random.choice(branches),
        "department": np.random.choice(departments),
        "admission_type": np.random.choice(["Emergency", "Scheduled"]),
        "admission_datetime": admit_time,
        "discharge_datetime": discharge_time
    })

admissions_df = pd.DataFrame(admissions)

# -------------------------
# 4. doctor_schedule.csv
# -------------------------
doctor_schedule = []
for _ in range(8000):
    scheduled = 8
    utilized = round(np.random.uniform(3, 8), 1)

    doctor_schedule.append({
        "doctor_id": np.random.choice(doctors_df["doctor_id"]),
        "date": start_date + timedelta(days=np.random.randint(0, 365)),
        "hours_scheduled": scheduled,
        "hours_utilized": utilized
    })

doctor_schedule_df = pd.DataFrame(doctor_schedule)

# -------------------------
# 5. procedures.csv
# -------------------------
procedures = []
for i in range(6000):
    procedures.append({
        "procedure_id": f"PR{i+1}",
        "admission_id": np.random.choice(admissions_df["admission_id"]),
        "department": np.random.choice(departments),
        "procedure_type": "Standard Procedure",
        "procedure_datetime": start_date + timedelta(days=np.random.randint(0, 365))
    })

procedures_df = pd.DataFrame(procedures)

# -------------------------
# 6. billing.csv
# -------------------------
billing = []
for adm in admissions_df["admission_id"]:
    room_cost = np.random.randint(5000, 40000)
    procedure_cost = np.random.randint(10000, 80000)

    billing.append({
        "admission_id": adm,
        "room_cost": room_cost,
        "procedure_cost": procedure_cost,
        "total_cost": room_cost + procedure_cost
    })

billing_df = pd.DataFrame(billing)

# -------------------------
# 7. outcomes.csv
# -------------------------
outcomes = []
for adm in admissions_df["admission_id"]:
    outcomes.append({
        "admission_id": adm,
        "outcome": np.random.choice(outcomes_list),
        "readmitted_30_days": np.random.choice([0, 1], p=[0.85, 0.15])
    })

outcomes_df = pd.DataFrame(outcomes)

# -------------------------
# 8. beds.csv
# -------------------------
beds = []
for i in range(20000):
    beds.append({
        "bed_id": f"B{i+1}",
        "branch": np.random.choice(branches),
        "department": np.random.choice(departments),
        "bed_type": np.random.choice(["General", "ICU"]),
        "occupied_date": start_date + timedelta(days=np.random.randint(0, 365)),
        "occupied_flag": np.random.choice([0, 1], p=[0.3, 0.7])
    })

beds_df = pd.DataFrame(beds)

# -------------------------
# SAVE ALL FILES
# -------------------------
output_path = "dataset/"

patients_df.to_csv(output_path + "patients.csv", index=False)
admissions_df.to_csv(output_path + "admissions.csv", index=False)
doctors_df.to_csv(output_path + "doctors.csv", index=False)
doctor_schedule_df.to_csv(output_path + "doctor_schedule.csv", index=False)
procedures_df.to_csv(output_path + "procedures.csv", index=False)
billing_df.to_csv(output_path + "billing.csv", index=False)
outcomes_df.to_csv(output_path + "outcomes.csv", index=False)
beds_df.to_csv(output_path + "beds.csv", index=False)

print("✅ All synthetic hospital datasets created successfully!")
