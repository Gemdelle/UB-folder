#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 18:43:10 2024

@author: gemy
"""

# INGRESAR COORDENADAS DEL REY

reyX=int(input("seleccione la posicion x del rey: "))
reyY=int(input("seleccione la  posicion y del rey: "))

while reyX < 0 or reyX >= 8 or reyY < 0 or reyY >= 8:
    print("Coordenadas inválidas. Deben estar dentro del rango (0-7).")
#     # Pedir al usuario que ingrese las coordenadas nuevamente
    reyX = int(input("Seleccione la posición x del rey: "))
    reyY = int(input("Seleccione la posición y del rey: "))


print(f"Coordenadas válidas: [{reyX},{reyY}]")

# INGRESAR COORDENADAS DE PIEZA Y EL TIPO DE PIEZA

coordenada x (int)
coordenada y (int)
tipo "caballo" (str)

# MOVIMIENTOS QUE REALIZA CADA PIEZA

si nombre == "torre":

