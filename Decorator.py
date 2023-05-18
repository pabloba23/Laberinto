from Hoja import Hoja

class Decorator(Hoja):

    def __init__(self,EM):
        self.component=EM
    def entrar(self):
        super().entrar()


