# PRÁCTICA 03

#-----------------------------------------Ejercicio 1----------------------------------------------------------
# Escribir una función que reciba una cadena que contiene un número entero largo y 
# devuelva una cadena con el número y las separaciones de miles. Por ejemplo, si recibe 
# ’1234567890’, debe devolver ’1.234.567.890’.

# def createNumber():
#     return input('Ingrese un número entero: ')


# def separateThousands(number):
    
#     number = number[::-1]
#     final_number = ''
    
#     for i in range(len(number)):
#         if i % 3 == 0 and i != 0:
#             final_number += '.' + number[i]
#         else:
#             final_number += number[i]            

#     final_number = final_number[::-1]    

#     print(final_number)                    

# def main():
#     number = createNumber()
#     separateThousands(number)
    
# main()


# frase = "Hola como estas"

# frase = frase[::-1]
# print(frase)

lista = ["Hola","Como","Estas"]
# numero = 43957834985

# print(lista[::-1])
# print(str(numero)[::-1])

# lista.pop(0)

lista[::1]
print(lista)

#-----------------------------------------Ejercicio 2----------------------------------------------------------

# Una palabra es "alfabética" si todas sus letras están ordenadas alfabéticamente. Por
# ejemplo, "amor", "chino" e "himno" son palabras "alfabéticas". Diseña un programa que lea
# una palabra y nos diga si es alfabética o no.
# amor (T)
# chinardo (F)

# def createWord():
#     return input('Ingrese una palabra: ')

# def isAlphabetic(word):
#     for i in range(len(word)-1):
#         if ord(word[i]) > ord(word[i+1]):
#             return False
#     return True

# def printIsAlphabetic(word,is_alphabetic):
#     if is_alphabetic:
#         print(f"La palabra '{word}' es alfabética")
#     else:
#         print(f"La palabra '{word}' no es alfabética")
    
# def main():
#     word = createWord()
#     is_alphabetic = isAlphabetic(word)
#     printIsAlphabetic(word,is_alphabetic)
    
# main()

#-----------------------------------------Ejercicio 3----------------------------------------------------------

# Hay un tipo de pasatiempos que propone descifrar un texto del que se han suprimido
# las vocales. Por ejemplo, el texto ".n .j.mpl. d. p.s.t..mp.s", se descifra sustituyendo cada
# punto con una vocal del texto. La solución es "un ejemplo de pasatiempos". Diseña un
# programa que ayude al creador de pasatiempos. El programa recibirá una cadena y 
# mostrará otra en la que cada vocal ha sido reemplazada por un punto.    

# def createText():
#     return input('Ingrese un texto: ')

# def replaceVowels(text):
#     vowels = 'aeiouAEIOU'
#     replaced_vowels = ''
    
#     for letter in text:
#         if letter in vocals:
#             replaced_vowels += '.'
#         else:
#             replaced_vowels += letter

#     print(replaced_vowels)

# def main():
#     text = createText()
#     replaceVowels(text)
    
# main()

#-----------------------------------------Ejercicio 4---------------------------------------------------------

# Haz un programa que lea dos cadenas que representen sendos números binarios. A
# continuación, el programa mostrará el número binario que resulta de sumar ambos (y que 
# será otra cadena). Si, por ejemplo, el usuario introduce las cadenas ’100’ y ’111’, el 
# programa mostrará como resultado la cadena ’1011’.
# Nota: El procedimiento de suma con acarreo que implementes deberá trabajar 
# directamente con la representación binaria leída.
# 100 / 4
# 111 / 7
# --> 1011 / 11

# ------------------------- FORMA MÍA

# # # Input binary numbers that will be converted to int
# def binaryToInt():
#     int_number = int(input("Ingrese un número binario: "),2)
#     return int_number

# # # Sum both int and convert them to binary
# def intToBinary(first_binary,second_binary):
#     print(bin(first_binary + second_binary)[2:]) # 4 + 7 = 11 (1011)

# def main():
#     first_binary = binaryToInt() # 100 = 4
#     second_binary = binaryToInt() # 111 = 7
    
#     intToBinary(first_binary,second_binary)
    
