import numpy as np
import random as rd
import os

def main():
    print("UCAB Elaborado por: Orlando Valdez") #                    Complejidad Temporal              Complejidad Especial
    
    # n = np.array([0]*10)
    n = np.full(10, 0)                                                                       #                40 bytes
    
    os.system('cls')
    
    print("El arreglo original es: ")
    for i in range(0, len(n)):
        print(n[i], end=", ")
        
    print("\n\nEl arreglo Nuevo es: ")
    for i in range(0, len(n)):
        n[i] = rd.randint(1, 20)
        print(n[i], end=", ")
        
    may = n[0]
    pos = 0
    
    for i in range(0, len(n)):
        if( n[i] > may ):
            may = n[i]
            pos = i
    
    print("\n\nEl mayor elemento es: ", may)
    print("Su posicion es: ", pos)
    
    # Ordenar ascendente
    
    for i in range(0, (len(n) - 1) ):
        for j in range((i+1), len(n)):
            if( n[j] < n[i] ):
                n[j] = n[i] + n[j]
                n[i] = n[j] - n[i]
                n[j] = n[j] - n[i]
                
                
    print("\nArreglo ordenado: ")
    for i in range(0, len(n)):
        print(n[i], end=", ")
        

main()