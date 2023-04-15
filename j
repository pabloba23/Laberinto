[1mdiff --git a/ElementoMapa.py b/ElementoMapa.py[m
[1mindex d4258ca..4d6ccfd 100644[m
[1m--- a/ElementoMapa.py[m
[1m+++ b/ElementoMapa.py[m
[36m@@ -1,10 +1,9 @@[m
[31m-#!/usr/bin/python[m
[31m-#-*- coding: utf-8 -*-[m
[32m+[m[32mfrom abc import ABC[m
 [m
[31m-class ElementoMapa:[m
[32m+[m
[32m+[m[32mclass ElementoMapa(ABC):[m
     def __init__(self):[m
         pass[m
 [m
[31m-    def entrar(self, ):[m
[32m+[m[32m    def entrar(self):[m
         pass[m
[31m-[m
[1mdiff --git a/HabitacionBomba.py b/HabitacionBomba.py[m
[1mindex 4c254c5..456989e 100644[m
[1m--- a/HabitacionBomba.py[m
[1m+++ b/HabitacionBomba.py[m
[36m@@ -1,7 +1,7 @@[m
 #!/usr/bin/python[m
 #-*- coding: utf-8 -*-[m
 [m
[31m-from Habitación import Habitación[m
[32m+[m[32mfrom Habitacion import Habitación[m
 [m
 class HabitacionBomba(Habitación):[m
     def __init__(self):[m
[1mdiff --git a/Juego.py b/Juego.py[m
[1mindex ead1555..81f63aa 100644[m
[1m--- a/Juego.py[m
[1m+++ b/Juego.py[m
[36m@@ -1,42 +1,50 @@[m
 #!/usr/bin/python[m
[31m-#-*- coding: utf-8 -*-[m
[32m+[m[32m# -*- coding: utf-8 -*-[m
 [m
 from Laberinto import Laberinto[m
 from Habitacion import Habitacion[m
 from Puerta import Puerta[m
 from Pared import Pared[m
 [m
[32m+[m
 class Juego:[m
[31m-    def__init__(self):[m
[31m-	self.laberinto=None[m
[31m-	[m
[32m+[m[32m    def __init__(self):[m
[32m+[m[32m        self.laberinto = None[m
[32m+[m
     def fabricarLaberinto(self):[m
[31m-	return Laberinto()[m
[31m-[m
[31m-    def laberinto2HabitacionFM(self):[m
[31m-	self.laberinto=self.fabricarLaberinto()[m
[31m-[m
[31m-    def laberinto2Habitaciones(self):[m
[31m-	self.laberinto=Laberinto()[m
[31m-	[m
[31m-	hab1=Habitacion(1)[m
[31m-	hab2=Habitacion(2)[m
[31m-	[m
[31m-	puerta=Puerta()[m
[31m-	puerta.lado1=hab1[m
[31m-	puerta.lado2=hab2[m
[31m-[m
[31m-	hab1.norte=Pared()[m
[31m-	hab1.este=Pared()[m
[31m-	hab1.oeste=Pared()[m
[31m-[m
[31m-	hab2.sur=Pared()[m
[31m-	hab2.este=Pared()[m
[31m-	hab2.oeste=Pared()[m
[31m-[m
[31m-	self.laberinto.agregarHabitacion(hab1)[m
[31m-	self.laberinto.agregarHabitacion(hab2)´[m
[31m-[m
[31m-juego=Juego()[m
[31m-juego.laberinto2Habitaciones()[m
[31m-	[m
\ No newline at end of file[m
[32m+[m[32m        return Laberinto()[m
[32m+[m
[32m+[m[32m    def fabricarPared(self):[m
[32m+[m[32m        return Pared()[m
[32m+[m
[32m+[m[32m    def fabricarPuerta(self, lado1, lado2, abierta):[m
[32m+[m[32m        puerta = Puerta(lado1, lado2, abierta)[m
[32m+[m[32m        return puerta[m
[32m+[m
[32m+[m[32m    def fabricarHab(self, num):[m
[32m+[m[32m        habitacion = Habitacion(num)[m
[32m+[m[32m        habitacion.este = self.fabricarPared[m
[32m+[m[32m        habitacion.oeste = self.fabricarPared[m
[32m+[m[32m        habitacion.sur = self.fabricarPared[m
[32m+[m[32m        habitacion.norte = self.fabricarPared[m
[32m+[m[32m        return habitacion[m
[32m+[m
[32m+[m[32m    def laberinto2Hab(self):[m
[32m+[m[32m        hab1 = self.fabricarHab(1)[m
[32m+[m[32m        hab2 = self.fabricarHab(2)[m
[32m+[m
[32m+[m[32m        puerta = self.fabricarPuerta(hab1, hab2, 'true')[m
[32m+[m
[32m+[m[32m        hab1.sur = puerta[m
[32m+[m[32m        hab2.norte = puerta[m
[32m+[m
[32m+[m[32m        laberinto = self.fabricarLaberinto()[m
[32m+[m[32m        laberinto.agregarHabitacion(hab1)[m
[32m+[m[32m        laberinto.agregarHabitacion(hab2)[m
[32m+[m
[32m+[m[32m        print("En que habitacion quieres empezar")[m
[32m+[m[32m        donde = input()[m
[32m+[m
[32m+[m[32m        while (donde == 0):[m
[32m+[m[32m            print("Habitacion no valida, en que habitacion quieres empezar")[m
[32m+[m[32m            donde = input()[m
[1mdiff --git a/Laberinto.py b/Laberinto.py[m
[1mindex 6ca5d15..b767abe 100644[m
[1m--- a/Laberinto.py[m
[1m+++ b/Laberinto.py[m
[36m@@ -4,6 +4,12 @@[m
 from Habitacion import Habitacion[m
 class Laberinto:[m
     def __init__(self):[m
[31m-	self.habitaciones=list()[m
[32m+[m	[32mself.habitaciones=[][m
[32m+[m
[32m+[m[32m    def habs(self):[m
[32m+[m[32m        return self.habitaciones[m
     def agregarHabitacion(self,hab):[m
[31m-	self.habitaciones[m
[32m+[m	[32mself.habitaciones.append(hab)[m
[32m+[m
[32m+[m[32m    def obtenerHabitacion(self,num):[m
[32m+[m[32m        return self.habitaciones[num][m
[1mdiff --git a/Puerta.py b/Puerta.py[m
[1mindex 5be0ac4..10d6965 100644[m
[1m--- a/Puerta.py[m
[1m+++ b/Puerta.py[m
[36m@@ -4,10 +4,10 @@[m
 from ElementoMapa import ElementoMapa[m
 [m
 class Puerta(ElementoMapa):[m
[31m-    def __init__(self):[m
[31m-        self.abierta = None[m
[31m-        self.lado1 = None[m
[31m-        self.lado2 = None[m
[32m+[m[32m    def __init__(self,lado1,lado2,abierta):[m
[32m+[m[32m        self.abierta = abierta[m
[32m+[m[32m        self.lado1 = lado1[m
[32m+[m[32m        self.lado2 = lado2[m
 [m
     def entrar(self):[m
         if self.abierta is True:[m
