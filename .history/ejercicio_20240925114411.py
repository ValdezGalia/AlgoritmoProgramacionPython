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
        
        if(n1 > 99 and n1 < 1000) and (n2 > 99 and n2 < 1000) and (n3 > 99 and n3 < 1000) and (n4 > 99 and n4 < 1000):
            bol = True
        else:
            bol = False
        
        return bol
    
    def Promedio( w, z ):
        # Variables Locales
        
        nonlocal prom
        prom = ((w + z) // 2)
        
    def PromedioTotal( w, z, x, y ):
        # Variables Locales
        
        nonlocal prom
        prom = ((w + z + x + y) // 4)
        
        
    
    # Programa principal
    # Encabezado
    print( Fore.BLUE + "UCAB Elaborado por: Orlando Valdez", Style.RESET_ALL)
    
    # Solicitud de Datos
    
    print( Fore.RED + "\nIndique numero 1 entero positivo del 100 - 999: ")
    n1 = int(input())
    
    print( Fore.RED + "Indique numero 2 entero positivo del 100 - 999: ")
    n2 = int(input())
    
    print( Fore.RED + "Indique numero 3 entero positivo del 100 - 999: ")
    n3 = int(input())
    
    print( Fore.RED + "Indique numero 4 entero positivo del 100 - 999: ")
    n4 = int(input())
    
    # Procesamiento
    
    if( not Validar(n1, n2, n3, n4) ):
        print( Fore.RED + f"ERROR, los numeros suministrados son {n1}, {n2}, {n3} y {n4}")
        print( Fore.RED + f"Ambos numeros deben ser enteros positivos del 100 sl 999", Style.RESET_ALL)
    else:
        Promedio(n1, n2)
        print( Fore.YELLOW + f"El promedio de {n1} y {n2} = {prom}")
        
        Promedio(n3, n4)
        print( Fore.YELLOW + f"El promedio 2 de {n3} y {n4} = {prom}")
        
        PromedioTotal(n1, n2, n3, n4)
        
        print( Fore.GREEN + f"El promedio total de {n1}, {n2}, {n3} y {n4} es: {prom}", Style.RESET_ALL)
    
main()