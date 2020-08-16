from app import db
from app import login
from models.Usuario import Usuario

class Promocion(db.Model):
    id_promocion = db.Column(db.Integer, primary_key=True)
    nombre_promocion = db.Column(db.String(100), index=True, nullable=False)
    promocion = db.relationship('Informacion', backref='promo', lazy='dynamic')
