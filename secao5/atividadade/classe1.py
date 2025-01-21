class Animal():
    def __init__(self, nome):
        self.nome = nome
        
    def som(self):
        print(f"O animal {self.nome}")
        
class Cachorro(Animal):
    pass

class Gato(Animal):
    pass

dog = Cachorro("cachorro")
cat = Cachorro("gato")

dog.som()
cat.som()