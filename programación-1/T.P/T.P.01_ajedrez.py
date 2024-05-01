# -*- coding: utf-8 -*-
"""
Created on Thur Aug  23 12:54:03 2023

@author: gemdelle
"""

#  ˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳⁺ˏ༻✧ 𝓣.𝓟. 𝟘𝟙 - 𝓐𝓳𝓮𝓭𝓻𝓮𝔃 ✧༺ˎ⁺˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳˳༚⁺༚˳

def originalBoard():
    SQUARES = 8
    for i in range(0,SQUARES):
        for j in range(0,SQUARES):
            print([i,j],end=' ')
        print()
        
def originalBoardNumbers():
    SQUARES = 8
    for i in range(0,SQUARES):
        for j in range(0,SQUARES):
            print(i + j,end='  ')
        print()


def createBoard(): 
    SQUARES = 8
    board = []
    row = []
    
    for i in range(0,SQUARES):
        positions = 0
        for j in range(0,SQUARES):
            position = input(f"Ingrese el personaje {j+1} de la fila {i+1}: ")
            row.append(position)
        board.append(row)
        print(f'\nLa línea ingresada es {row}\n')
        row = []
    return board

def printBoard(board):
    SQUARES = 8
    for i in range(0,SQUARES):
        for j in range(0,SQUARES):
            print(board[i][j],end=' ')
        print()


def pawnDangerousPositions(board):
    position = [0,0]
    positions = [[0,0],[0,0]] # 2 possible positions for 1 pawn
    dangerous_positions = []
    
    for i in range(0,len(board)):
        for j in range(0,len(board)):
            if board[i][j] == 'p' and i < 7:
                if 0 < j < 7:
                    positions = [[i+1,j+1],[i+1,j-1]]
                    dangerous_positions.append(positions)
                # arreglar si se sale del tablero
            elif board[i][j] == 'P' and i > 0:
                positions = [[i-1,j+1],[i-1,j-1]]  
                dangerous_positions.append(positions)
    return dangerous_positions

def main():
    board = createBoard()
    printBoard(board)
    pawnDangerousPositions(board)
    
# main()

originalBoardNumbers()
    
    
# abs(rx - ax) == abs(ry - ay) para la coordenada del rey y el alfil.
# torre = coincide en fila o columna
# 
    
    
    
    
    
    
    
    
    
    
    
    

