from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class IngresarDatosForm(FlaskForm):
    codigo = StringField('Código', validators=[DataRequired()])
    modalidad = SelectField('Modalidad', validators=[DataRequired()])
    promocion = SelectField('Promoción', validators=[DataRequired()])
    nombres = StringField('Nombres', validators=[DataRequired()])
    apellido_paterno = StringField('Apellido Paterno', validators=[DataRequired()])
    apellido_materno = StringField('Apellido Materno', validators=[DataRequired()])
    planta = SelectField('Planta')
    genero = SelectField('Género', choices=[('M', 'Masculino'), ('F', 'Femenino')], validators=[DataRequired()])
    fecha_inicio = DateField('Fecha inicio', validators=[DataRequired()])
    fecha_nacimiento = DateField('Fecha nacimiento', validators=[DataRequired()])
    correo = StringField('Correo', validators=[DataRequired()])
    dni = StringField('DNI', validators=[DataRequired()])
    telefono = StringField('Teléfono', validators=[DataRequired()])
    direccion = StringField('Dirección', validators=[DataRequired()])
    hijos = IntegerField('Número de hijos', validators=[DataRequired()])
    submit = SubmitField('Enviar datos')


class CargaMasivaForm(FlaskForm):
    archivo_excel = FileField('Cargar archivo Excel', validators=[FileRequired()])
    submit = SubmitField('Cargar archivo')


class SeleccionarFechasForm(FlaskForm):
    fecha_inicio = DateField('Seleccionar fecha inicio', validators=[DataRequired()])
    fecha_fin = DateField('Seleccionar fecha fin', validators=[DataRequired()])
    submit = SubmitField('Buscar')

class BuscarCodigoForm(FlaskForm):
    codigo = IntegerField('Buscar código', validators=[DataRequired()])
    submit = SubmitField('Buscar')