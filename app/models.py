from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128))
    age = db.Column(db.Integer)

    #permite imprimir el objeto usuario y mostrar datos
    def __repr__(self):
        return '<User {}>'.format(self.username)

class Login(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), index=True)
    timestamp = db.Column(db.Date())