from app import app
import json
from flask import request, render_template
from app import db
from app.models import Login

@app.route('/')
def index():
    return render_template("index.html")


@app.route("/sumar")
def sumar():
    valores = request.args
    valor1 = int(valores["valor1"])
    valor2 = int(valores["valor2"])

    return str(valor1+valor2)

@app.route("/mostrar/<id>")
def mostrar(id):
    return id

@app.route("/logins")
def getLogins():
    logins = Login.query.all()

    res = []
    for login in logins:
        res.append({"login": login.username, "timestamp": str(login.timestamp)})

    return json.dumps(res)