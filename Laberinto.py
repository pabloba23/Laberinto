
class Laberinto:
    def __init__(self):
        self.habitaciones = []

    def habs(self):
        return self.habitaciones

    def agregarHabitacion(self, hab):
        self.habitaciones.append(hab)

    def obtenerHabitacion(self, num):
        return self.habitaciones[num]
