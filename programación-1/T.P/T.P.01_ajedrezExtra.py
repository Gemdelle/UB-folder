# -*- coding: utf-8 -*-
"""
Created on Wed Aug  22 10:29:02 2023

@author: gemdelle
"""

import math
import random

def greet():
    return print(f"\n♖ₒ▫ᵒᴼᵒ▫ₒ♙ₒ▫ᵒᴼᵒ▫ₒ♘ₒ▫ᵒᴼᵒ▫ₒ♗ₒ▫ᵒᴼᵒ▫ₒ♕ₒ▫ᵒᴼᵒ▫ₒ♔ 𝓒𝓱𝓮𝓼𝓼 𝓖𝓪𝓶𝓮 ♚ₒ▫ᵒᴼᵒ▫ₒ♛ₒ▫ᵒᴼᵒ▫ₒ♝ₒ▫ᵒᴼᵒ▫ₒ♞ₒ▫ᵒᴼᵒ▫ₒ♟ₒ▫ᵒᴼᵒ▫ₒ♜\n\n            Para ganar se deben sobrevivir 10 jugadas sin que el rey caiga en jaque.            \n       Las piezas que puede ingresar son 'peon' ～ 'torre' ～ 'alfil' ～ 'rey' ～ 'caballo'     \n                           El rey aparecerá en un lugar random del tablero.        \n\n♖ₒ▫ᵒᴼᵒ▫ₒ♙ₒ▫ᵒᴼᵒ▫ₒ♘ₒ▫ᵒᴼᵒ▫ₒ♗ₒ▫ᵒᴼᵒ▫ₒ♕ₒ▫ᵒᴼᵒ▫ₒ♔ₒ▫ᵒᴼᵒ▫ₒ♚ₒ▫ᵒᴼᵒ▫ₒ♛ₒ▫ᵒᴼᵒ▫ₒ♝ₒ▫ᵒᴼᵒ▫ₒ♞ₒ▫ᵒᴼᵒ▫ₒ♟ₒ▫ᵒᴼᵒ▫ₒ♜ₒ▫ᵒᴼᵒ▫ₒ♙\n")

def printChessLine():
    return print(f"\n♖ₒ▫ᵒᴼᵒ▫ₒ♙ₒ▫ᵒᴼᵒ▫ₒ♘ₒ▫ᵒᴼᵒ▫ₒ♗ₒ▫ᵒᴼᵒ▫ₒ♕ₒ▫ᵒᴼᵒ▫ₒ♔\n")

def inputChessPiece():
    return input("Ingrese una pieza de ajedrez: ")

def chessLetter(chess_piece):
    chess_letter = ''
    
    if chess_piece == 'peon':
        chess_letter = '𝓟 '
    elif chess_piece == 'torre':
        chess_letter = '𝓡 '
    elif chess_piece == 'alfil':
        chess_letter = '𝓑 '
    elif chess_piece == 'reina':
        chess_letter = '𝓠 '
    elif chess_piece == 'rey':
        chess_letter = '𝓚 '
    elif chess_piece == 'caballo':
        chess_letter = ' 𝓝'
        
    return chess_letter

# -------- Funciones de tablero según letra --------

def buildBoardPeon(chess_letter,squares,king_position,is_dead):
    print()
    for i in range(0,squares):
        for j in range(0,squares):
            if i == 4 and j == 3:
                print(chess_letter, end='   ')
            elif ((i == 5 and j == 2) or (i == 5 and j == 4)) and i == king_position[0] and j == king_position[1]:
                print('💀', end='   ')
                is_dead = True
            elif i == king_position[0] and j == king_position[1]:
                print('⚜️', end='   ')
            elif (i == 5 and j == 2) or (i == 5 and j == 4):
                print('🗡', end='   ')
            else:
                print('⚫', end='   ') # prints each column 
        print('\n') # prints empty row
    return is_dead

def buildBoardTorre(chess_letter,squares,king_position,is_dead):
    print()
    for i in range(0,squares):
        for j in range(0,squares):
            if i == 4 and j == 3:
                print(chess_letter, end='   ')
            elif (i == (squares/2) or j == (squares/2)-1) and i == king_position[0] and j == king_position[1]:
                print('💀', end='   ')
                is_dead = True
            elif i == king_position[0] and j == king_position[1]:
                print('⚜️', end='   ')
            elif i == (squares/2) or j == (squares/2)-1:
                print('🗡', end='   ')
            else:
                print('⚫', end='   ') # prints each column 
        print('\n') # prints empty row
    return is_dead
        
