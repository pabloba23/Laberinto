#!/usr/bin/python
# -*- coding: utf-8 -*-
from Armario import Armario
from Bomba import Bomba
from Espada import Espada
from Este import Este
from Fuego import Fuego
from Laberinto import Laberinto
from Habitacion import Habitacion
from Norte import Norte
from Oeste import Oeste
from Puerta import Puerta
from Pared import Pared
from Sur import Sur


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

    def fabricarNorte(self):
        return Norte()

    def fabricarSur(self):
        return Sur()

    def fabricarEste(self):
        return Este()

    def fabricarOeste(self):
        return Oeste()

    def fabricarArm(self):
        return Armario()

    def fabricarBomba(self,bool,EM):
        return Bomba(bool, EM)

    def fabricarHabComposite(self, num):
        hab = Habitacion(num)
        hab.ponerEn(self.fabricarNorte(), self.fabricarPared())
        hab.ponerEn(self.fabricarSur(), self.fabricarPared())
        hab.ponerEn(self.fabricarEste(), self.fabricarPared())
        hab.ponerEn(self.fabricarOeste(), self.fabricarPared())
        return hab

    def laberinto2Hab(self):
        hab1 = self.fabricarHab(1)
        hab2 = self.fabricarHab(2)

        puerta = self.fabricarPuerta(hab1,hab2,True)

        hab1.sur=puerta
        hab2.norte=puerta

        laberinto=self.fabricarLaberinto()
        laberinto.agregarHabitacion(hab1)
        laberinto.agregarHabitacion(hab2)


    def lab4habsFMComposite(self):

            hab1 = self.fabricarHabComposite(1)
            hab2 = self.fabricarHabComposite(2)
            hab3 = self.fabricarHabComposite(3)
            hab4 = self.fabricarHabComposite(4)

            fuego = Fuego(hab4)

            p1 = self.fabricarPuerta(hab1, hab2, True)
            p2 = self.fabricarPuerta(hab2, hab4, True)
            p3 = self.fabricarPuerta(hab4, hab3, True)
            p4 = self.fabricarPuerta(hab4, hab1, False)

            bomba = Bomba(True, p3)
            espada = Espada(self.fabricarArm())

            bomba = self.fabricarBomba(True, self.fabricarArm())
            hab2.ponerEn(self.fabricarNorte(), bomba)

            hab1.ponerEn(self.fabricarEste(), p1)
            hab1.ponerEn(self.fabricarSur(), p4)

            hab2.ponerEn(self.fabricarOeste(), p1)
            hab2.ponerEn(self.fabricarSur(), p2)

            hab3.ponerEn(self.fabricarNorte(), p4)
            hab3.ponerEn(self.fabricarSur(),espada)
            hab3.ponerEn(self.fabricarEste(), bomba)

            hab4.ponerEn(self.fabricarNorte(), p2)
            hab4.ponerEn(self.fabricarOeste(), bomba)

            lab = self.fabricarLaberinto()
            lab.agregarHabitacion(hab1)
            lab.agregarHabitacion(hab2)
            lab.agregarHabitacion(hab3)
            lab.agregarHabitacion(hab4)

            return lab

















