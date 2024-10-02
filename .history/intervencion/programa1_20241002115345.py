from colorama import Fore, Style

# Entregar hoy antes de las 22:00 de la noche

def main():
    p1, p2, p3, p4, p5, p6 = 0, 0, 0, 0, 0, 0
    
    def Separar(n1, n2):
        
        count = 6
        nonlocal p1,p2,p3,p4,p5,p6
        
        while( count <= 0 ):
            if( count >= 1 and count <= 3 ):
                p1 = n1 // 1000000
                p2 = (n1 % 1000000) // 10000
                p3 = ((n1 % 1000000) % 10000) // 100
            else:
                p4 = n2 // 1000000
                p5 = (n2 % 1000000) // 10000
                p6 = ((n2 % 1000000) % 10000) // 100
            
            count -= 1
    
    def mayor( p1, p2, p3 ):
        if( p1 > p2 ) and ( p1 > p3):
            print("El mayor del primer grupo es")
        
    
    def validar(n1, n2):
        if (n1 > 9999999 and n1 < 100000000) and (n2 > 9999999 and n2 < 100000000):
            Separar( n1, n2 )
        else:
            print("Error, Alguno de los numeros suministrados es menor o mayor que 8 digitos")
    
    print("UCAB Elaborado por: Orlando Valdez")
    
    print(Fore.BLUE + "Ingrese el primer numero de 8 digitos enteros positivos: ")
    n1 = int(input())
    
    print(Fore.BLUE + "Ingrese el primer numero de 8 digitos enteros positivos: " + Style.RESET_ALL)
    n2 = int(input())
    
    validar(n1, n2)
    
    
main()

while():
    while