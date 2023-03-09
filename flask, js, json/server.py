from flask import Flask, jsonify
from pessoa import Pessoa
from flask_cors import CORS

app = Flask(__name__)

CORS(app) 

@app.route("/")
def index():
    return "oi"

@app.route('/listar_pessoas')
def listar():
    ret = []
    lista = [
        Pessoa(nome = "Maria",
               nascimento = "01/01/2005",
               email = 'm@gmail.com',
               telefone = '1234-5678')
               ]

    for pessoa in lista:
        ret.append(pessoa.json())
    return jsonify(ret)

app.run(debug=True, host="0.0.0.0")


