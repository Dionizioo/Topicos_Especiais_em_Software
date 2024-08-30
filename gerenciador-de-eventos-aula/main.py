from flask import render_template, redirect, url_for, flash
from config import app, db
from models import load_user, Event
from models import User
from werkzeug.security import generate_password_hash, check_password_hash
from forms import LoginForm, RegisterForm, EventForm
from flask_login import login_user, logout_user, login_required


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    from forms import RegisterForm


    formulario = RegisterForm()

    if formulario.validate_on_submit():
        usu = formulario.username.data
        #senha com hash
        sen = generate_password_hash(formulario.password.data)
        #sen = formulario.password.data

        usuarioBanco = User.query.filter_by(usuario=usu).first()
        if usuarioBanco:
            flash('Usuario já cadastrado')
        else:
            novoUsuario = User(usuario=usu,senha=sen)
            db.session.add(novoUsuario)
            db.session.commit()
            flash('Usuario cadastrado com sucesso')

            return redirect(url_for('login'))  #procura com base no nome da função


    return render_template('register.html',form=formulario)


@app.route('/login', methods=['GET', 'POST'])
def login():

    formulario = LoginForm()

    if formulario.validate_on_submit():
        usu = formulario.username.data
        sen = formulario.password.data

        usuarioBanco = User.query.filter_by(usuario=usu).first()
        if usuarioBanco and check_password_hash(usuarioBanco.senha,sen):
            flash('Usuario logado com sucesso')
            return redirect(url_for('dashboard'))
        else:
            flash('Usuario ou senha invalidos')
            return redirect(url_for('login'))




    return render_template('login.html',form=formulario)


@app.route('/logout')
def logout():
    logout_user()
    return  redirect(url_for('home'))


@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')


@app.route('/create_event', methods=['GET', 'POST'])
def create_event():

    formulario = EventForm()

    if formulario.validate_on_submit():
        nome = formulario.event_name.data
        data = formulario.event_date.data
        descricao = formulario.description.data

        evento = Event(nome=nome,data_evento=data,descricao=descricao,usuario_id=1)

        db.session.add(evento)
        db.session.commit()
        flash('Evento cadastrado com sucesso')
        return redirect(url_for('dashboard'))
    else:
        print(formulario.errors)

    return render_template('create_event.html', form=formulario)


@app.route('/edit_event/<int:event_id>', methods=['GET', 'POST'])
def edit_event(event_id):

    evento = Event.query.get(event_id)
    formulario = EventForm(obj=evento)

    if formulario.validate_on_submit():
        evento.nome = formulario.event_name.data
        evento.data_evento = formulario.event_date.data
        evento.descricao = formulario.description.data

        db.session.commit()
        flash('Evento editado com sucesso')

        return redirect(url_for('dashboard'))

    return render_template('edit_event.html')


@app.route('/delete_event/<int:event_id>', methods=['POST'])
def delete_event(event_id):
    pass


if __name__ == '__main__':
    app.run(debug=True)
