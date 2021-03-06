from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://sqlalchemy:Admin123@localhost:5432/revelhackathon'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app=app)
migrate = Migrate(app, db)

def create_all():
    import app.models

    db.create_all()
