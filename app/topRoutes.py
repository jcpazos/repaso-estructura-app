from app import app
from flask import request, render_template

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