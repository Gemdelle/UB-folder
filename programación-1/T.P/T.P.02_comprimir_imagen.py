# -*- coding: utf-8 -*-
"""
Created on Wed Aug  30 08:53:31 2023

@author: gemdelle
"""

#  ˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳⁺ˏ༻✧ 𝓣.𝓟. 𝟘𝟚 - 𝓒𝓸𝓶𝓹𝓻𝓲𝓶𝓲𝓻 𝓲𝓶𝓪𝓰𝓮𝓷 ✧༺ˎ⁺˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳

# Un grupo de investigadores se encuentra trabajando en un centro de observación espacial,
# donde toman fotografías digitales mediante un nuevo telescopio a una zona aún no
# explorada del espacio, con el objetivo de determinar la presencia de nuevos planetas
# girando alrededor de las estrellas que allí se encuentran.
# Estas fotografías tienen la particularidad de contener muy pocos colores, por lo aque cada
# pixel puede ser representado mediante alguna de las siguientes letras que indica su color:
# 'B', 'N', 'R', 'V', 'A'. De esta forma una imagen es directamente una secuencia de letras.
# Además de contener una poca cantidad de colores, también tienen la particularidad de ser
# demasiado grandes con la intención de obtener la mejor resolución posible. Por este
# motivo los investigadores necesitan de un método para comprimir estas imágenes y luego
# poder ser almacenadas.
# Mediante un estudio determinaron que un método muy simple para comprimir estas
# imágenes es buscar secuencias donde una letra este repetida de forma consecutiva, para
# después almacenarse sólo una única letra junto al número de veces que se repite. Para
# diferenciar las partes de la imagen que han sido comprimidas, y luego poder recuperar la
# imagen original sin ningún problema, se encierran entre paréntesis tanto la letra como el
# valor que indica la cantidad de repeticiones. Para lograr una verdadera compresión, se
# debe reemplazar una repetición de letras siempre que esta sea mayor que 4, ya que en caso
# contrario no se obtiene compresión alguna.
# Se pide escribir dos funciones, la primera recibiendo como entrada una cadena de
# caracteres conteniendo una imagen sin comprimir y que genere y retorne otra cadena con
# la compresión de la imagen y la segunda función que reciba una cadena conteniendo la
# imagen comprimida, genere y retorne otra cadena con la imagen descomprimida.
# Ejemplo:
# primera función
# imagen: NNNNNNNNBRAVBRRRRRAAAAAAAVVVVV
# imagen comprimida: (N8)BRAVB(R5)(A7)(V5)

# EJEMPLOS DE INPUTS 
# NNNNNNNNBRAVBRRRRRAAAAAAAVVVVV
# (N8)BRAVB(R5)(A7)(V5)

# NNNNBBBBRRRRBARVVVAAARVRAABRABRAAAABBBBBBBRBAAARBRAAAVRBVBAAANNBNRRRNBRNNAANBRNANAAAAA
# (N8)BRAVB(R5)(A7)(V5)BRABVBRA(N6)(B5)

# Funciones de compresión

def createImageCompression():
    return input('\n˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳\n\nIngrese una cadena para comprimir: ')

def createImageDecompression():
    return input('Ingrese una cadena para descomprimir: ')

def separateCommonCharacters(seq):
    count = 0
    rep = []
    
    for i in range(len(seq)):
        if i < len(seq)-1:
            if seq[i] == seq[i+1]:
                rep.append(seq[i])
            else:
                rep.append(seq[i])
                rep.append('-')
        if i == len(seq)-1:
            if seq[i-1] == seq[-1]:
                rep.append(seq[i])
            else:
                rep.append(seq[i])
        
    return ''.join(rep).split('-') # ['NNNNNNNN', 'B', 'R', 'A', 'V', 'B', 'RRRRR', 'AAAAAAA', 'VVVVV']


def countCommonCharacters(rep):
    comp_seq = []
    
    for i in range(len(rep)):
        if len(rep[i]) > 4:
            count = len(rep[i])
            comp_seq.append('('+rep[i][0]+str(count)+')')   
        else:
            comp_seq.append(rep[i])
     
    return ''.join(comp_seq) # (N8)BRAVB(R5)(A7)(V5)

def compressImage(image):
    
    compressed_image = separateCommonCharacters(image)
    compressed_image = countCommonCharacters(compressed_image)  
    
    return compressed_image

# Funciones de descompresión

def cleanImage(image):
    
    clean_sequence = []
    
    for i in range(len(image)):
        if image[i] not in '()':
            clean_sequence.append(image[i])
    
    return clean_sequence
        
def expandImage(clean_sequence):

    expanded_sequence = []
    
    for i in range(len(clean_sequence)):  
        if clean_sequence[i].isnumeric():
            for _ in range(int(clean_sequence[i])-1):
                expanded_sequence.append(clean_sequence[i-1])
        else:
            expanded_sequence.append(clean_sequence[i])            
    
    return ''.join(expanded_sequence)  

def decompressImage(image):
    
    decompressed_image = cleanImage(image)
    decompressed_image = expandImage(decompressed_image)

    return decompressed_image

def printImage(decompressed_image):

    print_image = [] 

    for i in range(len(decompressed_image)):
        if decompressed_image[i] == 'B':
            print_image.append('🤍')
        elif decompressed_image[i] == 'N':
            print_image.append('🖤')
        elif decompressed_image[i] == 'R':
            print_image.append('💗')
        elif decompressed_image[i] == 'V':
            print_image.append('💜')
        else:
            print_image.append('💙')

    print_image = ''.join(print_image)
    print(f'\n✦⋆⋆☆⋆⋆✦ Impresión ✦⋆⋆☆⋆⋆✦\n')
    
    for i in range(len(print_image)):
        if i == 0 or (i+1) % 6 != 0:
            print(print_image[i],end='') # imprimir caracteres pegados
        else:
            print(print_image[i]) # imprime el caracter y hace el salto de línea automáticamente porque no se especifica el end

def main():
    #  Creación de variables iniciales
    image_to_compress = createImageCompression()
    image_to_decompress = createImageDecompression()
    
    # Manipulación de variables con funciones
    compressed_image = compressImage(image_to_compress) 
    decompressed_image = decompressImage(image_to_decompress) 
    
    print(f'\n⁺⁺⁺⁺⁺⁺⁺⁺⁺⁺⁺⁺⁺⁺⁺⁺⁺⁺⁺⁺⁺⁺⁺⁺⁺⁺⁺⁺‧͙⁺˚*･༓☾　　☽༓･*˚⁺‧͙⁺⁺⁺⁺⁺⁺⁺⁺⁺⁺⁺⁺⁺⁺⁺⁺⁺⁺⁺⁺⁺⁺⁺⁺⁺⁺⁺⁺⁺⁺⁺⁺⁺⁺⁺⁺\n\n˳༚⁺ Imagen a comprimir ⁺༚˳ {image_to_compress} ---> {compressed_image}\n˳༚⁺ Imagen a descomprimir ⁺༚˳ {image_to_decompress} ---> {decompressed_image}\n\n˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳')
    
    printImage(decompressed_image)
           
main()

    
    

