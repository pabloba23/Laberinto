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
        habitacion.este = self.fabricarPared
        habitacion.oeste = self.fabricarPared
        habitacion.sur = self.fabricarPared
        habitacion.norte = self.fabricarPared
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


        print("En que habitacion quieres empezar")
        donde=input()

        while(donde==0):
            print("Habitacion no valida, en que habitacion quieres empezar")
            donde=input()









