# Librerias
import colorama
from colorama import Fore, Style


def main():
    # Variables globales
    prom : int
    prom = 0
    
    # Funciones y procedimientos
    def Validar(n1, n2, n3, n4):
        # Variables locales
        bol = True
        
        if(n1 > 99 and n1 < 1000) and (n2 > 99 and n2 < 1000) (n2 > 99 and n2 < 1000) (n2 > 99 and n4 < 1000):
            bol = True
        else:
            bol = False
        
        return bol
    
    def Promedio( w, z ):
        # Variables Locales
        
        nonlocal prom
        prom = ((w + z) // 2)
    
    # Programa principal
    # Encabezado
    print( Fore.BLUE + "UCAB Elaborado por: Orlando Valdez", Style.RESET_ALL)
    
    # Solicitud de Datos
    
    print( Fore.RED + "Indique numero 1 entero positivo mayor a cero: ")
    n1 = int(input())
    
    print( Fore.RED + "Indique numero 2 entero positivo mayor a cero: ")
    n2 = int(input())
    
    print( Fore.RED + "Indique numero 1 entero positivo mayor a cero: ")
    n3 = int(input())
    
    print( Fore.RED + "Indique numero 2 entero positivo mayor a cero: ")
    n4 = int(input())
    
    # Procesamiento
    
    if( not Validar(n1, n2) ):
        print( Fore.RED + f"ERROR, los numeros suministrados son {n1} y {n2}" )
        print( Fore.RED + f"Ambos numeros deben ser enteros positivos mayores que cero", Style.RESET_ALL)
    else:
        Promedio(n1, n2)
        print( Fore.GREEN + f"El promedio de {n1} y {n2} es: {prom}", Style.RESET_ALL)
    
main()