def buildBoardAlfil(chess_letter,squares,king_position,is_dead):
    print()
    for i in range(0,squares):
        for j in range(0,squares):
            if i == 4 and j == 3:
                print(chess_letter, end='   ')
            elif ((i-1 == j) or j + i == squares-1) and i == king_position[0] and j == king_position[1]:
                print('💀', end='   ')
                is_dead = True
            elif i == king_position[0] and j == king_position[1]:
                print('⚜️', end='   ')
            elif (i-1 == j) or j + i == squares-1:
                print('🗡', end='   ')
            else:
                print('⚫', end='   ') # prints each column 
        print('\n') # prints empty row
    return is_dead
        
def buildBoardReina(chess_letter,squares,king_position,is_dead):
    print()
    for i in range(0,squares):
        for j in range(0,squares):
            if i == 4 and j == 3:
                print(chess_letter, end='   ')
            elif ((i-1 == j) or j + i == squares-1 or i == (squares/2) or (j == (squares/2)-1)) and (i == king_position[0] and j == king_position[1]):
                print('💀', end='   ')
                is_dead = True
            elif i == king_position[0] and j == king_position[1]:
                print('⚜️', end='   ')
            elif (i-1 == j) or j + i == squares-1 or i == (squares/2) or j == (squares/2)-1:
                print('🗡', end='   ')
            else:
                print('⚫', end='   ') # prints each column 
        print('\n') # prints empty row
    return is_dead
        
def buildBoardRey(chess_letter,squares,king_position,is_dead):
    print()
    for i in range(0,squares):
        for j in range(0,squares):
            if i == 4 and j == 3:
                print(chess_letter, end='   ')
            elif j >= 2 and j <= 4 and i >= 3 and i <= 5 and i == king_position[0] and j == king_position[1]:
                print('💀', end='   ')
                is_dead = True
            elif i == king_position[0] and j == king_position[1]:
                print('⚜️', end='   ')
            elif j >= 2 and j <= 4 and i >= 3 and i <= 5:
                print('🗡', end='   ')
            else:
                print('⚫', end='   ') # prints each column 
        print('\n') # prints empty row
    return is_dead
        
def buildBoardCaballo(chess_letter,squares,king_position,is_dead):
    print()
    for i in range(0,squares):
        for j in range(0,squares):
            if i == 4 and j == 3:
                print(chess_letter, end='   ')
            elif (i + j) % 2 == 0 and 2<= i <=6 and i != squares/2 and 1<= j <= 5 and j != (squares/2)-1 and i == king_position[0] and j == king_position[1]:
                print('💀', end='   ')
                is_dead = True
            elif i == king_position[0] and j == king_position[1]:
                print('⚜️', end='   ')
            elif (i + j) % 2 == 0 and 2<= i <=6 and i != squares/2 and 1<= j <= 5 and j != (squares/2)-1:
                print('🗡', end='   ')
            else:
                print('⚫', end='   ') # prints each column 
        print('\n') # prints empty row
    return is_dead
    
# ---------------------------------------------------

def createKing():
    king_position = [random.randint(0,7),random.randint(0,7)]
    return king_position

def buildBoard(squares,chess_letter,king_position,is_dead):
    if chess_letter == '𝓟 ':
        is_dead = buildBoardPeon(chess_letter,squares,king_position,is_dead)
    elif chess_letter == '𝓡 ':
        is_dead = buildBoardTorre(chess_letter,squares,king_position,is_dead)
    elif chess_letter == '𝓑 ':
        is_dead = buildBoardAlfil(chess_letter,squares,king_position,is_dead)
    elif chess_letter == '𝓠 ':
        is_dead = buildBoardReina(chess_letter,squares,king_position,is_dead)
    elif chess_letter == '𝓚 ':
        is_dead = buildBoardRey(chess_letter,squares,king_position,is_dead)
    elif chess_letter == ' 𝓝':
        is_dead = buildBoardCaballo(chess_letter,squares,king_position,is_dead)
    return is_dead

def main():
    # mientras el rey no muera, siga pidiendo un personaje
    
    greet()

    play_again = 'Y'
    
    while play_again == 'Y':
        survive = 0
        is_dead = False
        SQUARES = 8
        while not is_dead:
            chess_piece = inputChessPiece()
            chess_letter = chessLetter(chess_piece)
            king_position = createKing()
            is_dead = buildBoard(SQUARES,chess_letter,king_position,is_dead)
            survive += 1
            print(f'Has sobrevivido {survive} veces')
            printChessLine()
            if survive == 10:
                is_dead = True
                print(f'♔ₒ▫ᵒᴼᵒ▫ₒ ¡Felicidades! ₒ▫ᵒᴼᵒ▫ₒ♔')
            elif is_dead == True:
                print(f'☠️ Jaque Mate ☠️\nHas sobrevivido ༼ {survive} ༽ veces antes de morir.\n')
        play_again = input('¿Seguir jugando? [Y/N]: ').upper()
        printChessLine()
    print('～ ♔ ～ Gracias por jugar ～ ♔ ～')
    
main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

