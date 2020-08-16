from app import db
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from app import login

class Usuario(UserMixin, db.Model):
    nombre_usuario = db.Column(db.String(45), primary_key=True)
    clave = db.Column(db.String(200), nullable=False)

    def set_password(self, password):
        self.clave = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.clave, password)

    def get_id(self):
        return self.nombre_usuario

@login.user_loader
def load_user(id):
    return Usuario.query.get(id)