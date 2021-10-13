#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 18:20:52 2021

@author: Johanna Peña
"""

# Ejercicio #1 Parte 2

#instrucción que permite mostrar un mensaje en consola.
print("Programa  que  identifica  el  tipo  de  dato  de  un  valor  ingresado  por  el  usuario,  se  realizarán  cinco interacciones:\n")
#uso de variable y función input que permite ingresar por teclado un valor.
variable1=input("Primera Interacción, ingrese un valor cualquiera: ")
#uso de funciones anidadas en una sola linea de código que permite mostrar un mensaje con el typo de dato ingresado por teclado
print("Este tipo de dato en Python es:\n", type(variable1))
variable2=input("Segunda Interacción, ingrese un valor cualquiera: ")
print("Este tipo de dato en Python es:\n", type(variable2))
variable3=input("Tercera Interacción, ingrese un valor cualquiera: ")
print("Este tipo de dato en Python es:\n", type(variable3))
variable4=input("Cuarta Interacción, ingrese un valor cualquiera: ")
print("Este tipo de dato en Python es:\n", type(variable4))
variable5=input("Quinta Interacción, ingrese un valor cualquiera: ")
print("Este tipo de dato en Python es:\n", type(variable5))
print("¡YA NO SE HARÁN MÁS INTERACCIONES!")
