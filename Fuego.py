from Decorator import Decorator

class Fuego(Decorator):

    def __init__(self,EM):
        self.EM=EM

    def entrar(self):
        super().entrar()
        self.EM.entrar()
        print("La habitacion se esta quemando")