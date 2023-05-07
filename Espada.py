from Decorator import Decorator

class Espada(Decorator):

    def __init__(self,EM):
        self.EM=EM
    def entrar(self):
        super().entrar()
        self.EM.entrar()
        print("Armario: tiene una espada")