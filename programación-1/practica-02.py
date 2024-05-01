# PRÁCTICA 02

#-----------------------------------------Ejercicio 1----------------------------------------------------------
# Implementa un programa que muestre todos los múltiplos de 6 entre 6 y 150, ambos
# inclusive.



#---------------------૮( ꒦ິ࿄꒦ີ)ა FORMA 01 ૮( ꒦ິ࿄꒦ີ)ა ---------------------

def defineNumbers(): 
    
    print("Los múltiplos de 6 entre 6 y 150 son: ")
    for i in range(6,151):
        if i % 6 == 0:
            print(i,end =' ')

def main():
    defineNumbers()
    
main()

#-----------------------------------------Ejercicio 2----------------------------------------------------------

# Diseña un programa que solicite la lectura de un número entre 0 y 10 (ambos inclusive).
# Si el usuario teclea un número fuera del rango válido, el programa solicitará nuevamente 
# la introducción del valor cuantas veces sea menester.
# 
def createNumber():
    return int(input('Ingrese un número entre 0 y 10: '))

def evaluateNumber(number):
    while number not in range(0,11):
        print(f'El número "{number}" se encuentra fuera del rango')
        number = createNumber()

    print(f'Él número ingresado es "{number}"')

def main():
    number = createNumber()
    evaluateNumber(number)
    
main()

#-----------------------------------------Ejercicio 3----------------------------------------------------------

# Escribir un programa que muestre, de a diez números por línea y separados por un 
# blanco, todos los números entre 100 y 1000 que sean divisibles por 5 y 6.

def printNumbers():
    
    count = 0
    
    for number in range(100,1001):
        if number % 5 == 0 and number % 6 == 0:
            if count < 9:
                count += 1
                print(number,end=' ')
            else:
                count = 0
                print(number,end=' ')
                print()
                
def main():
    printNumbers()
    
main()

#-----------------------------------------Ejercicio 4---------------------------------------------------------

# Construir un programa que permita multiplicar dos números enteros positivos empleando
# el método denominado multiplicación rusa. Este método permite calcular el producto de N 
# por M de la siguiente forma:
    
# En pasos sucesivos se divide M por 2 (división entera) y se multiplica N por 2. Este 
# proceso se repite hasta que M es 0. El resultado de la multiplicación deseada se obtiene 
# acumulando aquellos valores sucesivos de N para los cuales el valor correspondiente de M
# es impar.
#  Ejemplo: 31 * 27
#  N | M
#  * 31 | 27
#  * 62 | 13
#  124 | 6
#  * 248 | 3
#  * 496 | 1
#  992 | 0
#  Si sumamos los valores marcados con un asterisco (que son los que corresponden a un 
# valor de M impar) obtenemos: 31 + 62 + 248 + 496 = 837 = 31 * 27


def createNumbers():
    n = int(input('Ingrese el primer número: '))
    m = int(input('Ingrese el segundo número: '))

    return n, m

def russianMultiplication(n,m):
    
    mutliplication = n * m
    russian_sum = 0
    
    while m != 0:
        if m % 2 != 0:
            print(n)
            russian_sum += n
            
            
        m = int(m/2)
        n *= 2
    
    print(f'Multiplication ---> {mutliplication}\nRussian multiplicaton ---> {russian_sum}')

def main():
    n, m = createNumbers()
    russianMultiplication(n,m)

main()

#-----------------------------------------Ejercicio 6----------------------------------------------------------

# Diseñar un programa que genere una lista de números usando el siguiente proceso: 
# comenzar con un entero n que deberá ingresar el usuario. Si n es par, dividirlo por 2. Si n 
# es impar, multiplicarlo por 3 y sumarle 1. Repetir este proceso hasta que el nuevo valor 
# obtenido para n sea 1.
# Ejemplo, para n = 22, la secuencia que se obtiene es: 
# 22 11 33 17 52 26 13 40 20 10 5 16 8 4 2 1

def createInt():
    return int(input('Ingrese un número entero: '))

def generateList(number):

    numbers = [number]
    
    while number != 1:
        
        if number % 2 == 0:
            number = int(number/2)
        else:
            number = (number*3) + 1
        numbers.append(number)
    
    print(f'La secuencia para el número "{number}" es:')
    
    for number in numbers:
        print(number,end=' ')

def main():
    number = createInt()
    generateList(number)
    
main()





    
    



 


