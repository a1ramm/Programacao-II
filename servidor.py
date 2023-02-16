from flask import Flask
app = Flask(__name__)
@app.route("/")

def oi():
    return "<b> oi </b>"

from classe_pessoa import Pessoa

# inicializa uma lista vazia
lista = []

# cria uma pessoa
p1 = Pessoa(nome = "João da Silva", email = "josilva@gmail.com",
            telefone = "47 99012 3232")

# adiciona a pessoa na lista
lista.append(p1)

# cria outra pessoa
p2 = Pessoa(nome = "Maria Oliveira", telefone = "47 98822 2531")

# adiciona pessoa na lista
lista.append(p2)

# percorre a lista
for p in lista:
    # exibe a pessoa "atual"
    print(p)

app.run(debug = True, host = '0.0.0.0', port = 4998)