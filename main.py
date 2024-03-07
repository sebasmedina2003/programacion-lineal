from scripts.transporte import menu_transporte
from scripts.hungaro import menu_hungaro

def menu() -> None:
    # Mantenemos un ciclo abierto para
    while(True):
        # iniciamos mostrando el menu
        print('Seleccione el tipo de problema a resolver')
        print('1: Problema de Transporte')
        print('2: Problema de Asignación')
        print('3: Salir del programa')

        # Inicializamos las variables de control de la respuesta
        opcion = ''
        opciones = ['1', '2', '3']

        # Mientras que la opcion no este en las disponibles seguimos leyendo la variable
        while(opcion not in opciones): opcion = input('-> ')

        # Según la opcion vamos a un modulo u a otro
        if(opcion == '1'):
            menu_transporte()

        elif(opcion == '2'):
            menu_hungaro()

        else:
            print('\nSaliendo del programa')
            return None

if __name__ == '__main__':
    menu()