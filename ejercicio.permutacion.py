import numpy as np
from colorama import Fore, Style

def main():
    number = np.array([0]*20)
    increment = 1
    
    def permutacion(arr):
        
        for i in range(len(arr)):
            if(i == 0):
                aux = arr[i]
                arr[i] = arr[len(arr)-1]
                arr[len(arr)-1] = aux
            else:
                
                
        return arr
    
    def printerArray(arr):
        for i in range(len(arr)):
            if( i != len(arr) - 1 ):
                print(arr[i], end=", ")
            else:
                print(arr[i], end=". ")
                
        print()
    
    for i in range(len(number)):
        number[i] = increment
        increment += 1
        
    print(Fore.RED + "\nArreglo original", Style.RESET_ALL)
    printerArray(number)
    
    print(Fore.RED + "\nLista permutada 1 vez", Style.RESET_ALL)
    arrPermutado = permutacion(number)
    printerArray(arrPermutado)
        
main()