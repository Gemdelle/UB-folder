# PRÁCTICA 01
import math

#-----------------------------------------Ejercicio 1----------------------------------------------------------
# Diseña un programa que lea la edad de dos personas y diga quién es más joven, la
# primera o la segunda. Ten en cuenta que ambas pueden tener la misma edad. En tal caso, 
# hazlo saber con un mensaje adecuado.

def defineAge1():
    return int(input('Ingrese la primera edad: '))

def defineAge2():
    return int(input('Ingrese la segunda edad: '))

def oldest(age1, age2):
    if age1 > age2:
        print(f'{age1} es mayor a {age2}')
    elif age2 > age1:
        print(f'{age2} es mayor a {age1}')
    else:
        print(f'{age2} es igual a {age1}')
        
def main():
    age1 = defineAge1()
    age2 = defineAge2()   
    oldest(age1,age2)
    
main()
    
#-----------------------------------------Ejercicio 2----------------------------------------------------------
# Diseña un programa que lea un carácter de teclado y muestre por pantalla el mensaje
# "Es paréntesis" sólo si el carácter leído es un paréntesis abierto o cerrado. En caso contrario
# muestra el mensaje “No es paréntesis”.

def createChar():
    return input('Ingrese un caracter: ')

def isParenth(char):
    if char in '()':
        print(f'"{char}" es paréntesis')
    else:
        print(f'"{char}" no es paréntesis')
        
def main():
    char = createChar()
    isParenth(char)
    
main()
        
#-----------------------------------------Ejercicio 3----------------------------------------------------------
# Diseña un programa que, dado un número entero, muestre por pantalla el mensaje "El
# número es par." cuando el número sea par y el mensaje "El número es impar." cuando sea
# impar. (Una pista: un número es par si el resto de dividirlo por 2 es 0, e impar en caso 
# contrario.)

def createNumber():
    return int(input('Ingrese un número: '))

def evaluateNumber(number):
    if number % 2 == 0:
        print(f'El número "{number}" es par')
    else: 
        print(f'El número "{number}" no es par')
        
def main():
    number = createNumber()
    evaluateNumber(number)
    
main()

#-----------------------------------------Ejercicio 4---------------------------------------------------------
# Diseña un programa que, dado un número entero, determine si éste es el doble de un
# número impar. (Ejemplo: 14 es el doble de 7, que es impar.")

def createNumber():
    return int(input('Ingrese un número entero: '))

def evaluateNumber(number):
    if (number/2) % 2 == 0:
        print(f'Eñ número "{number}" es el doble de un número par --> {number/2}')
    else:
        print(f'Eñ número "{number}" no es el doble de un número par --> {number/2}')
        
def main():
    number = createNumber()
    evaluateNumber(number)
    
main()
               
#-----------------------------------------Ejercicio 5----------------------------------------------------------
# Escribir un programa que permita ingresar dos números enteros y escribirlos en orden 
# creciente.

def createNumberOne():
    return int(input('Ingrese el primer número: '))

def createNumberTwo():
    return int(input('Ingrese el segundo número: '))

def defineOrder(n1,n2):
    
    if n1 < n2:
        print(f'{n1} {n2}')
    else: 
        print(f'{n2} {n1}')

def main():
    n1 = createNumberOne()
    n2 = createNumberTwo()
    
    defineOrder(n1,n2)
    
main()

#-----------------------------------------Ejercicio 6----------------------------------------------------------
# Escribir un programa que permita ingresar tres números enteros y escribirlos en orden 
# creciente.

def createNumber1():
    return int(input('Ingrese el primer n�mero: '))

def createNumber2():
    return int(input('Ingrese el segundo n�mero: '))

def createNumber3():
    return int(input('Ingrese el tercer n�mero: '))

def orderNumbers(n1,n2,n3):
    
    smallest = n1
    middle = n2
    biggest = n3
    aux = 0
    
    if middle > biggest:
        aux = middle
        middle = biggest
        biggest = aux
    if smallest > biggest:
        aux = smallest
        smallest = biggest
        biggest = aux
    if smallest > middle:
        aux = smallest
        smallest = middle
        middle = aux

    print(f'Smallest --> {smallest}\nMiddle --> {middle}\nBiggest --> {biggest}')

def main():
    
    n1 = createNumber1()
    n2 = createNumber2()
    n3 = createNumber3()
    
    orderNumbers(n1,n2,n3)
    
main()


#-----------------------------------------Ejercicio 7----------------------------------------------------------
# Escribir un programa que permita ingresar el mes y el año y muestre la cantidad de días 
# del mes. Por ejemplo, si el usuario ingresa mes 2 y año 2000, el programa debe responder 
# que Febrero 2000 tiene 29 días. Si el usuario ingresa mes 3 y año 2005, el programa 
# responderá que Marzo 2005 tiene 31 días.

def createMonth():
    return input('Ingrese un mes: ').lower()

def createYear():
    return int(input('Ingrese un año: '))

def evaluateDate(month,year):
    
    days_30 = 'abril junio septiembre noviembre'
    days_31 = 'enero marzo mayo julio agosto octubre diciembre'
    
    if month == 'febrero':
        if year % 4 == 0: 
            print(f'El mes febrero del año {year} tiene 29 días')
        else:
            print(f'El mes febrero del año {year} tiene 28 días')
    if month in days_30:
        print(f'El mes {month} del año {year} tiene 30 días')
    elif month in days_31:
        print(f'El mes {month} del año {year} tiene 31 días')

def main():
    month = createMonth()
    year = createYear()
    
    evaluateDate(month,year)
    
main()

#-----------------------------------------Ejercicio 8----------------------------------------------------------
# Escribir un programa que permita ingresar las coordenadas (x,y) de un punto en el plano y
# verifique si el punto está dentro del círculo con centro en (0,0) y radio 10, o está fuera o en 
# la circunferencia. Mostrar los mensajes adecuados

def createCoordX():
    return int(input('Ingrese la coordenada "X": '))

def createCoordY():
    return int(input('Ingrese la coordenada "Y": '))

def evaluateCoords(x,y):
    module = math.sqrt(pow(x, 2)+pow(y,2))
    
    if module < 10:
        print(f'Las coordenadas [{x},{y}] se encuentran dentro de la circunferencia')
    elif module == 10:
        print(f'Las coordenadas [{x},{y}] se encuentran sobre la circunferencia')
    else: 
        print(f'Las coordenadas [{x},{y}] se encuentran fuera de la circunferencia')

def main():
    x = createCoordX()
    y = createCoordY()
    evaluateCoords(x,y)
    
main()

