# PROGRAMA PARA SOLUCIONAR PROBLEMAS DE TRANSPORTE Y ASIGNACION
### Realizado por Sebastián Medina y José Pineda

## Problemas de Transporte
## Problema de transporte 1
### Matriz de datos:
            Destino 1       Destino 2       Destino 3       Destino 4       Oferta  
            10.0            2.0             20.0            11.0            15.0    
            12.0            7.0             9.0             20.0            25.0    
            4.0             14.0            16.0            18.0            10.0    
    Demanda 5.0             15.0            15.0            15.0

### Resultados:
        Destino 1       Destino 2       Destino 3       Destino 4
        5.0             10.0            None            None
        None            5.0             15.0            5.0
        None            None            None            10.0

### Costos:
        Cantidad        Costo   Costo total
        5.0             10.0    50.0
        10.0            2.0     20.0
        5.0             7.0     35.0
        15.0            9.0     135.0
        5.0             20.0    100.0
        10.0            18.0    180.0
        Total: 520.0

## Problema de transporte 2
### Matriz de datos:
            Destino 1       Destino 2       Destino 3       Oferta
            5.0             2.0             3.0             100.0
            8.0             4.0             3.0             300.0
            9.0             7.0             5.0             300.0
    Demanda 300.0           200.0           200.0

### Resultados:
        Destino 1       Destino 2       Destino 3
        100.0           None            None
        200.0           100.0           None
        None            100.0           200.0

### Costos:
        Cantidad        Costo   Costo total
        100.0           5.0     500.0
        200.0           8.0     1600.0
        100.0           4.0     400.0
        100.0           7.0     700.0
        200.0           5.0     1000.0
        Total: 4200.0

## Problema de transporte 3
### Matriz de datos:
            Destino 1       Destino 2       Destino 3       Oferta
            30.0            50.0            60.0            110.0
            70.0            80.0            35.0            90.0
            90.0            20.0            40.0            150.0
    Demanda 80.0            170.0           100.0

### Resultados:
        Destino 1       Destino 2       Destino 3
        80.0            30.0            None
        None            90.0            None
        None            50.0            100.0

### Costos:
        Cantidad        Costo   Costo total
        80.0            30.0    2400.0
        30.0            50.0    1500.0
        90.0            80.0    7200.0
        50.0            20.0    1000.0
        100.0           40.0    4000.0

## Solución de los problemas de asignacion
## Problema 1
### Matriz de resultados:
            Puesto 1        Puesto 2        Puesto 3
    Trab 1  0.0             1.0             0.0
    Trab 2  1.0             2.0             0.0
    Trab 3  0.0             0.0             6.0

### Costos:
    Trab 1: 3.0
    Trab 3: 0.0
    Trab 2: 0.0
    Total:  3.0

## Problema 2
### Matriz de resultados:
            Puesto 1        Puesto 2        Puesto 3
    Trab 1  6.0             0.0             0.0
    Trab 2  0.0             5.0             1.0
    Trab 3  2.0             3.0             0.0

### Costos:
    Trab 2: 9.0
    Trab 1: 10.0
    Trab 3: 8.0
    Total:  27.0