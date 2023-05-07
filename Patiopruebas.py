from Fuego import Fuego
from Juego import Juego
from Laberinto import Laberinto

class Patiopruebas():

    def Menu(self):

        print("----------------------------------------------------")
        print("A que laberinto quieres jugar 2Habitaciones(pulsa 1) o 4Habitaciones(pulsa 2)? Si eliges 0, es que no quieres jugar más")
        eleccion = None

        while (eleccion != "0"):
            eleccion = input("Elige 1 o 2 -- Empieza a jugar de nuevo: ")

            if (eleccion == "1"):
                print("Vas a laberinto 2Habitaciones")
                self.Juego2habs()


            elif (eleccion == "2"):
                print("Laberinto 4Habitaciones")
                self.Juego4habs()

            elif (eleccion == "0"):
                print("Se cierra la aplicacion.")

            else:
                print("Eleccion no valida, elige jugar 2Habitaciones(pulsa 1) o 4Habitaciones(pulsa 2). Si eliges 0, es que no quieres jugar más.")

        print("Ya no se juega")

    def Juego2habs(self):

        juego= Juego()
        lab=juego.laberinto2Hab()
        print("----------------------------------------------------")
        print("En que habitacion quieres empezar 1 o 2? Si eliges 0 el juego se acabará")
        donde = None

        while (donde != "0"):
            donde = input("Elige hab: ")

            if (donde == "1"):
                print("Estamos en la habitacion 1")
                print("Elige una sentido: norte, sur, este u oeste")

                hab1 = lab.obtenerHabitacion(0)
                donde = input()
                if donde == "norte":
                    hab1.norte.entrar()
                elif donde == "este":
                    hab1.este.entrar()
                elif donde == "oeste":
                    hab1.oeste.entrar()
                elif donde == "sur":
                    hab1.sur.entrar()
                else:
                    print("Dirección no valida, elige: norte, sur, este, oeste")

            elif (donde == "2"):
                print("Estamos en la habitacion 2")
                print("Elige una sentido: norte, sur, este u oeste")
                hab2 = lab.obtenerHabitacion(1)
                donde = input()

                if donde == "norte":
                    hab2.norte.entrar()
                    print("Estas en la habitacion 1")
                elif donde == "este":
                    hab2.este.entrar()
                elif donde == "oeste":
                    hab2.oeste.entrar()
                elif donde == "sur":
                    hab2.sur.entrar()
                else:
                    print("Dirección no valida, elige: norte, sur, este, oeste")

            elif (donde == "0"):
                print("Ya no juegas más.")

            else:
                print("Eleccion no valida, elige hab 1 o 2, y si quieres acabar el juego pulsa 0.")

        print("El juego se ha acabado")

    def Juego4habs(self):
            juego = Juego()
            laberinto = juego.lab4habsFMComposite()
            print("EMPIEZA EL JUEGO\n")
            print("En que habitacion quieres empezar (1/2/3/4)?")
            eleccion = input()

            if eleccion == "1":
                print("Te encuentras en la primera habitación")
                print("Hacia qué orientacion quieres ir (norte,sur,este,oeste?")
                hab = laberinto.obtenerHabitacion(0)
                sentido = input()

                if sentido == "norte":
                    hab.norte.entrar()
                elif sentido == "este":
                    hab.este.entrar()
                elif sentido == "oeste":
                    hab.oeste.entrar()
                elif sentido == "sur":
                    hab.sur.entrar()
                else:
                    print("Dirección incorrecta, opciones válidas: norte, sur, este, oeste")

            elif eleccion == "2":
                print("Te encuentras en la segunda habitación")
                print("Hacia qué orientacion quieres ir (norte,sur,este,oeste?")

                hab = laberinto.obtenerHabitacion(1)
                sentido = input()
                if sentido == "norte":
                    hab.norte.entrar()
                elif sentido == "este":
                    hab.este.entrar()
                elif sentido == "oeste":
                    hab.oeste.entrar()
                elif sentido == "sur":
                    hab.sur.entrar()
                else:
                    print("Dirección incorrecta, opciones válidas: norte, sur, este, oeste")
            elif eleccion == "3":
                print("Te encuentras en la tercera habitación")
                print("Hacia qué orientacion quieres ir (norte,sur,este,oeste)?")

                hab = laberinto.obtenerHabitacion(2)
                sentido = input()
                if sentido == "norte":
                    hab.norte.entrar()
                elif sentido == "este":
                    hab.este.entrar()
                elif sentido == "oeste":
                    hab.oeste.entrar()
                elif sentido == "sur":
                    hab.sur.entrar()
                else:
                    print("Dirección incorrecta, opciones válidas: norte, sur, este, oeste")
            elif eleccion == "4":
                print("Te encuentras en la cuarta habitación")


                hab = laberinto.obtenerHabitacion(3)
                Fuego(hab).entrar()

                print("Huye antes que puedas, direcciones validas norte o oeste")
                sentido = input()
                if sentido == "norte":
                    hab.norte.entrar()
                elif sentido == "este":
                    hab.este.entrar()
                elif sentido == "oeste":
                    hab.oeste.entrar()
                elif sentido == "sur":
                    hab.sur.entrar()
                else:
                    print("Dirección incorrecta, opciones válidas: norte, sur, este, oeste")
            else:
                print("Opción inválida. Por favor, ingrese 1, 2, 3 o 4")
