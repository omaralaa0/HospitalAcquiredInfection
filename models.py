from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Patient(db.Model):
    __tablename__ = "patients"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200))
    phone = db.Column(db.String(20))
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))
    
    hr = db.Column(db.Float)
    o2sat = db.Column(db.Float)
    temp = db.Column(db.Float)
    map = db.Column(db.Float)
    resp = db.Column(db.Float)
    bun = db.Column(db.Float)
    chloride = db.Column(db.Float)
    creatinine = db.Column(db.Float)
    glucose = db.Column(db.Float)
    hct = db.Column(db.Float)
    hgb = db.Column(db.Float)
    wbc = db.Column(db.Float)
    platelets = db.Column(db.Float)
    
    hosp_adm_time = db.Column(db.Float)
    iculos = db.Column(db.Float)

    prediction = db.Column(db.String(50))
    probability = db.Column(db.Float)