# main()

# ------------------------- FORMA DIANA

##def completarConCeros(a,b):
##    if len(a) > len(b):
##        cant = len(a) - len(b)
##        b = '0'*cant +b
##    else:
##        cant = len(b) - len(a)
##        a = '0' * cant + a
##    return a,b
##
##def sumaBin(a,b):
##    a,b = completarConCeros(a,b)
##    a = a[::-1]
##    b = b[::-1]
##    c = ""
##    acarreo = 0
##    for x,y in zip(a,b):
##        x = int(x)
##        y = int(y)
##        aux = x + y + acarreo
##        if aux == 0:
##            c = c + '0'
##            acarreo = 0
##        elif aux == 1:
##            c = c + '1'
##            acarreo = 0
##        elif aux == 2:
##            c = c + '0'
##            acarreo = 1
##        else:
##            c = c + '1'
##            acarreo = 1
##    if acarreo == 1:
##        c = c + '1'
##    return c[::-1]
##        
###programa principal
##a = input("nro binario: ")
##b = input("nro binario: ")
##print(sumaBin(a,b))
##a,b = completarConCeros(a,b)
##print(a,b)

#-----------------------------------------Ejercicio 5----------------------------------------------------------

# Escribir un programa que verifique si un string es una password correcta. Las reglas para 
# determinar si es correcta son:
# Debe tener como mínimo 8 caracteres.
#  Sólo puede tener letras y dígitos.
# Como mínimo debe tener dos dígitos.

# def createPassword():
#     return input('Ingrese una contraseña: ')

# def isLengthOk(password):
#     if len(password) < 8:
#         print(f'La contraseña debe tener como mínimo 8 caracteres')
#         return False
#     return True

# def hasLettersAndDigits(password):
    
#     if not password.isalnum():
#         print(f'La contraseña debe ser alfanumérica')
#         return False
#     return True


# def hasDigits(password):
#     digits = 0
#     for character in password:
#         if character.isdigit():
#             digits += 1
    
#     if digits < 2:
#         print(f'La contraseña debe tener al menos 2 dígitos')
#         return False
#     return True

# def isPasswordValid(password):
#     while not isLengthOk(password) or not hasLettersAndDigits(password) or not hasDigits(password):
#         password = createPassword()
    
#     print(f'La contraseña "{password}" es válida')

# def main():
#     password = createPassword()
#     isPasswordValid(password)    

# main()

#-----------------------------------------Ejercicio 6----------------------------------------------------------

# Escribir un programa que retorne el número que le corresponde a una letra en mayúscula 
# de acuerdo al teclado telefónico (ver figura):

# def createLetter():
#     return input('Ingrese una letra: ').lower()

# def evaluateLetter(letter):
#     dic = {
#             2: 'abc',
#             3: 'def',
#             4: 'ghi',
#             5: 'jkl',
#             6: 'mno',
#             7: 'pqrs',
#             8: 'tuv',
#             9: 'wxyz'
#             }
    
#     for i in range(2,10):
#         if letter in dic[i]:
#             print(f'A la letra "{letter.upper()}" le corresponde el número {i}')
        
# def main():
    
#     letter = createLetter()
#     evaluateLetter(letter)
    
# main()
    
#-----------------------------------------Ejercicio 7----------------------------------------------------------

# Escribir un programa que ingrese un número telefónico como un string y convierta los
# caracteres al dígito correspondiente, ejemplo:
#  1-800-FLOWERS ---> 1-800-3569377

# def createNumber():
#     return input('Ingrese un número telefónico: ')

# def evaluateNumber(number):
    
#     dic = {
#             2: 'abc',
#             3: 'def',
#             4: 'ghi',
#             5: 'jkl',
#             6: 'mno',
#             7: 'pqrs',
#             8: 'tuv',
#             9: 'wxyz'
#             }
    
#     final_number = ''
    
#     for digit in number:
#         if digit.isalpha():
#             for i in range(2,10):
#                 if digit.lower() in dic[i]:
#                     final_number += str(i)
#         else:
#             final_number += digit
            
#     print(final_number)
    
