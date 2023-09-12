class Pessoa:
    def __init__(self, id):
        self.__nome = None 
        self.id = id  

    def set_nome(self, nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome

    nome = property(get_nome, set_nome)

pessoa = Pessoa(0)
pessoa.set_nome('joao')
print("ID:", pessoa.id)
print("Nome:", pessoa.get_nome()) 
