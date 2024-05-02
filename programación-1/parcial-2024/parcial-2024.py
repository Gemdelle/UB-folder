# -*- coding: utf-8 -*-
"""
Created on Wed May  1 19:11:22 2024

@author: Gemdelle
"""


# Ordenar los siguientes elementos para escribir una función llamada areaRectangulo que calcule el
# área de un rectángulo.

def areaRectangulo(base,altura):
    area = base * altura
    return area

# Ejercicio 4:
# Hacer una función que permita ingresar un número n desde teclado. El número n debe verificar que 
# se encuentre entre dos valores a y b (suponer que a < b). La función deberá tener como parámetros 
# los valores a y b y deberá retornar el valor n que cumple con dicha condición. 

# Usar la función para ingresar la base y la altura de un rectángulo cuyos valores deben ser positivos y menores que 100. 
# Usar la función del ejercicio 3 para calcular la superficie del rectángulo. Mostrar el resultado calculado

def validarNumero(a,b):
    menor = a
    mayor = b
    numero = int(input(f"Ingrese un número dentro del rango {menor}-{mayor}: "))
    
    while numero<a or numero>b:
        numero = int(input(f"Número fuera de rango. Ingrese un número dentro del rango {menor}-{mayor}: "))
    
    return numero

def areaRectangulo(base, altura):
    area = base * altura
    return area
        
def main():
    print("Base del rectángulo")
    base = validarNumero(0,100)
    print("\nAltura del rectángulo")
    altura = validarNumero(0,100)
    area = areaRectangulo(base,altura)
    print(f"\nEl área calculada del rectángulo es {area}")
    
main()


