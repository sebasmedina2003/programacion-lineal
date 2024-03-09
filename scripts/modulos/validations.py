from re import search

REG_NUMBER = '^[1-9]{1}[0-9]*$'              # Validamos que el primer numero no sea 0 y lo consiguiente sea cualquiera
REG_FLOAT = '^([0-9])+(\\.{1}[0-9]+)*$'      # Validamos que el haya una secuencia de numeros con un punto con mas numeros

def lectura(reg_ex:str) -> str:
    var = ''
    while(not search(reg_ex, var)): var = input('-> ')
    return var