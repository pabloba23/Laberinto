from Decorator import Decorator

class Bomba(Decorator):
    def __init__(self,activa,EM):
        self.activa = activa
        self.EM=EM

    def start(self):
        self.activa=False
        return self

    def entrar(self):
        if(self.activa == True):
            print("Explota bomba, has muerto")

        else:
            self.EM.entrar()
            print("Bomba no activa")


