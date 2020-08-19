from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm, IngresarDatosForm, CargaMasivaForm, SeleccionarFechasForm
from flask_login import current_user, login_user
from models.Usuario import Usuario
from models.Persona import Persona
from models.Informacion import Informacion
from flask_login import logout_user
from flask_login import login_required
from flask import request
from werkzeug.urls import url_parse


@app.route('/')
@app.route('/index')
def index():
    return redirect(url_for('ingresar_datos'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Usuario.query.filter_by(nombre_usuario=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')

        return redirect(next_page)

    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/ingresar_datos')
def ingresar_datos():
    form = IngresarDatosForm()
    if form.validate_on_submit():
        pass
    return render_template('ingresar_datos.html', form=form, title='Ingresar Datos')


@app.route('/carga_masiva', methods=['GET', 'POST'])
def carga_masiva():
    form = CargaMasivaForm()
    if form.validate_on_submit():
        pass
    return render_template('carga_masiva.html', form=form, title='Carga masiva')


@app.route('/proximos_ceses', methods=['GET', 'POST'])
def proximos_ceses():
    form = SeleccionarFechasForm()
    if form.validate_on_submit():
        return redirect(url_for('proximos_ceses_tabla'))
    return render_template('proximos_ceses.html', form=form, title='Próximos ceses')


@app.route('/proximos_ceses_tabla')
def proximos_ceses_tabla():
    return render_template('proximos_ceses_tabla.html')


@app.route('/proximas_renovaciones', methods=['GET', 'POST'])
def proximas_renovaciones():
    form = SeleccionarFechasForm()
    if form.validate_on_submit():
        return redirect(url_for('proximas_renovaciones_tabla',
                                fecha_inicio=form.fecha_inicio.data,
                                fecha_fin=form.fecha_fin.data))
    return render_template('proximas_renovaciones.html', form=form, title='Próximas renovaciones')


@app.route('/proximas_renovaciones_tabla')
def proximas_renovaciones_tabla():
    f_inicio_renovacion = request.args.get('fecha_inicio')
    f_fin_renovacion = request.args.get('fecha_fin')
    l_prox_renovaciones = Informacion.query.join(Persona).add_columns(Persona.codigo, Persona.nombres,
                                                                      Persona.apellido_paterno,
                                                                      Persona.apellido_materno).filter(
        Informacion.fecha_renovacion >= f_inicio_renovacion).filter(
        Informacion.fecha_renovacion <= f_fin_renovacion).all()
    print(l_prox_renovaciones)
    return render_template('proximas_renovaciones_tabla.html', l_prox_renovaciones=l_prox_renovaciones)
