# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 15:54:01 2023

@author: Gemdelle
"""

# Ejercicio 1:
# El formato usado para las patentes consiste de 5 caracteres. Cada uno de esos carateres es un dígito entre 0 y 
# 9. Por ejemplo: “00123”, “99180”. La patente siguiente de una dada es la que se obtiene avanzando el último 
# dígito, es decir, reemplazándolo por el dígito siguiente correspondiente. Por ejemplo: la patente siguiente de 
# “00151” es “00152”. Cuando el último dígito es 9, se sustituye por el 0 y pasa a avanzar el anteúltimo dígito
# de la patente, teniendo en cuenta que también puede ser 9, este proceso se continúa hasta conseguir la 
# siguiente patente. Ejemplo: la siguiente de “09199” es “09200” y la siguiente de “09999” es “10000”. (No se 
# ingresan patentes mayores a “09999”, es decir, la última patente es “10000”).
# Se pide realizar la función siguiente(patente) que dada una patente calcule y retorne la patente siguiente. 
# Usar esta función para obtener la k-ésima patente siguiente. Por ejemplo: siguiente(“00151”) → “00152” y si 
# k = 5, la patente 5-ésima de “00151” es “00156”


# def createNumber():
#     number = input('Ingrese una patente: ')
#     return number

# def numberOK(number):
#     if int(number) > 9999:
#         return False
#     return True

# def numberHighestOK(number,k):
#     if int(number) == 9999 and k > 1:
#         return False
#     return True

# def createK():
#     k = int(input('Ingrese el número k: '))
#     return k

# def nextNumber(number,k):
    
#     final_number = list(str(int(number) + k))
    
#     while len(final_number) < 5:
#         final_number.insert(0,'0')
    
#     final_number = ''.join(final_number)
    
#     print(final_number)
    
# def main():
#     number = createNumber()
    
#     while not numberOK(number):
#         print('El número ingresado debe ser menor o igual a 09999')
#         number = createNumber()
    
#     k = createK()
    
#     while not numberHighestOK(number,k):
#         print('El máximo valor de k con 09999 es 1')
#         k = createK()
    
#     nextNumber(number,k)

# main()

# Ejercicio 2:
# Se tienen tres pilas de cartas: una con cartas sólo de espada, otra con cartas sólo de oros y otra
# con cartas sólo de bastos. Se desea armar una cuarta pila con la siguiente combinación:oro, oro, espada,
# basto, basto. Tener en cuenta que las tres pilas originales pueden no tener igual cantidad de cartas.

# Pila A = Pila de cartas a ser usada
# Pila B = Pila de cartas de palo Oro
# Pila C = Pila de cartas de palo Espada
# Pila D = Pila de cartas de palo Basto

# comenzar ejercicio_2
#  	mientras la pila B no está vacía y la pila C no está vacía y la pila D no está vacía hacer
# 		tomar una carta de la pila B
# 		depositar la carta en la pila A
# 		
# 		tomar una carta de la pila B
# 		depositar la carta en la pila A
# 		
# 		tomar una carta de la pila C
# 		depositar la carta en la pila A
# 		
# 		tomar una carta de la pila D
# 		depositar la carta en la pila A
# 		
# 		tomar una carta de la pila D
# 		depositar la carta en la pila A
#  	finmientras
# fin ejercicio_2

# Ejercicio 3:
# Esta aplicación deberá descubrir el refrán que está escrito en una frase donde cada palabra que forma la frase está 
# modificada de la siguiente forma:
# Las palabras con una cantidad par de letras están invertidas. Por ejemplo: sarbalap es palabras
# Se pide hacer la función obtenerPalabra(palabra) que dada una palabra obtenga la correspondiente al 
# refrán. Por ejemplo:
# obtenerPalabra(“sarbalap”) → “palabras”
# obtenerPalabra(“cosmpioli”) → “olimpicos”
# Usar la función para descubrir todas las palabras de un refrán. El refrán se debe poder leer de corrido,
# finalizado con punto y comenzando la primer letra en mayúscula. Por ejemplo: la información ingresada es: 
# on por mucho ragurdam amanece mas onarpmet y el programa deberá mostrar: No por mucho 
# madrugar amanece mas temprano.
# oN por mucho ragurdam amanece mas onarpmet ---> No por mucho madrugar amanece mas temprano

# def createPhrase():
#     return input('Ingrese un texto: ')

# def rewritePhrase(phrase):
    
#     phrase = phrase.split()
#     final_phrase = []
    
#     for i in range(len(phrase)):
#         if len(phrase[i]) % 2 == 0:
#             final_phrase.append(phrase[i][::-1])
#         else:
#             final_phrase.append(phrase[i])
    
#     final_phrase = ' '.join(final_phrase)
#     print(f'La frase desencriptada corresponde a ---> "{final_phrase}"')
    
# def main():
#     phrase = createPhrase()
#     rewritePhrase(phrase)
    
# main()
            

















































