# -*- coding: utf-8 -*-
"""
Created on Fri May  5 23:37:11 2023
@author: nitro5
"""

import time
import sys

N = 9
#chequeo de numero valido.
def es_valido(sudoku, fila, columna, num):
    for i in range(N):
        if sudoku[fila][i] == num:
            return False
    for i in range(N):
        if sudoku[i][columna] == num:
            return False
    fila_inicio = fila - fila % 3
    columna_inicio = columna - columna % 3
    for i in range(3):
        for j in range(3):
            if sudoku[i + fila_inicio][j + columna_inicio] == num:
                return False

    return True
#VORAZ
def resolver_greedy(sudoku):
    for fila in range(N):
        for columna in range(N):
            if sudoku[fila][columna] == 'X':
                for num in range(1, N + 1):
                    if es_valido(sudoku, fila, columna, str(num)):
                        sudoku[fila][columna] = str(num)
                        if resolver_greedy(sudoku):
                            return True
                        sudoku[fila][columna] = 'X'
                return False
    return True
#DINAMICA
def resolver_backtracking(sudoku):
    encontrar = encontrar_vacio(sudoku)
    if not encontrar:
        return True
    else:
        fila, columna = encontrar

    for num in range(1, N + 1):
        if es_valido(sudoku, fila, columna, str(num)):
            sudoku[fila][columna] = str(num)

            if resolver_backtracking(sudoku):
                return True

            sudoku[fila][columna] = 'X'

    return False

def encontrar_vacio(sudoku):
    for fila in range(N):
        for columna in range(N):
            if sudoku[fila][columna] == 'X':
                return (fila, columna)
    return None
#Imprimir sudoku
def imprimir_sudoku(sudoku):
    for i in range(N):
        for j in range(N):
            print(sudoku[i][j], end=" ")
        print()

#lectura
def leer_sudoku(nombre_archivo):
    sudoku = []
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            fila = [caracter for caracter in linea if caracter != '\n']
            sudoku.append(fila)
    return sudoku

#MAIN
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Por favor, proporciona el nombre del archivo como argumento de línea de comandos.")
        sys.exit(1)
        #nombre_archivo = "game_04.txt"
    else:
        nombre_archivo = sys.argv[1]
    sudoku = leer_sudoku(nombre_archivo)

    tiempo_inicio = time.time()
    resolver_greedy(sudoku)
    tiempo_fin = time.time()
    print("Solución utilizando el algoritmo voraz:")
    imprimir_sudoku(sudoku)
    print("Tiempo transcurrido: {:.6f} segundos".format(tiempo_fin - tiempo_inicio))

    sudoku = leer_sudoku(nombre_archivo)
    tiempo_inicio = time.time()
    resolver_backtracking(sudoku)
    tiempo_fin = time.time()
    print("Solución utilizando el algoritmo dinámico con backtracking:")
    imprimir_sudoku(sudoku)
    print("Tiempo transcurrido: {:.6f} segundos".format(tiempo_fin - tiempo_inicio))
