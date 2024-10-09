import numpy as np
import random as rd
from colorama import Fore, Style

def main():
    z = np.array([" "]*10)
    mc = np.array([0]*10)
    me = np.array([0]*10)
    
    def imprimirArreglo(arr):
        for i in range(0, len(arr)):
            if( i != len(arr) - 1 ):
                print(arr[i], end=", ")
            else:
                print(arr[i], end=". ")
                
        print("\n\n---------------------------------------------")
        
        
    def ordenarMenorAMayor(arr):
        for i in range(0, len(arr)):
            for j in range(i+1, len(arr)):
                if( arr[i] > arr[j] ):
                    aux = arr[j]
                    arr[j] = arr[i]
                    arr[i] = aux
                    
        for i in range(0, len(arr)):
            if( i != len(arr) - 1 ):
                print(arr[i], end=", ")
            else:
                print(arr[i], end=". ")
        
        print()
        print("-"*50)
    
    def MenorMayor(arr):
        print(Fore.GREEN + f"\nEl menor monto de envio es: { Fore.WHITE + f"{arr[0]}," + Fore.GREEN} y el monto de mayor envio es: {Fore.WHITE + f"{arr[len(arr)-1]}"}.")
        
        
                    
    
    for i in range(0, len(z)):
        rand = rd.randint(1, 4)
        randMc = rd.randint(1000, 99999)
        if(rand == 1):
            z[i] = "N"
            mc[i] = randMc
        elif(rand == 2):
            z[i] = "S"
            mc[i] = randMc
        elif(rand == 3):
            z[i] = "E"
            mc[i] = randMc
        elif(rand == 4):
            z[i] = "O"
            mc[i] = randMc
            
    
    for i in range(0, len(me)):
        if(z[i] == "N"):
            p = ((mc[i]*20)//100)
            me[i] = p
        elif(z[i] == "S"):
            p = ((mc[i]*25)//100)
            me[i] = p
        elif(z[i] == "E"):
            p = ((mc[i]*35)//100)
            me[i] = p
        elif(z[i] == "O"):
            p = ((mc[i]*30)//100)
            me[i] = p
            
    print(Fore.RED + "\nArreglo de las zonas:", Style.RESET_ALL)
    imprimirArreglo(z)
    
    print(Fore.RED + "Arreglo de monto de compra:", Style.RESET_ALL)
    imprimirArreglo(mc)
    
    print(Fore.GREEN + "Arreglo de monto de envio:", Style.RESET_ALL)
    imprimirArreglo(me)
    
    print(Fore.GREEN + "Arreglo ordenado de menor a mayor", Style.RESET_ALL)
    ordenarMenorAMayor(me)
    
    MenorMayor(me)
main()