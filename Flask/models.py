
from flask_sqlalchemy import SQLAlchemy
from main import app


db = SQLAlchemy()
db.init_app()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(50), primary_key=True, unique=True,nullable=False)
    senha = db.Column(db.String(),  nullable=False)


with app.app_context():
    db.create_all()