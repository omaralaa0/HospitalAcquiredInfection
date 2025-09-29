import joblib
import numpy as np
from flask_sqlalchemy import SQLAlchemy
from models import db, Patient
from flask import Flask, render_template, request, redirect, url_for, jsonify
import os
from dotenv import load_dotenv

app = Flask(__name__)

@app.template_filter('getattr')
def getattr_filter(obj, attr, default=''):
    return getattr(obj, attr, default)



load_dotenv()

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

model = joblib.load("rfc_model_compressed.pkl")

@app.route("/")
def home():
    return render_template("form.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        name = request.form.get("name")
        address = request.form.get("address")
        phone = request.form.get("phone")

        fields = [
            "HR","O2Sat","Temp","MAP","Resp","BUN","Chloride","Creatinine",
            "Glucose","Hct","Hgb","WBC","Platelets","Age","HospAdmTime","ICULOS"
        ]
        values = [float(request.form[field]) for field in fields]

        g_str = request.form.get("Gender", "")
        if g_str == "":
            return render_template("result.html", prediction="Please select Gender.")
        g = int(g_str)

        dummy_0 = 1.0 if g == 0 else 0.0
        dummy_1 = 1.0 if g == 1 else 0.0
        values.extend([dummy_0, dummy_1])

        X = np.array(values).reshape(1, -1)

        pred = model.predict(X)[0]
        proba = None
        if hasattr(model, "predict_proba"):
            try:
                proba = float(model.predict_proba(X)[0][1])
            except Exception:
                pass

        msg = "Patient has Hospital Acquired Infection" if pred == 1 else "Patient does not have HAI"
        if proba is not None:
            msg += f" (probability: {proba:.2%})"

        new_patient = Patient(
            name=name,
            address=address,
            phone=phone,
            age=float(request.form.get("Age")),
            gender="Male" if g == 1 else "Female",
            hr=float(request.form.get("HR")),
            o2sat=float(request.form.get("O2Sat")),
            temp=float(request.form.get("Temp")),
            map=float(request.form.get("MAP")),
            resp=float(request.form.get("Resp")),
            bun=float(request.form.get("BUN")),
            chloride=float(request.form.get("Chloride")),
            creatinine=float(request.form.get("Creatinine")),
            glucose=float(request.form.get("Glucose")),
            hct=float(request.form.get("Hct")),
            hgb=float(request.form.get("Hgb")),
            wbc=float(request.form.get("WBC")),
            platelets=float(request.form.get("Platelets")),
            hosp_adm_time=float(request.form.get("HospAdmTime")),
            iculos=float(request.form.get("ICULOS")),
            prediction="HAI" if pred == 1 else "No HAI",
            probability=proba
        )
        db.session.add(new_patient)
        db.session.commit()

        return render_template("result.html", prediction=msg)

    except Exception as e:
        return render_template("result.html", prediction=f"Error: {e}")


@app.route("/patients")
def patients():
    all_patients = Patient.query.all()
    return render_template("patients.html", patients=all_patients)


@app.route("/patients/<int:patient_id>/edit", methods=["GET"])
def edit_patient(patient_id):
    patient = Patient.query.get_or_404(patient_id)

    field_map = {
        "HR": "hr",
        "O2Sat": "o2sat",
        "Temp": "temp",
        "MAP": "map",
        "Resp": "resp",
        "BUN": "bun",
        "Chloride": "chloride",
        "Creatinine": "creatinine",
        "Glucose": "glucose",
        "Hct": "hct",
        "Hgb": "hgb",
        "WBC": "wbc",
        "Platelets": "platelets",
        "Age": "age",
        "HospAdmTime": "hosp_adm_time",
        "ICULOS": "iculos"
    }

    return render_template("form.html", patient=patient, field_map=field_map)


@app.route("/patients/<int:patient_id>/update", methods=["POST"])
def update_patient(patient_id):
    patient = Patient.query.get_or_404(patient_id)

    patient.name = request.form.get("name")
    patient.phone = request.form.get("phone")
    patient.address = request.form.get("address")
    patient.age = float(request.form.get("Age"))
    patient.gender = "Male" if request.form.get("Gender") == "1" else "Female"
    patient.hr = float(request.form.get("HR"))
    patient.o2sat = float(request.form.get("O2Sat"))
    patient.temp = float(request.form.get("Temp"))
    patient.map = float(request.form.get("MAP"))
    patient.resp = float(request.form.get("Resp"))
    patient.bun = float(request.form.get("BUN"))
    patient.chloride = float(request.form.get("Chloride"))
    patient.creatinine = float(request.form.get("Creatinine"))
    patient.glucose = float(request.form.get("Glucose"))
    patient.hct = float(request.form.get("Hct"))
    patient.hgb = float(request.form.get("Hgb"))
    patient.wbc = float(request.form.get("WBC"))
    patient.platelets = float(request.form.get("Platelets"))
    patient.hosp_adm_time = float(request.form.get("HospAdmTime"))
    patient.iculos = float(request.form.get("ICULOS"))

    db.session.commit()
    return redirect(url_for("patients"))


@app.route("/patients/<int:patient_id>", methods=["DELETE"])
def delete_patient(patient_id):
    patient = Patient.query.get(patient_id)
    if not patient:
        return jsonify({"error": "Patient not found"}), 404

    db.session.delete(patient)
    db.session.commit()
    return jsonify({"message": f"Patient {patient_id} deleted successfully"})


@app.route("/stats", methods=["GET"])
def get_stats():
    total = Patient.query.count()
    total_males = Patient.query.filter_by(gender="Male").count()
    total_females = Patient.query.filter_by(gender="Female").count()

    hai = Patient.query.filter_by(prediction="HAI").count()
    no_hai = total - hai

    male_hai = Patient.query.filter_by(gender="Male", prediction="HAI").count()
    female_hai = Patient.query.filter_by(gender="Female", prediction="HAI").count()

    stats = {
        "total_patients": total,
        "total_males": total_males,
        "total_females": total_females,
        "male_hai": male_hai,
        "female_hai": female_hai,
        "hai_cases": hai,
        "non_hai_cases": no_hai,
    }

    return render_template("stats.html", stats=stats)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=False)
