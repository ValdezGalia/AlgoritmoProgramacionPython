# Librerias
import colorama
from colorama import Fore, Style


def main():
    # Variables globales
    
    # Funciones y procedimientos
    def Validar(x, y):
        # Variables locales
        bol = True
        
         
        if(x > 0):
            return  
    
    # Programa principal
    # Encabezado
    print( Fore.BLUE + "UCAB Elaborado por: Orlando Valdez", Style.RESET_ALL)
    
    # Solicitud de Datos
    
    print( Fore.RED + "Indique numero 1 entero positivo mayor a cero: ")
    n1 = int(input())
    
    print( Fore.RED + "Indique numero 2 entero positivo mayor a cero: ")
    n2 = int(input())
    
    # Procesamiento
    
    if(Validar()):
        print("ERROR, El numero ingresado no es mayor que cero (0).")
    
main()