# def main():
#     number = createNumber()
#     evaluateNumber(number)

# main()

#-----------------------------------------Ejercicio 8----------------------------------------------------------

# Un ISBN-10 (International Standard Book Number) consiste de 10 dígitos: 
# d1d2d3d4d5d6d7d8d9d10.
# El último dígito, d10, es el dígito verificador que se calcula como sigue:
# (d1 * 1 + d2 * 2 + d3 * 3 ...) % 11 ---> si da 10, se pone x. Sino, la cuenta.
# Si el dígito verificador es 10, el último dígito es x, de acuerdo a las normas ISBN. Escribir 
# un programa que permita ingresar los primeros 9 dígitos como una cadena y muestre el 
# número ISBN.
# 013601267 ---> 0136012671
# 013031997 ---> 013601267X

# def createSequence():
#     return input('Ingrese una secuencia: ')

# def sumDigits(sequence):
#     suma = 0
    
#     for i in range(len(sequence)):
#         suma += int(sequence[i]) * (i+1)

#     return suma

# def calculateLastDigit(sequence,suma):
#     new_sequence = sequence
    
#     if suma % 11 == 10:
#         new_sequence += 'X'
#     else:
#         new_sequence += str(suma%11)

#     print(f'{sequence} ---> {new_sequence}')

# def main():
#     sequence = createSequence()
#     suma = sumDigits(sequence)
#     calculateLastDigit(sequence,suma)

# main()

#-----------------------------------------Ejercicio 9----------------------------------------------------------

# ISBN-13 es un nuevo estandar para identificar libros. Usa 13 dígitos: 
# d1d2d3d4d5d6d7d8d9d10d11d12d13 .
# El último dígito, es el dígito verificador y se calcula con la siguiente fórmula:
# 10 - (d1 + 3 d2 + d3 + 3d4 ...) % 10      
# Si el dígito verificador es 10 se reemplaza por 0. El programa deberá permitir ingresar un 
# número como un string y mostrar el ISBN-13, ejemplo:
# 978013213080 ---> 9780132130806
# 978013213079 ---> 9780132130790

# def createSequence():
#     return input('Ingrese una secuencia: ')

# def calculateSum(sequence):
    
#     suma = 0
    
#     for i in range(len(sequence)):
#         if i % 2 == 0:
#             suma += int(sequence[i])
#         else:
#             suma += int(sequence[i]) * 3

#     return suma

# def calculateLastDigit(sequence,suma):
#     new_sequence = sequence

#     if 10 - (suma % 10) == 10:
#         new_sequence += '0'
#     else:
#         new_sequence += str(10 - (suma % 10))
        
#     print(f'{sequence} ---> {new_sequence}')

# def main():
#     sequence = createSequence()
#     suma = calculateSum(sequence)
#     calculateLastDigit(sequence,suma)

# main()

#-----------------------------------------Ejercicio 10----------------------------------------------------------

# Escribir un programa que permita ingresar un texto y un caracter e imprima la palabra 
# más larga en la que se encuentra ese carácter.
# Me gustan las majesties

# def createText():
#     return input('Ingrese una frase: ')

# def createCharacter():
#     return input('Ingrese el caracter a evaluar: ')

# def defineLongestWord(character,text):
    
#     separated_text = text.split()
    
#     longest = separated_text[0]
    
#     for i in range(len(separated_text)):
#         if character in separated_text[i] and len(separated_text[i]) > len(longest):
#           longest = separated_text[i]
    
#     print(f'La palabra más larga en "{text}" con el caracter "{character}" es "{longest}"')

# def main():
#     text = createText()
#     character = createCharacter()
#     defineLongestWord(character,text)

# main()

#-----------------------------------------Ejercicio 11----------------------------------------------------------

# La ley de Chargaff dice que en el ADN de un organismo la cantidad de Adenina es la 
# misma que la de Tiamina, y la de Citosina es la misma que la de Guanina. Dada una 
# secuencia de nucleótidos del estilo de ATTACCAGTACA... podemos comprobar si cumple
# dicha ley de la siguiente forma:
# Contamos la cantidad de A, T, C y G presentes en la cadena y calculamos los coeficientes
# donde NX indica la cantidad de nucleótidos del tipo X presentes en la secuencia.
# Partiremos de una cadena que contiene una cantidad indeterminada de caracteres, que 
# solo pueden ser A, T, G ó C. Calcula a partir de dicha cadena los coeficientes a y c.

