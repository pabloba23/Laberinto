#!/usr/bin/python
# -*- coding: utf-8 -*-

from Laberinto import Laberinto
from Habitacion import Habitacion
from Puerta import Puerta
from Pared import Pared


class Juego:
    def __init__(self):
        self.laberinto = None

    def fabricarLaberinto(self):
        return Laberinto()

    def fabricarPared(self):
        return Pared()

    def fabricarPuerta(self, lado1, lado2, abierta):
        puerta = Puerta(lado1, lado2, abierta)
        return puerta

    def fabricarHab(self, num):
        habitacion = Habitacion(num)
        habitacion.este = self.fabricarPared()
        habitacion.oeste = self.fabricarPared()
        habitacion.sur = self.fabricarPared()
        habitacion.norte = self.fabricarPared()
        return habitacion

    def laberinto2Hab(self):
        hab1 = self.fabricarHab(1)
        hab2 = self.fabricarHab(2)

        puerta = self.fabricarPuerta(hab1,hab2,'true')

        hab1.sur=puerta
        hab2.norte=puerta

        laberinto=self.fabricarLaberinto()
        laberinto.agregarHabitacion(hab1)
        laberinto.agregarHabitacion(hab2)

        print("----------------------------------------------------")
        print("En que habitacion quieres empezar 1 o 2? Si eliges 0 el juego se acabará")
        donde=None

        while(donde!="0"):
            donde=input("Elige hab: ")

            if(donde== "1"):
                print("Estamos en la habitacion 1")
                print("Elige una sentido: norte, sur, este u oeste")

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

            elif(donde=="2"):
                print("Estamos en la habitacion 2")
                print("Elige una sentido: norte, sur, este u oeste")

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

            elif (donde=="0"):
                print("Ya no juegas más.")

            else:
                print("Eleccion no valida, elige hab 1 o 2, y si quieres acabar el juego pulsa 0.")

        print("El juego se ha acabado")















