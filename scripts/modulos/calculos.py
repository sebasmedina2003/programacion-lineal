from numpy import array, transpose, identity


def esquina_noroeste(matriz:list[list[float]], ofertas:list[float], demandas:list[float]) -> list[dict]:
    resultados = []
    columnas_resueltas = []
    filas_resueltas = []

    # Recorremos la matriz de datos por filas
    for fila, lista in enumerate(matriz):
        for columna in range(len(lista)):
            # Verificamos si no es una fila o columna culminada
            if(columna not in columnas_resueltas and fila not in filas_resueltas):
                # Caso en el que la oferta es mayor que la demanda
                if(ofertas[fila] > demandas[columna]):
                    resultado = {
                        'valor': demandas[columna],
                        'coordenada': [fila, columna]
                    }
                    # Guardamos la columna como resuelta y anexamos el diccionario
                    columnas_resueltas.append(columna)
                    resultados.append(resultado)

                    # Restamos el valor de la oferta y ponemos en 0 la demanda
                    ofertas[fila] -= demandas[columna]
                    demandas[columna] = 0
                
                # Caso en el que la demanda es mayor que la oferta
                elif(demandas[columna] > ofertas[fila]):
                    resultado = {
                        'valor': ofertas[fila],
                        'coordenada': [fila, columna]
                    }
                    # Guardamos la fila como terminada y anexamos el resultado
                    filas_resueltas.append(fila)
                    resultados.append(resultado)

                    # Restamos el valor de la demanda con el de la oferta y ponemos en 0 la oferta
                    demandas[columna] -= ofertas[fila]
                    ofertas[fila] = 0
                
                # Caso en el que la oferta y demanda son iguales
                else:
                    # Guardamos cualquier dato de oferta o demanda
                    resultado = {
                        'valor': ofertas[fila],
                        'coordenada': [fila, columna]
                    }
                    # Guardamos la fila y columna como terminada
                    filas_resueltas.append(fila)
                    columnas_resueltas.append(columna)

                    # Guardamos el resultado
                    resultados.append(resultado)

                    # Ponemos en 0 la oferta y demanda
                    ofertas[fila] = 0
                    demandas[columna] = 0

    # Despues de terminar los calculos retornamos los resultados
    return resultados


def restar_minimo_fila(matriz:array) -> None:
    # Buscamos el numero mas pequeño por fila y lo restamos al resto de valores
    for k, fila in enumerate(matriz):
        menor = min(fila)
        # Si el menor es 0 no hacemos nada, caso contrario remplazamos la fila por una nueva con la diferencia de valores
        if (menor != 0): matriz[k] = [valor - menor for valor in fila]


def eliminar_filas(matriz:array, coordenadas_eliminadas:list[list], intersecciones:list[list], invertir=False, cant_ceros=1) -> int:
    # Definimos una funcion que retorna la cantidad de ceros de una lista
    cal_ceros = lambda lista: sum(valor == 0 for valor in lista)

    # Definimos una variable que sea la cantidad de eliminaciones
    cant_eliminaciones = 0

    for k, filas in enumerate(matriz):
        # Si la contiene mas ceros que lo pedido iniciamos a borrar filas
        cant_ceros_interes = 0

        # Buscamos si hay ceros que no han sido eliminados
        for j, valor in enumerate(filas):
            coordenadas = [k, j] if not invertir else [j, k]
            if coordenadas not in coordenadas_eliminadas and valor == 0:
                cant_ceros_interes += 1

        # Si la cantidad de ceros que no han sido eliminados es mayor que el requisito los eliminamos
        if cant_ceros_interes > cant_ceros:
            for j in range(len(filas)):
                coordenadas = [k, j] if not invertir else [j, k]
                # Si la coordenada creada en la iteracion existe en las eliminadas es una interseccion
                if coordenadas in coordenadas_eliminadas:
                    intersecciones.append(coordenadas)
                else:
                    coordenadas_eliminadas.append(coordenadas)
            # Agregamos las eliminaciones
            cant_eliminaciones += 1
    
    return cant_eliminaciones


def minimo_valor(matriz:array, coordenadas_eliminadas:list[list]) -> float:
    # Definimos el mayor valor posible
    menor = 999999999

    for k, filas in enumerate(matriz):
        for j, valor in enumerate(filas):
            coordenadas = [k, j]
            # Si la coordenada actual no fue eliminada y el menor guardado es mayor que el valor lo remplazamos
            if coordenadas not in coordenadas_eliminadas and menor > valor: menor = valor

    return menor


def actualizar_valores(valor:float, matriz:array, coordenadas_eliminadas:list[list], intersecciones=list[list]):
    for k, fila in enumerate(matriz):
        new_fila = []
        for j, valor_columna in enumerate(fila):
            coordenadas = [k, j]
            # Si las coordenadas estan en las intersecciones sumamos el valor
            if  coordenadas in intersecciones:
                new_fila.append(valor_columna + valor)
            
            # Si la coordenada no fue eliminada lo restamos
            elif coordenadas not in coordenadas_eliminadas:
                new_fila.append(valor_columna - valor)
            
            # Si la coordenada fue eliminada lo guardamos normal
            else:
                new_fila.append(valor_columna)
        
        matriz[k] = new_fila


def metodo_hungaro(matriz:list[list]) -> array:
    # Restamos los valores minimos a cada fila
    matriz = array(matriz)
    restar_minimo_fila(matriz=matriz)
    
    # Trasponemos la matriz y aplicamos el mismo algoritmo
    matriz = transpose(matriz)
    restar_minimo_fila(matriz=matriz)

    # Trasponemos la matriz para volver a la original
    matriz = transpose(matriz)

    # Definimos esta variable de control de ciclo
    cant_eliminaciones = 0
    validar = False

    while cant_eliminaciones < len(matriz[0]):
        coordenadas_eliminadas = []
        coordenadas_intersecciones = []

        # Vamos eliminando las filas por iteraciones
        cant_eliminaciones = eliminar_filas(
            matriz=matriz,
            coordenadas_eliminadas=coordenadas_eliminadas,
            intersecciones=coordenadas_intersecciones,
            invertir=False,
            cant_ceros=1
        )
        
        # Trasponemos la matriz y aplicamos lo mismo solo que cambiando el orden
        matriz = transpose(matriz)
        cant_eliminaciones += eliminar_filas(
            matriz=matriz,
            coordenadas_eliminadas=coordenadas_eliminadas,
            intersecciones=coordenadas_intersecciones,
            invertir=True,
            cant_ceros=0
        )

        # Si la cantidad de eliminaciones es mayor la longitud de la matriz paramos
        if cant_eliminaciones >= len(matriz[0]) and validar:
            matriz = transpose(matriz)
            validar = False
            break
        
        # Devolvemos la matriz a su estado original
        matriz = transpose(matriz)

        menor_valor = minimo_valor(matriz=matriz, coordenadas_eliminadas=coordenadas_eliminadas)

        actualizar_valores(
            valor=menor_valor,
            matriz=matriz,
            coordenadas_eliminadas=coordenadas_eliminadas,
            intersecciones=coordenadas_intersecciones
        )
        validar=True

    # Si quedamos en medio de un ciclo la volvemos a la normalidad
    matriz = transpose(matriz) if validar else matriz

    # Retornamos la matriz resultante
    return matriz


def ordenar_metodo_hungaro(matriz:list[list]) -> array:
    # Inicializamos una matriz donde guardaremos las coordenadas de los costos/columnas que sean 0
    costos_ceros = []