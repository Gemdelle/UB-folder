# -*- coding: utf-8 -*-
"""
Created on Wed Aug  30 08:53:31 2023

@author: gemdelle
"""

#  ˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳⁺ˏ༻✧ 𝓣.𝓟. 𝟘𝟝 - 𝓡𝓮𝓼𝓬𝓪𝓽𝓮 𝓭𝓮 𝓷𝓪𝓾𝓯𝓻𝓪𝓰𝓸𝓼 ✧༺ˎ⁺˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳

#  Ver Imagen
# Náufragos es un juego basado en el juego Galaxis que consiste en rescatar personas
# perdidas en el espacio. En nuestro caso, el rescate se produce en el mar, y el objetivo es
# rescatar la máxima cantidad de personas, con la menor cantidad de sondas detectoras.
# Una sonda detectora es un artefacto que se utiliza para detectar personas. Cuando una
# sonda es activada en una posición dada, ésta envía una señal en dirección de cada uno de
# los cuatro puntos cardinales. La señal se propaga hasta perderse salvo que choque con el
# dispositivo reflector de alguno de los náufragos. En ese caso, la señal retorna a la sonda lo
# que produce que se encienda una luz intermitente sobre la cubierta de la sonda. Note que
# cada sonda tiene una única luz, por lo cual cuando la luz comienza a parpadear, no hay
# forma de saber si esto ocurre por que retornaron varias señales o sólo una, tampoco hay
# cómo saber desde que dirección retornó la señal, y menos aún, a qué distancia de la sonda
# se encontraba el dispositivo reflector que hizo retornar la señal.
# Sin embargo la sonda detectora sí es capaz de determinar si ella es activada en la posición
# en que se encuentra un náufrago, en cuyo caso la luz se enciende y no parpadea. Cuando
# esto sucede, el náufrago puede ser rescatado desde la posición en que se ha activado la
# sonda.
# En el siguiente ejemplo se muestra las posiciones de 4 náufragos, representados por la
# letra N. Así, si la sonda detectora es activada en la posición [3,3] la señal se pierde, en tanto
# que si es activada en la posición [6,2] se detecta un náufrago, y en la posición [6,5] se
# rescata un náufrago.
# Estrategia de solución
# Para implementar este juego se utiliza una lista bidimensional que representar´a el tablero
# correspondiente al espacio del naufragio. El tamaño del tablero será configurable, y en él
# se dispondrán los náufragos en posiciones aleatorias. La cantidad de náufragos, así como la
# cantidad de sondas disponibles también será configurable.
# En cada paso, debe pedirse al jugador la posición en la cual desea activar una sonda
# detectora.
# El algoritmo deberá determinar si en esa posición existe un náufrago, si en alguna de las
# cuatro direcciones existe un náufrago, o si la señal se pierde. En cualquier situación debe
# notificar el resultado al jugador. Esta rutina se repite hasta que se hayan rescatado todos
# los náufragos, o se acaben las sondas detectoras.
    
    
    
    
    
    

