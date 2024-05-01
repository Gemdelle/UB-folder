# Resolución del ejercicio 1 del examen parcial de Programación I
# @author Gerardo Wacker

# Esta función se dedica a calcular la k-ésima de una patente. Obtiene como parámetros a la patente (en formato string),
# y a k (en formato int). Es usada por la función "siguiente()", también solicitada.
def k_esima(p, k):
    # Se solicita la patente en formato string para verificar si su longitud equivale a 5 caracteres.
    if len(p) == 5:
        # Si cumple con ello, se lo convierte a integer, para luego procesarlo de manera fácil.
        patente_int = int(p)
        # Si la suma de patente + k da un número dentro del rango solicitado, es decir, es mayor a 00000 y
        # menor a 10000, continuar.
        if 10000 >= (patente_int + k) >= 0:
            # Sumar los dos parámetros, y convertirlo a string, para poder luego rellenar con los "0" que sean
            # necesarios, y así cumplir con el formato de las patentes de 5 caracteres.
            patente_string = str(patente_int + k)
            # Si la k equivale a 1, se deduce que trata de obtener la siguiente. Entonces, devuelve un string
            # redactado de la manera correspondiente.
            if k == 1:
                return "La patente siguiente es " + patente_string.zfill(5) + "."
            # Si k no es 1, entonces devolver un string que muestra el valor de k.
            else:
                return "La " + str(k) + "-ésima patente es " + patente_string.zfill(5) + "."
        # Finalmente, en caso de que no cumpla con uno de los parámetros solicitados, devolver un string aclarándolo.
        else:
            return "La patente no es válida, el resultado no se encuentra dentro del rango establecido (00000 a 10000)."
    else:
        return "La patente no es válida, debe estar compuesta por 5 caracteres."


# Esta función se dedica a calcular la siguiente patente, por lo que es
# simplemente calcular la k-ésima, pero siendo k = 1.
def siguiente(p):
    return k_esima(p, 1)


# Inputs correspondientes para que las dos funciones puedan correr, una detrás de otra.
patente = input("Ingresá la patente: ")
print(siguiente(patente))

patente2 = input("Ingresá una segunda patente: ")
input_k = input("Ahora, ingresá cuántas patentes más querés ver: ")
print(k_esima(patente2, int(input_k)))
