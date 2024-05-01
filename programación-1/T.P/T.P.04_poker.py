# -*- coding: utf-8 -*-
"""
Created on Wed Aug  30 08:53:31 2023

@author: gemdelle
"""

#  ˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳⁺ˏ༻✧ 𝓣.𝓟. 𝟘𝟜 - 𝓟𝓸𝓴𝓮𝓻 ✧༺ˎ⁺˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳

# En los juegos de naipes, una carta tiene dos atributos: un valor (1,2,3,4,5,6,7,8,9,10,J,Q,K) y
# un palo (♠, ♣,♥, ♦). En un programa, el valor puede ser representado como un número del
# 1 al 13, y el palo como un carácter ('T','D','C','P'). Una carta puede ser representada como
# una tupla de dos elementos: (valor,palo), por ejemplo: (5,'T') representa la carta 5 de trébol.
# El as se representa por 1, y la J,Q, y K como 11, 12, 13. En el juego de póker, una mano
# tiene 5 cartas, lo que en un programa vendría a ser un conjunto de cinco tuplas, por
# ejemplo:
# mano = {(1, 'P'), (1, 'C'), (1, 'T'), (13, 'D'), (12, 'P')}
# 1) Un full es una mano en que tres cartas tienen el mismo valor, y las otras dos tienen otro
# valor común. Por ejemplo, A♠ A♥ 6♣ A♦ 6♦ es un full (tres ases y dos seis), pero 2♣
# A♥ Q♥ A♦ 6♦ no. Escriba una función que indique si la mano es un full.
# >>> mano1 = {(1, 'P'), (1, 'C'), (6, 'T'), (1, 'D'), (6, 'D')}
# >>> mano2 = {(2, 'T'), (1, 'C'), (12, 'C'), (1, 'D'), (6, 'D')}
# >>> esFull(mano1)
# True
# >>> esFull(mano2)
# False
# 2) Un color es una mano en que todas las cartas tienen el mismo palo. Por ejemplo, 8♠ K♠
# 4♠ 9♠ 2♠ es un color (todas las cartas son picas), pero Q♣ A♥ 5♥ 2♥ 2♦ no lo es.
# Escriba la función que indique si la mano es un color:
# >>> mano1 = {(8, 'P'), (13, 'P'), (4, 'P'), (9, 'P'), (2, 'P')}
# >>> mano2 = {(12, 'T'), (1, 'C'), (5, 'C'), (2, 'C'), (2, 'D')}
# >>> esColor(mano1)
# True
# >>> esColor(mano2)
# False
# 3) Una escalera es una mano en que las cartas tienen valores consecutivos. Por ejemplo, 4♠
# 7♥ 3♥ 6♣ 5♣ es una escalera (tiene los valores 3, 4, 5, 6 y 7), pero Q♣ 7♥ 3♥ Q♥ 5♣ no
# lo es.
# Escriba la función que indique si la mano es una escalera:
# >>> mano1 = {(4, 'P'), (7, 'C'), (3, 'C'), (6, 'T'), (5, 'T')}
# >>> mano2 = {(12, 'T'), (7, 'C'), (3, 'C'), (12, 'C'), (5, 'T')}
# >>> esEscalera(mano1)
# True
# >>> esEscalera(mano2)
# False
# 4) Una escalera de color es una escalera en la que todas las cartas tienen el mismo palo. Por
# ejemplo, 4♦ 7♦ 3♦ 6♦ 5♦ es una escalera de color (son sólo diamantes, y los valores 3, 4,
# 5, 6 y 7 son consecutivos).
# Escriba la función que indique si la mano es una escalera de color:
# >>> mano1 = {(4, 'P'), (7, 'C'), (3, 'C'), (6, 'T'), (5, 'T')}
# >>> mano2 = {(8, 'P'), (13, 'P'), (4, 'P'), (9, 'P'), (2, 'P')}
# >>> mano3 = {(4, 'D'), (7, 'D'), (3, 'D'), (6, 'D'), (5, 'D')}
# >>> esEscaleraDeColor(mano1)
# False
# >>> esEscaleraDeC(mano2)
# False
# >>> es_escalera_de_color(mano3)
# True
# 5) Escriba las funciones para identificar las demás manos del póker.
# 6) Escriba un programa que pida al usuario ingresar cinco cartas, y le indique qué tipo de
# mano es:
# Carta 1: 5D
# Carta 2: QT
# Carta 3: QD
# Carta 4: 10P
# Carta 5: 5C
# Doble pareja
# Carta 1: KP
# Carta 2: KT
# Carta 3: 8T
# Carta 4: KC
# Carta 5: 2P
# Trio
# Carta 1: 4P
# Carta 2: 4C
# Carta 3: QD
# Carta 4: 4D
# Carta 5: QT
# Full
    
    
    
    
    
    


    
    
    
    
    
    

