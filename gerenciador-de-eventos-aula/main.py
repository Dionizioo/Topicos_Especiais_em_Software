from flask import render_template, redirect, url_for, flash
from config import app, db
from models import load_user
from models import User
from werkzeug.security import generate_password_hash, check_password_hash
from forms import LoginForm


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
            return redirect(url_for('/'))


    return render_template('login.html')


@app.route('/logout')
def logout():
    pass


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/create_event', methods=['GET', 'POST'])
def create_event():
    return render_template('create_event.html')


@app.route('/edit_event/<int:event_id>', methods=['GET', 'POST'])
def edit_event(event_id):
    return render_template('edit_event.html')


@app.route('/delete_event/<int:event_id>', methods=['POST'])
def delete_event(event_id):
    pass


if __name__ == '__main__':
    app.run(debug=True)
