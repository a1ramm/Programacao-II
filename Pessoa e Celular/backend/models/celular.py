from config.config import *
from models.pessoa import Pessoa

class Celular(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    modelo = db.Column(db.Text)
    marca = db.Column(db.Text)
    # atributo de relacionamento de chave estrangeira
    pessoa_id = db.Column(db.Integer, db.ForeignKey(Pessoa.id), nullable=False)
    # atributo de acesso ao objeto
    pessoa = db.relationship("Pessoa")
    
    def __str__(self):
        return f'''
        {self.modelo}, {self.marca}, {self.pessoa}
        '''

    def json(self):
        return {
            "id":self.id,
            "modelo":self.modelo,
            "marca":self.marca,
            "pessoa":self.pessoa.json()
        }
