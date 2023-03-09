class Pessoa:

    def __init__(self, nome, nascimento, email, telefone):
        self.nome = nome
        self.nascimento = nascimento
        self.email = email
        self.telefone = telefone 

    def __str__(self):
        return f'Nome: {self.nome},\nNascimento: {self.nascimento} \nEmail: {self.email} \nTelefone: {self.telefone}'

    def json (self):
        return {
            'nome': self.nome,
            'nascimento': self.nascimento,
            'email': self.email,
            'telefone': self.telefone
        }