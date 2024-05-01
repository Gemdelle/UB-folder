# -*- coding: utf-8 -*-
"""
Created on Wed Aug  30 08:53:31 2023

@author: gemdelle
"""

#  ˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳⁺ˏ༻✧ 𝓣.𝓟. 𝟘𝟛 - 𝓒𝓲𝓯𝓻𝓪𝓭𝓸 ✧༺ˎ⁺˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳

# El agente 0069 lleva años utilizando un método de codificación de mensajes secretos.
# Si X es el mensaje original, éste se codifica en dos etapas:
# 1. X se transforma en X' reemplazando cada sucesión de caracteres consecutivos
# que no sean vocales por su imagen especular.
# X' se transforma en la sucesión de caracteres X'' obtenida al ir tomando sucesivamente:
# el primer carácter de X', luego el último, luego el segundo, luego el penúltimo, etc.
# Por ejemplo, para X = "Bond, James Bond", resultan:
# X' = "BoJ ,dnameB sodn"
# y
# X'' = "BnodJo s, dBneam"
# Lo que el pobre agente 0069 no sabe es que el señor Fon Noiman ha analizado algunos
# mensajes cifrados y ha dado con el mecanismo que está utilizando. Lo único que le
# queda a Fon Noiman es hacer el programa que, dado un mensaje cifrado, lo descifre.
# Entrada
# Un mensaje cifrado según el algoritmo anterior. El agente 0069 utiliza un teclado inglés,
# por lo que ninguna vocal tendrá tilde y no tiene ñ.
# Salida
# Se mostrará el mensaje cifrado leído de la entrada y a continuación aparecerá "=>"entre
# dos espacios y el mensaje original descifrado.
# Entrada de ejemplo
# Ejemplos:
# BnodJo s, dBneam
# aueoi
# E. .n.ualn cnhuag aMda rle
# Aauirnedleiua nBo

# Salida de ejemplo
# BnodJo s, dBneam => Bond, James Bond
# BnodJo s, dBneam

# aueoi => aeiou
# aueoi

# E. .n.ualn cnhuag aMda rle => En un lugar de la Mancha...
# Ea .n.u.ln cnhuag aMda  rle

# Aauirnedleiua nBo => Aureliano Buendia 
# Aauirnedleiua nBo

# ----------------------------------------------------------------------------------------------------------------------------

# ENCRIPTACIÓN

# 00. Definir acción: encriptar o desencriptar
def defineAction():
    return (input('¿Desea encriptar o desencriptar una frase? [E/D]: ')).upper()

# 01. Ingresar una frase y separar las letras 
def createPhrase():
    return list(input('Ingrese una frase: '))

# 02. Si la letra es una vocal, agregar - antes y después
def addUnderscores(phrase):
    VOWELS = 'aeiouAEIOU'
    
    underscore_array = []
    
    for i in range(len(phrase)):
        if i+1 < len(phrase):
            if phrase[i] in VOWELS and phrase[i+1] not in VOWELS:
                underscore_array.append(phrase[i])
                underscore_array.append('-')
            elif phrase[i] not in VOWELS and phrase[i+1] in VOWELS:
                underscore_array.append(phrase[i])
                underscore_array.append('-')
            else:
                underscore_array.append(phrase[i])
        elif i == len(phrase)-1:
            underscore_array.append(phrase[i])

    return underscore_array

# 03. Separar las partes del array entre -
def splitArr(underscore_array):
    underscore_array = ''.join(underscore_array)
    split_array = underscore_array.split('-')
    
    return split_array

# 04. Si el elemento del array tiene más de 1 letra, invertirlo
def reverseArr(split_array):
    VOWELS = 'aeiouAEIOU'
    
    reversed_array = []
    
    for i in range(len(split_array)):
        if len(split_array[i]) > 1 and not all(char in VOWELS for char in split_array[i]): 
            index = split_array[i][::-1] # dar vuelta el string
            reversed_array.append(index) # agregarlo al nuevo array
        else:
            reversed_array.append(split_array[i])

    joined_array = ''.join(reversed_array)

    return joined_array    

# 05. Separar palabra en 2 arrays
def divideArr(joined_array):
    joined_array = list(joined_array)
    
    first_half = joined_array[0:int(len(joined_array)/2)]
    second_half = joined_array[int(len(joined_array)/2):len(joined_array)]
    
    second_half_reversed = second_half.reverse()

    encripted_array = []
    
    even = 0
    odd = 0
        
    for i in range(len(joined_array)):
        if odd < (len(first_half)):
            
            if i % 2 == 0:
                encripted_array.append(first_half[even])
                even += 1
            else:
                encripted_array.append(second_half[odd])
                odd += 1
        else:
            encripted_array.append(second_half[odd])
    
    encripted_array = ''.join(encripted_array)
    
    return encripted_array


def main():
    
    action = defineAction()
    
    if action == 'E':
        phrase = createPhrase()
        underscore_array = addUnderscores(phrase)
        split_array = splitArr(underscore_array)
        joined_array = reverseArr(split_array)
        encripted_array = divideArr(joined_array)
        print(encripted_array)
    else:
        phrase = createPhrase()        
        encripted_array = divideArr(phrase)
        
main()




































