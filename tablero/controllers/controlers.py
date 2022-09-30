from tablero import app
from flask import render_template


@app.route('/')
def tablero():
    return render_template("tablero.html")


@app.route('/<int:numero>')
def tablero_num(numero):
    return render_template("tablero_num.html", numero=numero)


@app.route('/<int:num1>/<int:num2>')
def tablero_completo(num1,num2):
    return render_template("tablero_completo.html",x=num1,y=num2)