from Semana_10.menu import ingresar_vector
from Semana_13 import Archivo

matrices = Archivo.leer('Matrices.json')

def leer_matriz():
    """
    Lee una matriz por teclado
    :return: (list of list of int) la matriz del usuario
    """
    resultado = []
    while True:
        entrada = input('Desea ingresar una fila? s/n ')
        if entrada == 'n':
            break
        resultado.append(ingresar_vector())
    return resultado

while True:

    MENU = """
    **********Menu**********
    0. Salir
    1. Ingresar Matriz
    2. Ver Matrices
    3. Matriz cuadrada
    4. Sumar matrices
    5. Producto escalar
    6. Multiplicar matrices
    ************************
    """

    seleccion = input(MENU)
    if seleccion == '0':
        print('Suerte')
        Archivo.guardar('Matrices.json', matrices)
        break
    elif seleccion == "1":
        nombre = input('cual es el nombre de su matriz ')
        matriz = leer_matriz()
        matrices[nombre[0]]=matriz
    elif seleccion == "2":
        print('Sus matrices')
        for matriz in matrices:
         print(matrices[matriz])
    elif seleccion == '3':
        print()
    elif seleccion == '4':
        print()
    elif seleccion == '5':
        print()
    elif seleccion == '6':
        print()
    else:
        print("Seleccion invalida")

