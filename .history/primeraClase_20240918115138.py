import os

def main():
    print("UCAB Elaborado por: Orlando valdez")
    
    cont = 0
    suma = 0
    while cont < 10:
        if cont % 2 != 0:
            suma += cont 
            
            
            
        if cont == 9:
            print(cont, end='. ')
            print()
            print(suma)
        else:
            print(cont, end=', ')
        cont += 1
    
    
    
    
    
    # for i in range(0, 10):
    #     print(i, end=", ")
main()