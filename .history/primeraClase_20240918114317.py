import os

def main():
    print("UCAB Elaborado por: Orlando valdez")
    
    cont = 0
    while cont < 10:
        print(len(cont))
        if cont == 9:
            print(cont, end='.')
        else:
            print(cont, end=', ')
        cont += 1
    
    
    
    
    
    # for i in range(0, 10):
    #     print(i, end=", ")
main()