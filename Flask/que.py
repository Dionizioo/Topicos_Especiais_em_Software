from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class MyForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    btn = SubmitField('Enviar')
