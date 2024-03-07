from re import search

def lectura(reg_ex:str) -> str:
    var = ''
    while(not search(reg_ex, var)): var = input('-> ')
    return var


def mostrar_matriz(matriz:list[list[float]], ofertas=[], demandas=[]) -> None:    
    # Imprimimos el encabezado de la tabla
    for k in range(len(matriz[0])):
        print(f'\tDestino {k+1}', end='')
    print('\tOferta')

    # Imprimimos los valores de la tabla
    for j, fila in enumerate(matriz):
        for valor in fila:
            print(f'\t{valor}', end='\t')

        print(f'\t{ofertas[j]}')
    
    print('Demanda ', end='')
    for valores in demandas:
        print(f'{valores}', end='\t\t')

    print('')


def esquina_noroeste(matriz:list[list[float]], ofertas:list[float], demandas:list[float]) -> list[dict]:
    resultados = []
    columnas_resueltas = []
    filas_resueltas = []

    for fila, lista in enumerate(matriz):
        for columna in range(len(lista)):

            if(columna not in columnas_resueltas and fila not in filas_resueltas):

                if(ofertas[fila] > demandas[columna]):
                    resultado = {
                        'valor': demandas[columna],
                        'coordenada': [fila, columna]
                    }
                    columnas_resueltas.append(columna)
                    resultados.append(resultado)

                    ofertas[fila] -= demandas[columna]
                    demandas[columna] = 0
                
                elif(demandas[columna] > ofertas[fila]):
                    resultado = {
                        'valor': ofertas[fila],
                        'coordenada': [fila, columna]
                    }
                    filas_resueltas.append(fila)
                    resultados.append(resultado)

                    demandas[columna] -= ofertas[fila]
                    ofertas[fila] = 0
                
                else:
                    resultado = {
                        'valor': ofertas[fila],
                        'coordenada': [fila, columna]
                    }
                    filas_resueltas.append(fila)
                    columnas_resueltas.append(columna)

                    resultados.append(resultado)

                    ofertas[fila] = 0
                    demandas[columna] = 0

    return resultados


def mostrar_matriz_resultante(resultados:list[dict], ofertas: int, demandas:int) -> None:

    for k in range(demandas):
        print(f'\tDestino {k+1}', end='')
    print('')
    
    for k in range(ofertas):
        for j in range(demandas):
            encontrado = False
            for resultado in resultados:
                if(resultado['coordenada'] == [k,j]):
                    print(f'\t{resultado['valor']}', end='\t')
                    encontrado = True
            
            if not encontrado:
                print(f'\tNone', end='\t')
        print('')