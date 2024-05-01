# Resolución del ejercicio 3 del examen parcial de Programación I
# @author Gerardo Wacker

# Función solicitada para poder obtener la palabra correspondiente. Si la misma es par, devolverla al revés. Si no,
# devolverla en su orden original.
def obtenerPalabra(palabra):
    if len(palabra) % 2 == 0:
        return palabra[::-1]
    else:
        return palabra


# Función principal para descubrir el contenido del refrán.
def descubrirRefran(refran):
    # Declarar el resultado como string vacío, al cual luego vamos a agregarle contenido.
    resultado = ""
    # Dividir las palabras del refrán en una lista.
    palabras = refran.split()
    # Se hace un for, iterando por números. Se hace esto para poder saber si, después de cada palabra,
    # se le agrega un espacio, o un punto final.
    for i in range(len(palabras)):
        # Establecemos el valor de palabra, mediante obtener el valor en la posición i. Al mismo tiempo, quitamos de
        # la palabra los puntos, y la haremos minúscula para que tenga efecto la capitalización del final.
        palabra = palabras[i].lower().replace(".", "")
        # Usando la función obtenerPalabra, se agrega al string final la palabra en su formato correcto.
        resultado += obtenerPalabra(palabra)
        # Procesamiento previamente descrito, donde si se trata de la última palabra en el refrán, se agregará un
        # punto en lugar de un espacio.
        if i == (len(palabras) - 1):
            resultado += "."
        else:
            resultado += " "
    # Finalmente, hacemos mayúscula la primera letra del refrán.
    return resultado.capitalize()


# Input correspondiente para obtener el refrán.
refran = input("Ingresá el refrán: ")
print(descubrirRefran(refran))
