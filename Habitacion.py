from Contenedor import Contenedor

class Habitacion(Contenedor):
    def __init__(self,num):

        self.num=num

    def entrar(self):
        print("Estas en la habitacion", self.num)

    def esHabitacion(self):
        return True



