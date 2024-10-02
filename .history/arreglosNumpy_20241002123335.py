import numpy as np
import random as rd
import os

def main():
    print("UCAB Elaborado por: Orlando Valdez")
    
    # n = np.array([0]*10)
    n = np.full(10, 0)
    
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
            may = n[]
        

main()