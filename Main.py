from Juego import Juego


class Main:
    def __init__(self, name):
        self.name = name

if __name__ == "__main__":
    juego = Juego()
    juego.laberinto = juego.laberinto2Hab()
