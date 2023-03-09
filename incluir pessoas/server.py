from flask import Flask, jsonify, request
from pessoa import Pessoa
from flask_cors import CORS

app = Flask(__name__)
with app.app_context():
    CORS(app)

    @app.route("/")
    def index():
        return "oe"

    @app.route('/incluir_pessoas', methods=['POST'])
    def incluir():
        dados = request.get_json() #recebe os dados das pessoas do html
        try:
            nova = Pessoa(**dados)

            return jsonify({"resultado": "ok"})

        except Exception as e:
            return jsonify({"resultado": "erro", "detalhes": str(e)})
        
if __name__ == "__main__":
    app.run(debug=True)