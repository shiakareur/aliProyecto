from app import db
from app import login
from models.Usuario import Usuario

class Persona(db.Model):
    codigo = db.Column(db.Integer, primary_key=True)
    nombres = db.Column(db.String(120), nullable=False)
    apellido_paterno = db.Column(db.String(80), index=True, nullable=False)
    apellido_materno = db.Column(db.String(80), index=True, nullable=False)
    dni = db.Column(db.String(8), index=True, nullable=False)
    fecha_nacimiento = db.Column(db.DateTime, nullable=False)
    genero = db.Column(db.String(1), index=True, nullable=False)
    correo = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(40), nullable=False)
    direccion = db.Column(db.String(200), nullable=False)
    hijos = db.Column(db.Integer, nullable=False)
