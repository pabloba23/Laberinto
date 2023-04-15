#!/usr/bin/python
#-*- coding: utf-8 -*-

from Pared import Pared

class ParedBomba(Pared):
    def __init__(self, activa):
        self.activa = activa

    def entrar(self):
        print("Ha explotado la bomba de la pared")
