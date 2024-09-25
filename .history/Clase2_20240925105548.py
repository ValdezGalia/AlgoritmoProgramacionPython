# Librerias
import colorama
from colorama import Fore, Style


def main():
    # Variables globales
    
    # Funciones y procedimientos
    def Validar(x, y):
        # Variables locales
        bol = True
        
        if(x > 0) and (y > 0):
            bol = True
        else:
            bol = False
        
        return bol
    
    # Programa principal
    # Encabezado
    print( Fore.BLUE + "UCAB Elaborado por: Orlando Valdez", Style.RESET_ALL)
    
    # Solicitud de Datos
    
    print( Fore.RED + "Indique numero 1 entero positivo mayor a cero: ")
    n1 = int(input())
    
    print( Fore.RED + "Indique numero 2 entero positivo mayor a cero: ")
    n2 = int(input())
    
    # Procesamiento
    
    if( not Validar(n1, n2) ):
        print( f"ERROR, los numeros suministrados son {n1} y {n2}" )
    
main()