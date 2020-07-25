from anatomia import app
from flask import render_template
from flask import request
from partes.musculos.todos_los_musculos import todos_los_musculos
import partes

@app.route("/")
def home():
    return render_template("busqueda.html", musculos=todos_los_musculos)

@app.route('/buscar', methods=['POST'])
def handle_data():
    clicked=request.data
    print("CLICKED", clicked)
    return "OK"
