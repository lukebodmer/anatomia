from anatomia import app
from flask import render_template
from flask import request
from partes.musculos.todos_los_musculos import todos_los_musculos
from partes.huesos.todos_los_huesos import todos_los_huesos
import partes

@app.route("/")
def home():
    return render_template("busqueda.html", musculos=todos_los_musculos, huesos=todos_los_huesos, iterador=[1,2,3,4,5,6])

@app.route('/buscar', methods=['POST'])
def handle_data():
    clicked=request.data
    print("CLICKED", clicked)
    return "OK"
