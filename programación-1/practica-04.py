# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 11:19:44 2023

@author: Gemdelle
"""

# PRÁCTICA 04

#-----------------------------------------Ejercicio 1----------------------------------------------------------
# Ver imagen

# Ejercicio 1:
# Escribir funciones que, tomando como entrada una lista de números enteros, decida si la
# lista:
#   ● está ordenada crecientemente.
#   ● está ordenada decrecientemente.
#   ● es gaspariforme. Se dice que un lista de n elementos es gaspariforme si todas sus
# sumas parciales son no negativas, y la suma total es igual a 0. Las sumas parciales son la suma de los números acumulados

# Ejemplo:
# Si a = [ 10, 5, 2, 20, 6], n = 5
# s0 = 10
# s1 = 10 + 5 = 15
# s2 = 10 + 5 + 2 = 15 + 2 = 17
# s3 = 10 + 5 + 2 + 20 = 17 + 20 = 37
# s4 = 10 + 5 + 2 + 20 + 6= 17 + 20 + 6 = 37 + 6 = 43
#   ● es melchoriforme. Se dice que una lista es melchoriforme si alguno de sus elementos es
# un centro . Un elemento es un centro si su valor coincide con la suma de los otros
# elementos de la lista.

# [5, 4, 3, 2, 1] ---> es decreciente
# [5, 4, 3, 2, 1, -1, -2, -3, -4, -5] ---> es decreciente y es gaspariforme
# [1, 2, 3, 4] ---> es creciente
# [5, 4, 3, 2, 1, -1, 1, -2, -3, -4, -5] ---> no es decreciente y no es gaspariforme
# [1, 2, 3, 4, 10] ----> es creciente y es melchoriforme

# def createSequence():
#     sequence = input("Ingrese una secuencia con números separados por coma: ")
#     sequence = sequence.split(',')    
#     for number in range(0,len(sequence)):
#         sequence[number] = int(sequence[number])
#     return sequence

# def esCreciente(sequence):
#     result = True
#     for i in range(0,len(sequence)-1):
#         if sequence[i] > sequence[i+1]:
#             result = False
#     return result
    
# def esDecreciente(sequence):
#     result = True
#     for i in range(0,len(sequence)-1):
#         if sequence[i] < sequence[i+1]:
#             result = False
#     return result
    
# def esGaspariforme(sequence):
#     sum = 0
#     for i in range(0,len(sequence)):
#         sum += int(sequence[i])
#         if sum < 0:
#             return False
    
#     if sum != 0:
#         return False
#     return True

# def esMelchoriforme(sequence):
#     sum = 0
#     melchoriforme = False
#     for i in range(0,len(sequence)):
#         sum += int(sequence[i])
#         if sum == sequence[i]:
#             melchoriforme = True
#     return melchoriforme

# def main():    
#     sequence = createSequence() 
#     creciente = esCreciente(sequence)
#     decreciente = esDecreciente(sequence)    
#     gaspariforme = esGaspariforme(sequence)
#     melchoriforme = esMelchoriforme(sequence)
        
#     print(f'Secuencia ---> {sequence}\nCreciente ---> {creciente}\nDecreciente ---> {decreciente}\nGaspariforme ---> {gaspariforme}\nMelchoriforme ---> {melchoriforme}')

# main()

# -----------------------------------------Ejercicio 2----------------------------------------------------------
# Ver imagen

# Dada una matriz de n x m elementos (una lista que contiene n listas de tamaño m) donde
# cada fila representa una cadena de ADN de longitud m como la siguiente:
# Obtener otra matriz de la siguiente forma:
# Donde en cada fila tenemos la cantidad de repeticiones de cada letra por columnas que
# forma un codón, además obtener una lista donde se muestra por columnas cuál es el
# símbolo que se repite más veces, para el ejemplo anterior se tiene como resultado:

# ATCCAGCT
# GGGCAACT
# ATGGATCT
# AAGCAACC
# TTGGAACT
# ATGCCATT
# ATGGCACT
# ATCCAGCT,GGGCAACT,ATGGATCT,AAGCAACC,TTGGAACT,ATGCCATT,ATGGCACT

# def inputDNA():
#     return input('Ingrese una serie de 7 cadenas de ADN separadas por ",": ').upper()

# def printDNASequence(sequence):
#     separated_sequence = sequence.split(',')
#     filas = len(separated_sequence)
#     columnas = len(separated_sequence[0])

#     print('\nDNA Strings')
#     print()
#     for i in range(filas):
#         for j in range(columnas):
#             print(separated_sequence[i][j], sep=' ', end=' ')
#         print()

#     print()
#     return separated_sequence


# def evaluateDNASequence(sequence):
#     a = []
#     c = []
#     g = []
#     t = []
#     filas = len(sequence)
#     columnas = len(sequence[0])

#     for i in range(columnas):
#         a_count = 0
#         c_count = 0
#         g_count = 0
#         t_count = 0

#         for j in range(filas):
#             if sequence[j][i] == 'A':
#                 a_count += 1
#             elif sequence[j][i] == 'C':
#                 c_count += 1
#             elif sequence[j][i] == 'G':
#                 g_count += 1
#             elif sequence[j][i] == 'T':
#                 t_count += 1

#         a.append(a_count)
#         c.append(c_count)
#         g.append(g_count)
#         t.append(t_count)

#     # agregar letra en el index 0 para imprimir
    
#     a.insert(0,'A')
#     c.insert(0,'C')
#     g.insert(0,'G')
#     t.insert(0,'T')
    
#     print('Profile\n')
    
#     for char in a:
#         print(char,end=' ')
#     print()
        
#     for char in c:
#         print(char,end=' ') 
#     print()
    
#     for char in g:
#         print(char,end=' ')
#     print()
        
#     for char in t:
#         print(char,end=' ')
#     print('\n')

#     # borrar letra en el index 0 para usarlo en la otra función
#     a.remove('A')
#     c.remove('C')
#     g.remove('G')
#     t.remove('T')

#     return [a, c, g, t]


# def mostRepeatedNumber(column_repetition):
#     letters = []
#     highest_value = 0
#     highest_letter = ''
#     filas = len(column_repetition)
#     columnas = len(column_repetition[0])

#     dic = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}
#     for i in range(columnas):
#         for j in range(filas):
#             if column_repetition[j][i] > highest_value:
#                 # Save provisory highest value and letter
#                 highest_value = column_repetition[j][i]
#                 highest_letter = dic[j]

#         letters.append(highest_letter)
#         #Reset values for next column
#         highest_value = 0
#         highest_letter = ''

#     print('Consensus\n')
#     for letter in letters:
#         print(letter,end=' ')

# def main():
#     sequence = inputDNA()
#     separated_sequence = printDNASequence(sequence)
#     column_repetition = evaluateDNASequence(separated_sequence)
#     mostRepeatedNumber(column_repetition)

# main()

#-----------------------------------------Ejercicio 3----------------------------------------------------------
# Diseñar una función que determine si una lista de números enteros está ordenada de
# menor a mayor y cada número i entre 1 y n aparece exactamente i veces.
# Ejemplo:
# para n = 5
# esTelescopio(5,[1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]) --> verdadero

# def createNumber():
#     number = int(input('Ingrese el número a evaluar: '))
#     return number 

# def createSequence():
#     sequence_input = input("Ingrese una secuencia de números: ")
#     sequence = []
    
#     for number in sequence_input:
#         sequence.append(int(number))
        
#     return sequence
    
# def inOrder(sequence):
#     return sequence == sorted(sequence)
    
# def esTelescopio(number,arr):
    
#     if not inOrder(arr):
#         print(f'El array {arr} no está en orden\n--------------------------------------------------------------')
#         return False
    
#     index = len(arr) - list(reversed(arr)).index(number) -1
#     # print(index,arr) // chequear la posición en la que tiene que terminar de evaluar
    
#     for i in range(1,arr[index]):
#         if arr.count(i) != i:
#             return False
#     return True
    
# def main():
#     number = createNumber()
#     sequence = createSequence()
    
#     es_telescopio = esTelescopio(number,sequence)
    
#     print(f'--------------------------------------------------------------\n{number} <-> {sequence} ---> {es_telescopio}')
    
# main()

#-----------------------------------------Ejercicio 4----------------------------------------------------------

# Ejercicio 4:
# Diseñar una función que genere una lista en forma de telescopio .
# Ejemplo: genTelescopio(5) --> [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]

# def inputNumber():
#     return int(input('Ingrese un número: '))

# def genTelescopio(number):
#     arr = []

#     for i in range(0,number+1):
#         while arr.count(i) < i:
#             arr.append(i)
    
#     print(arr)
    
# def main():
#     number = inputNumber()
#     genTelescopio(number)
    
# main()

#-----------------------------------------Ejercicio 5----------------------------------------------------------

# Ejercicio 5:
# Diseñar una función que determine si una lista de números enteros, cada número i entre 1
# y n aparece i veces consecutivas.
# Ejemplo: sonConsecutivos(5,[3,3,3,1,2,2,5,5,5,5,5,4,4,4,4]) --> verdadero

# 33312255555444 --> falso - falta un 4
# 333122555554444 --> verdadero

# def inputNumber():
#     return int(input('Ingrese un número: '))

# def inputArr():    
#     return input('Ingrese una cadena de números: ')

# def arrToInt(arr):
    
#     new_arr = []
    
#     for i in range(0,len(arr)):
#         new_arr.append(int(arr[i]))
#     return new_arr

# def sonConsecutivos(number,arr):
#     consecutive = True
    
#     for i in range(number+1):
#         if arr.count(i) < i:
#             consecutive = False
    
#     print(f'{number} {arr} ---> {consecutive}')
    
#     return consecutive

# def main():
#     number = inputNumber()
#     arr = inputArr()
#     arr = arrToInt(arr)
#     sonConsecutivos(number,arr)
# main()

#-----------------------------------------Ejercicio 6----------------------------------------------------------

# Ejercicio 6:
# Diseña una función que reciba una lista de cadenas y devuelva el prefijo común más
# largo. Por ejemplo, la cadena "pol" es el prefijo común más largo de esta lista:
# [’poliedro’, ’policia’, ’polifona’, ’polinizar’, ’polaridad’, ’politica’]

# poliedro,policia,polifona,polinizar,polaridad,politica

# def inputWords():
#     words = input('Ingrese una secuencia de palabras separadas por ",": ')
#     return words.split(',')

# def commonPrefix(words):     # Esta función recibe un array de strings como parámetros.
#     prefix_evaluation = []
#     prefix = []
#     first_word = words.pop(0)

#     #poliedro ['policia', 'polifona', 'polinizar', 'polaridad', 'politica']

#     for word in words: # Retorna cada palabra en words.    Ej:  'polifona'...'polinizar'
#         prefix_evaluation = []
#         for i in range(len(word)):    # Iteramos el largo de esa palabra  Ej: 'polifona' del 0 al 7              || Ej. 'polinizar' del 0 al 8
#             if i < len(first_word):   # Si i menor que el largo de la primer palabra Ej. i < 7, itera de 0 a 6   || Ej. i < 7, itera del 0 a 6
#                 if word[i] == first_word[i]:  # Si las letras son iguales                                        || Si son iguales
#                     prefix_evaluation.append(word[i]) # Meto las letras aca ['p','o','l','i']                    || metemos las palabras
#         # Bien seguimos aca luego de completar prefix_evaluation = ['p','o','l','i']                             || Quedaria prefix_evaluation = ['p','o','l','i','poli','p','o','l','i']
        
#         joined_prefix_evaluation = ''.join(prefix_evaluation)  # joined_prefix_evaluation = 'poli'               || joined_prefix_evaluation = 'polipolipoli' 
#         prefix.append(joined_prefix_evaluation)
#         joined_prefix_evaluation = ''                          # joined_prefix_evaluation = ''                   || joined_prefix_evaluation = ''
#     # Todo esto para la primer palabra 'polifona', ahora viene el siguiente bucle con 'polinizar'                || Sigue el bucle con la siguiente palabra
    
#     return prefix

# def longestPrefix(words):
    
#     prefix_list = commonPrefix(words)
    
#     shortest_prefix = prefix_list[0]
    
#     for i in range(len(prefix_list)):
#         if len(prefix_list[i]) < len(shortest_prefix):
#             shortest_prefix = prefix_list[i]
            
#     print(f'\nEl prefijo más largo es "{shortest_prefix}"')
        

# def main():
#     words = inputWords()
#     longestPrefix(words)

# main()

#-----------------------------------------Ejercicio 7----------------------------------------------------------

# La ciudad de Babilonia tiene una alta congestión de vehículos circulando por sus calles.
# Las autoridades han decidido aplicar restricción vehicular para descongestionar la ciudad
# en base a las patentes de los vehículos.
# La patente de un vehículo es un string de cuatro letras y dos dígitos, y la restricción
# depende sólo del penúltimo dígito. Por ejemplo, para la patente GEEA78, el dígito 7 es el
# utilizado para evaluar la restricción.
# La restricción vehícular de los días hábiles de la semana se encuentra ingresada en el
# diccionario digitos, cuyas llaves son los días de la semanas, y cuyos valores son tuplas de
# cuatro enteros que representan los dígitos con restricción de ese día.
# Implemente la función estaConRestriccion(digitos,dia, patente), que indique si el
# vehículo está o no con restricción.
# • Implemente la función diasConRestriccion(digitos,patente), que retorne la lista de
# los días en que el vehículo no puede circular.
# • Implemente la función diasSinRestriccion(digitos,patente), que retorne el conjunto
# de los días en que el vehículo sí puede circular.
# digitos = {'lunes': (3, 4, 5, 6), 'martes': (7, 8, 9, 0),...,'miercoles': (1, 2, 3, 4), 'jueves':
#  (5, 6, 7, 8), ... , 'viernes': (9, 0, 1, 2)}
# estaConRestriccion(digitos, 'lunes', 'BBDT35') ---> True
# diasConRestriccion(digitos, 'BBDT35') ---> ['lunes', 'miercoles']
# diasSinRestriccion(digitos, 'BBDT35') ---> set(['jueves', 'martes', 'viernes'])

# E//0
# BBDT35 = Días con restricción = BBDT35 ---> ['lunes', 'miercoles'] Días sin restricción = BBDT35 ---> ['martes', 'jueves', 'viernes'] Restricción el día jueves = BBDT35 ---> False


# def createRegistrationPlateAndDay():
#     patente = input("Ingrese una patente: ")
#     day = input("Ingrese un día de la semana: ")
#     return patente,day

# def registrationPlateDigit(plate):    
#     patente = list(plate)
#     return int(patente.pop(4))

# def estaConRestriccion(digitos,day,plate):
    
#     digit_pat = registrationPlateDigit(plate)
    
#     esta_con_restriccion = False
    
#     for key in digitos:
#         if day == key:
#             if digit_pat in digitos[key]:
#                 esta_con_restriccion = True
    
#     print(f'Restricción el día {day} = {plate} ---> {esta_con_restriccion}')

# def diasConRestriccion(digitos,plate):
    
#     digit_pat = registrationPlateDigit(plate)
    
#     restriction_days = []
    
#     for key in digitos:
#         if digit_pat in digitos[key]: 
#             restriction_days.append(key)
    
#     print(f'Días con restricción = {plate} ---> {restriction_days}')
    
# def diasSinRestriccion(digitos,plate):
    
#     digit_pat = registrationPlateDigit(plate)
    
#     no_restriction_days = []
    
#     for key in digitos:
#         if digit_pat not in digitos[key]: 
#             no_restriction_days.append(key)
    
#     print(f'Días sin restricción = {plate} ---> {no_restriction_days}')

# def main():
#     digitos = {'lunes': (3, 4, 5, 6), 'martes': (7, 8, 9, 0),'miercoles': (1, 2, 3, 4), 'jueves':
#       (5, 6, 7, 8), 'viernes': (9, 0, 1, 2)}
    
#     patente,day = createRegistrationPlateAndDay()
    
#     diasConRestriccion(digitos,patente)
#     diasSinRestriccion(digitos,patente)
#     estaConRestriccion(digitos,day,patente)
    
# main()

#-----------------------------------------Ejercicio 8----------------------------------------------------------

# La empresa RawInput S.A. desea hacer una clasificación de sus clientes según su ubicación
# geográfica. Para esto, analizará su base de datos de correos electrónicos con el fin obtener
# información sobre el lugar de procedencia de cada cliente.
# En una dirección de correo electrónico, el dominio es la parte que va después de la arroba,
# y el TLD es lo que va después del último punto. Por ejemplo, en la dirección
# fulano.de.tal@alumnos.usm.cl, el dominio es alumnos.usm.cl y el TLD es cl.
# Algunos TLD no están asociados a un país, sino que representan otro tipo de entidades.
# Estos TLD genéricos son los siguentes:
# genericos = {'com', 'gov', 'edu', 'org', 'net', 'mil'}
# 1. Escriba la función obtenerDominios(correos) que reciba como parámetro una lista
# de correos electrónicos, y retorne la lista de todos los dominios, sin repetir, y en
# orden alfabético.
# 2. Escriba la función contarTld(correos) que reciba como parámetro la lista de correos
# electrónicos, y retorne un diccionario que asocie a cada TLD la cantidad de veces
# que aparece en la lista. No debe incluir los TLD genéricos.
# c = ['fulano@usm.cl', 'erika@lala.de', 'li@zi.cn', 'a@a.net', 'gudrun@lala.de',
# 'otto.von.d@lorem.ipsum.de', 'org@cn.de.cl', 'yayita@abc.cl', 'jozin@baz.cz', 'jp@foo.cl',
# 'dawei@hao.cn', 'pepe@gmail.com', 'ana@usm.cl', 'polo@hotmail.com', 'fer@x.com',
# 'ada@alumnos.usm.cl', 'dj@foo.cl', 'jan@baz.cz', 'd@abc.cl']

# obtenerDominios(c) se obtiene:
# ['abc.cl', 'alumnos.usm.cl', 'baz.cz', 'cn.de.cl', 'foo.cl',
# 'hao.cn', 'lala.de', 'lorem.ipsum.de', 'usm.cl', 'zi.cn']
# contarTld(c) se obtiene: {'cz': 2, 'de': 3, 'cn': 2, 'cl': 8}

# E//0 Solo correr

# def obtenerDominios(correos):
#     dominios = []
    
#     # crear la lista de dominios
#     for i in range(0,len(correos)):
#         dominio = correos[i].split('@')
#         if dominio[1] not in dominios:
#             dominios.append(dominio[1])
        
#     # ordenar alfabéticamente 
#     dominios = sorted(dominios)
    
#     print(f'\nLista de dominios ---> {dominios}\n')    

# def obtenerTld(correos):
#     for i in range(len(correos)):
#         mail_end = correos[i].split('.')
#         correos[i] = mail_end[-1] 
    
#     return correos

# def filtrarTld(correos):
#     genericos = ['com', 'gov', 'edu', 'org', 'net', 'mil']
#     correos = obtenerTld(correos)
#     correos_filtrados = []
    
#     for i in range(len(correos)):
#         if correos[i] not in genericos:
#             correos_filtrados.append(correos[i])
        
#     return sorted(correos_filtrados)

# def contarTld(correos):
#     correos = filtrarTld(correos)
#     dic = {}
    
#     for correo in correos:
#         if correo in dic:
#             dic[correo] += 1
#         else:
#             dic[correo] = 1
    
#     print(f'Diccionario ---> {dic}')

# def main():
#     mails = ['fulano@usm.cl', 'erika@lala.de', 'li@zi.cn', 'a@a.net', 'gudrun@lala.de',
#     'otto.von.d@lorem.ipsum.de', 'org@cn.de.cl', 'yayita@abc.cl', 'jozin@baz.cz', 'jp@foo.cl',
#     'dawei@hao.cn', 'pepe@gmail.com', 'ana@usm.cl', 'polo@hotmail.com', 'fer@x.com',
#     'ada@alumnos.usm.cl', 'dj@foo.cl', 'jan@baz.cz', 'd@abc.cl']
     
#     obtenerDominios(mails)
#     contarTld(mails)
    
# main()

#-----------------------------------------Ejercicio 9----------------------------------------------------------

# Debido a la gran cantidad de crímenes y casos sin resolver, la policía local ha decidido
# implementar su propio sistema de reconocimiento de sospechosos con la técnica basada en
# el uso del DNA.
# Para esto la policía mantiene dos listas de información; la primera contiene el nombre de
# las personas registradas en la región (nombre y apellido), la otra, un cromosoma
# representativo del DNA de cada una de esas personas.
# Por simplicidad, un cromosoma se considera como una cadena de 0 (ceros) y 1 (unos), de
# largo 20.
# El método para determinar el sospechoso, es el siguiente:
# • Se obtiene una muestra del cromosoma del autor del delito (20 caracteres)
# • Se busca en la lista de cromosomas, aquel cromosoma que esmás parecido a la
# muestra. El más parecido se define como el cromosoma que tiene más genes
# (caracteres) iguales a la muestra.
# • Al terminar la búsqueda, se muestra el nombre de la persona cuyo cromosoma es
# sospechoso, con el porcentaje de parentesco.
# La información inicial del programa se debe ingresar directamente en el código, es decir,
# nombres y cromosomas, en cambio la secuencia encontrada en la escena del crimen, debe
# ser ingresada por el usuario.
# Desarrolle un programa que lleve a cabo la búsqueda descrita a partir de una muestra de
# entrada.
# Consideremos, personas como Pedro, Juan y Diego. Sus secuencias serán
# • 00000101010101010101
# • 00101010101101110111|
# • 00100010010000001001
# Ingrese secuencia: 01010101000011001100
# El culpable es Pedro con un parentesco de 60%

# 01100111011001110010 ---> El culpable es ASHLEY con un parentesco del 95%
# 10000101110100101110 ---> El culpable es DIATEWY con un parentesco del 100%

# def createDNASequence():
#     return input("Ingrese una secuencia de DNA: ")

# def evaluateSequence(sequence,suspect_list,dna_list,percentage):
#     coincidence = 0
    
#     for i in range(0,len(dna_list)): # se ingresa a cada cadena de dna_list
#         for j in range(0,len(dna_list[i])): # se ingresa a cada dígito de la cadena que se está evaluando
#             if dna_list[i][j] == sequence[j]: # se iguala el dígito sospechoso al dígito de la secuencia ingresada
#                 coincidence += 1
#         percentage.append(coincidence)
#         coincidence = 0        
        
# def findGuilty(suspect_list,percentage):
#     max_percentage = max(percentage) # el valor de coincidencia más alto
#     percentage_guilt = max_percentage * 5 # sacar porcentaje de parentesco   
#     index_guilty = percentage.index(max_percentage) # encontrar la posición de la mayor coincidencia en arr percentage
#     guilty = (suspect_list[index_guilty]).upper() # buscar en la lista de suspects el que tenga el mismo index
#     print(f'El culpable es {guilty} con un parentesco del {percentage_guilt}%')
    
# def main():
#     suspect_list = ['Ashley', 'Gemy', 'Winnye', 'Cristu', 'Jonytito', 'Diatewy','Osyto']
#     dna_list =  ['01100111011001110011','00011100011100011100','01001110110001110101','00110001001001111010','11010100101110011100','10000101110100101110','01110100100101101010']
#     percentage = []
    
#     sequence = createDNASequence()
#     evaluated_sequence = evaluateSequence(sequence,suspect_list,dna_list,percentage)
#     guilty = findGuilty(suspect_list,percentage)

# main()

#-----------------------------------------Ejercicio 10---------------------------------------------------------

# En el juego ScrabbleTM, cada letra tiene asociado un valor numérico. El puntaje total de una
# palabra es la suma de los valores numéricos de cada letra. Las letras más comunes tienen
# menor valor que las letras menos comunes. Los puntos asociados a cada letra se muestran
# en la siguiente tabla:
# Escribir un programa que calcule y muestre el puntaje de una palabra. Crear un
# diccionario para almacenar la tabla anterior.
# hola ---> 7
# quesardo ---> 18
# majesty ---> 19

# def createWord():
#     return (input("Ingrese una palabra: ")).upper()

# def wordValue(word,tabla):

#     value = 0
#                                               # word = hola
#     for letter in word:                      # itera cada letra, primero 'h', luego 'o', 'l' y 'a'
#         for clave in tabla:                  # itera cada clave en el diccionario primero 1, luego 2, 3, 4, 5, 8, 10
#             if( letter in tabla[clave] ):    # IF substring in string --> if 'h' in 'AEILNORSTU' (true or false)
#                 value += clave               # If true, suma la clave al valor.
#     return value                             # ¡¡¡Consideración!!!, pasar a upper() la word del usuario.

# def main():
#     tabla = { 1: "AEILNORSTU",
#           2: "DG",
#           3: "BCMP",
#           4: "FHVWY",
#           5: "K",
#           8: "JX",
#           10: "QZ"
#         } 
#     word = createWord()
#     value = wordValue(word,tabla)
#     word = word.lower()

#     print(f'Word ---> {word}\nValue ---> {value}')

# main()


















