#!/usr/bin/python
#-*- coding: utf-8 -*-


from ElementoMapa import ElementoMapa

class Habitacion(ElementoMapa):
    def __init__(self,num):
        self.norte=None
        self.sur=None
        self.este=None
        self.oeste=None
        self.num=num

    def norte(self):
        return self.norte
    def sur(self):
        return self.sur
    def este(self):
        return self.este

    def oeste(self):
        return self.oeste

    def entrar(self):
        print("Estas en la habitacion", self.num)