# def createSequence():
#     return input('Ingrese una secuencia: ').upper()

# def charactersOK(sequence):    
#     letters = 'ATGC'
    
#     for letter in sequence:
#         if letter not in letters:
#             return False
#     return True

# def countLetters(sequence):
#     dic = {
#         'A': 0,
#         'T': 0,
#         'G': 0,
#         'C': 0        
#         }

#     for i in range(len(sequence)):
#         if sequence[i] in dic.keys():
#             dic[sequence[i]] += 1
            
#     return dic
    
# def calculateCoefAnC(sequence,dic):
    
#     a = (dic['A'] - dic['T']) / (dic['A'] + dic['T'])
#     c = (dic['C'] - dic['G']) / (dic['C'] + dic['G'])

#     print(f'\nLos coeficientes de la cadena "{sequence}" son\na ---> {a:.2f}\nc ---> {c:.2f}')    

# def main():
#     sequence = createSequence()    
#     are_characters_ok = charactersOK(sequence)
    
#     while not are_characters_ok:
#         sequence = createSequence()    
    
#     dic = countLetters(sequence)
#     calculateCoefAnC(sequence,dic)

# main()

#-----------------------------------------Ejercicio 12----------------------------------------------------------

# Escribe un programa que lea dos cadenas y devuelva el prefijo común más largo de
# ambas. Ejemplo: las cadenas "politécnico" y "polinización" tienen como prefijo común más
# largo a la cadena "poli".
# politécnico / polinización = poli

# def createWord1():
#     return input('Ingrese la primera palabra: ').lower()

# def createWord2():
#     return input('Ingrese la segunda palabra: ').lower()

# def shortestWord(word1,word2):
#     shortest = word1
#     if len(word2) < len(word1):
#         shortest = word2
        
#     return shortest

# def findCommonPrefix(word1,word2,shortest):
#     shortest_prefix = ''

#     for i in range(len(shortest)):
#         if word1[i] == word2[i]:
#           shortest_prefix += word1[i]  
    
#     print(f'The shortest prefix for words "{word1}" and "{word2}" is "{shortest_prefix}"')   
    
    
# def main():
#     word1 = createWord1()
#     word2 = createWord2()
#     shortest_word = shortestWord(word1,word2)
#     findCommonPrefix(word1,word2,shortest_word)
    
# main()
    
#-----------------------------------------Ejercicio 13----------------------------------------------------------

# Necesitamos buscar en diversas secuencias de ARN las posibles apariciones del codón 
# iniciador 'AUG', que marca el inicio de un gen. Como en una secuencia de ARN puede 
# haber más de un gen, deseamos conocer todas las posiciones en las que aparece dicho 
# codón. Para ello elaboraremos un programa que ingresará una cadena de caracteres que 
# representa una secuencia de ARN y comprobará que la secuencia de ARN contiene 
# únicamente los caracteres 'A','U','G' ó 'C'. En caso contrario, la secuencia es inválida y se 
# deberá imprimir un mensaje adecuado.
# AUGAGCGAGAUGCUA ---> [0,9]

# def createSequence():
#     return input('Ingrese una secuencia: ').upper()

# def charactersOK(sequence):
#     letters = 'AUGC'
    
#     for character in sequence:
#         if character not in letters:
#             return False
#     return True

# def findGene(sequence):
    
#     positions = []
    
#     for i in range(len(sequence)):
#         if i < len(sequence)-2:
#             if sequence[i] == 'A' and sequence[i+1] == 'U' and sequence[i+2] == 'G':
#                 position = [i,i+1,i+2]
#                 positions.append(position)
                
#     return positions

# def numberOfGenes(sequence,positions):
#     if len(positions) > 0:
#         print(f'Las posiciones donde hay un codón "AUG" en la secuencia ARN "{sequence}" son {positions}')
#     else:
#         print(f'En la secuencia de ARN "{sequence}" no hay codones "AUG"')

