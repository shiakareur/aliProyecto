from app import db
from app import login
from models.Usuario import Usuario

class Informacion(db.Model):
    estado = db.Column(db.String(45), nullable=False)
    planta = db.Column(db.String(45), nullable=False)
    motivo_cese = db.Column(db.String(200))
    observaciones = db.Column(db.String(300))
    fecha_inicio = db.Column(db.DateTime, nullable=False)
    fecha_fin = db.Column(db.DateTime)
    fecha_renovacion = db.Column(db.DateTime, nullable=False)
    fecha_cese = db.Column(db.DateTime, nullable=False)
    codigo_persona = db.Column(db.Integer, db.ForeignKey('persona.codigo'), primary_key=True)
    id_promocion = db.Column(db.Integer, db.ForeignKey('promocion.id_promocion'))
    id_modalidad = db.Column(db.Integer, db.ForeignKey('modalidad.id_modalidad'))
