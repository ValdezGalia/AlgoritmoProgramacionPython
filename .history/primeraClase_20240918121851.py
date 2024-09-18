import os

def main():
    print("UCAB Elaborado por: Orlando valdez")
    
    cont = 0
    suma = 0
    
    valorInicial = int(input("Ingrese un valor inicial entero positivo: "))
    cantidadN = int(input("Ingrese la cantidad de numeros que desea con un valor entero positivo: "))
    deCuanto = int(input("Ingrese de cuanto en cuanto quiere incrementar el valor inicial por un numero entero positivo: "))
    ciclo = True
    
    
    
    while(ciclo):
        if( cont != cantidadN ):
            
            print(valorInicial, end=", ")
            valorInicial += deCuanto
            if(valorInicial % 2 != 0):
                suma += valorInicial
            
        else:
            print()
            ciclo = False
        cont += 1
    
    # while cont < 10:
    #     if cont % 2 != 0:
    #         suma += cont 
            
            
            
    #     if cont == 9:
    #         print(cont, end='. ')
    #         print()
    #         print(suma)
    #     else:
    #         print(cont, end=', ')
    #     cont += 1
    
    
    
    
    
    # for i in range(0, 10):
    #     print(i, end=", ")
main()