#!/usr/bin/python
#-*- coding: utf-8 -*-

from Habitación import Habitación
from ElementoMapa import ElementoMapa

class Habitación(Habitación, ElementoMapa):
    def __init__(self,num):
        self.norte = None
		self.sur=None
		self.este=None
		self.oeste=None
		self.num=num

