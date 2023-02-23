class Pessoa:
    # usando valor padrão nos parâmetros do construtor
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone

    # usando string formatada, que coisa linda :-)
    def __str__(self):
        return f'{self.nome}, '+\
               f'{self.email}, {self.telefone}'

    # expressar a classe em formato json
    def json(self):
        return {
            "nome" : self.nome,
            "email" : self.email,
            "telefone" : self.telefone 
        }

# teste da classe
p1 = Pessoa(nome = "João da Silva", 
            email = "josilva@gmail.com",  
            telefone = "47 99012 3232")
            
# exibir em formato textual
print(p1)

# exibir em format json
print(p1.json())

'''
resultado da execução:

João da Silva, josilva@gmail.com, 47 99012 3232
{'nome': 'João da Silva', 'email': 'josilva@gmail.com', 'telefone': '47 99012 3232'}

'''