# def main():
#     sequence = createSequence()
    
#     while not charactersOK(sequence):
#         print("La secuencia ingresada contiene caracteres inválidos, vuelva a ingresar una nueva secuencia: ")
#         sequence = createSequence()
    
#     positions = findGene(sequence)
#     numberOfGenes(sequence,positions)

# main()

#-----------------------------------------Ejercicio 14----------------------------------------------------------

# Los biólogos usan una secuencia de letras A, C, T, y G para modelar un genoma. Un gen es
# una subcadena de un genoma que comienza después de la tripleta ATG y termina con una 
# tripleta TAG, TAA, ó TGA. La longitud de una cadena de gen es un múltiplo de 3 y el gen 
# no contiene a las tripletas ATG, TAG, TAA y TGA. Escribir un programa que permita 
# ingresar un genoma y muestre todos los genes en el genoma. Si en la cadena no se 
# encuentran genes, el programa mostrará un mensaje acorde. Ejemplo: 
# si la cadena es TTATGTTTTAAGGATGGGGCGTTAGTT, el programa mostrará:
# TTT
# GGGCGT
# Si la cadena es TGTGTGTATAT entonces se deberá mostrar "no se encontraron genes".

def createSequence():
    return input('Ingrese una secuencia: ').upper()

def evaluateSequence(sequence):
    start = 'ATG'
    end = ['TAG','TAA','TGA']
    
    sequence = sequence.split('ATG')
    print(f"sequence: {sequence}")
    new_sequence = []
    
    for i in range(len(sequence)):
        for j in range(len(end)):
            if end[j] in sequence[i]:
                new_sequence.append(sequence[i].split(end[j])[0])

    return new_sequence
    
def hasGenes(sequence,new_sequence):
    if len(new_sequence) > 0:
        print(f'La secuencia "{sequence}" tiene los genes {new_sequence}')
    else:
        print(f'La secuencia "{sequence}" no tiene genes')

def main():
    sequence = createSequence()
    new_sequence = evaluateSequence(sequence)
    hasGenes(sequence,new_sequence)
main()

#-----------------------------------------Ejercicio 15----------------------------------------------------------

# Dos palabras son anagramas si tienen las mismas letras pero en otro orden. Por ejemplo, 
# «torpes» y «postre» son anagramas, mientras que «aparta» y «raptar» no lo son, ya que 
# «raptar» tiene una r de más y una a de menos.
# Escriba la función sonAnagramas(p1, p2) que indique si las palabras p1 y p2 son 
# anagramas:
# sonAnagramas('torpes', 'postre') ---> True
# sonAnagramas('aparta', 'raptar') ---> False

# def createWord1():
#     return input('Ingrese la primera palabra: ')

# def createWord2():
#     return input('Ingrese la segunda palabra: ')

# def evaluateWords(word1,word2):
#     word1_sorted = sorted(word1)
#     word2_sorted = sorted(word2)

#     print(f'"{word1}" y "{word2}" son anagramas ---> {word1_sorted == word2_sorted}')

# def main():
#     word1 = createWord1()
#     word2 = createWord2()
#     evaluateWords(word1,word2)

# main()

#-----------------------------------------Ejercicio 16----------------------------------------------------------

# Las palabras panvocálicas son las que tienen las cinco vocales. Por ejemplo: centrifugado, 
# bisabuelo, hipotenusa. Escriba la función esPanvocalica(palabra) que indique si una 
# palabra es panvocálica o no:
# esPanvocalica('educativo') ---> True
# esPanvocalica('pedagogico') ---> False

# def createWord():
#     word = input("Ingrese una palabra: ").lower()
#     return word

# def esPanvocalica(word):
#     panvocalica = False
#     vowels = set('aeiou')
#     if vowels.issubset(word):
#         panvocalica = True
#         print(f"'{word}' ---> {panvocalica}")
#     else:
#         print(f"'{word}' ---> {panvocalica}")

# def main():
#     word = createWord()
#     esPanvocalica(word)
    
# main()


 


