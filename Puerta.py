#!/usr/bin/python
#-*- coding: utf-8 -*-

from ElementoMapa import ElementoMapa

class Puerta(ElementoMapa):
    def __init__(self,lado1,lado2,abierta):
        self.abierta = abierta
        self.lado1 = lado1
        self.lado2 = lado2

    def entrar(self):
        if self.abierta is True:
            print("La puerta esta abierta")
        else:
            print("La puerta esta cerrada")

