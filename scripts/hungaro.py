from .modulos.validations import REG_NUMBER, REG_FLOAT, lectura
from .modulos.calculos import metodo_hungaro, costos_hungaro
from .modulos.mostrar import mostrar_matriz_hungaro

def menu_hungaro() -> None:
    # inicializamos las variables
    print('Ingrese la cantidad de Tareas:')
    cantidad_tareas= int(lectura(REG_NUMBER))
    print('Ingrese la cantidad de Trabajadores:')
    cantidad_trabajadores = int(lectura(REG_NUMBER))

    matriz_datos = []

    # Procedemos a la carga inicial de datos
    for k in range(cantidad_trabajadores):
        # En cada iteración creamos una lista de valores
        datos = []

        for j in range(cantidad_tareas):
            print(f'Costo unitario de la tarea [{k+1}] del trabajador [{j+1}]:')
            datos.append(float(lectura(REG_FLOAT)))

        # Después de cargar la lista de datos la anexamos a la matriz de datos
        matriz_datos.append(datos)
    
    # Creamos la copia que sera la matriz de costos
    matriz_costos = [fila for fila in matriz_datos]

    # Usamos el algotimo del metodo hungaro para encontrar la matriz resultante
    matriz_resultado = metodo_hungaro(matriz=matriz_datos)

    mostrar_matriz_hungaro(matriz_resultado)

    # Calculamos los costos
    print('\nCostos:')
    costos_hungaro(matriz_resultado, matriz_costos)