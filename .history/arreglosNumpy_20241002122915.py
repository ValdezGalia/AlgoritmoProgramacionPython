import numpy as np
import random as rd

def main():
    print("UCAB Elaborado por: Orlando Valdez")
    
    # n = np.array([0]*10)
    n = np.full(10, 0)
    
    print("El arreglo original es: ")
    for i in range(0, len(n)):
        print(n[i], end=", ")
        
    print("\nEl arreglo Nuevo es: ")
    for i in range(0, len(n)):
        n[i] = rd.randint(1, 20)
        print(n[i], end=", ")
        

main()