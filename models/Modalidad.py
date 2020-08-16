from app import db
from app import login
from models.Usuario import Usuario

class Modalidad(db.Model):
    id_modalidad = db.Column(db.Integer, primary_key=True)
    nombre_modalidad = db.Column(db.String(100), index=True, nullable=False)
    modalidad = db.relationship('Informacion', backref='mod', lazy='dynamic')
