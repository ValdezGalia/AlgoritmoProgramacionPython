def main():
    def Regresiva(x):
        if x > 0:
            Regresiva(x-1)
            print(x, end=", ")
    
    print("UCAB Elaborado por: Orlando Valdez")
    print("Indique el numero entero positivo mayor que 1: ", end="")
    n = int(input())
    
    
    
    #Opcion Iterativa
    x=n
    
    print("Opcion Iterativa")
    while(x>0):
        print(x, end=", ")
        x -= 1
        
    print("\n\nOpcion Regresiva")
    Regresiva(n)
        

main()