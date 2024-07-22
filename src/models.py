from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Characters(db.Model):
    __tablename__ = 'characters'
   
    charId = db.Column(db.Integer, primary_key=True)
    charName = db.Column(db.String(250))
    charDescription = db.Column(db.String(2500))
    charOrigin = db.Column(db.String(250))

class Planets(db.Model):
    __tablename__ = 'planets'

    planetId = db.Column (db.Integer, primary_key=True)
    planetName = db.Column (db.String(250))
    planetDescription = db.Column (db.String (2500))