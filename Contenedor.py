from ElementoMapa import ElementoMapa

class Contenedor(ElementoMapa):

    def __init__(self):
        self.hijos=[]
        self.ors = []

    def entrar(self):
        pass

    def agregarHijos(self,unEM):
        self.hijos.append(unEM)

    def ors(self):
        self.ors
    def agregarOrientacion(self,Or):
        self.ors.append(Or)

    def ponerEn(self,Or,unEM):
        Or.ponerEM(unEM,self)