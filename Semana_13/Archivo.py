import json

diccionario={
    'hola' : 'mundo',
    'jose' : 'cordoba',
    'programacion' : 'ean'
}

def guardar(nombre_archivo, diccionario_a_guardar):
    """
    (str,dict)->boolean
    :param nombre_archivo:
    :param diccionario_a_guardar:
    :return:
    """
    try:
        archivo = open(nombre_archivo,"w")
        convertido = json.dumps(diccionario_a_guardar)
        archivo.write(convertido)
        archivo.close()
        return True
    except:
        return False

def leer(nombre_archivo):
    '''
    (str)->dict...
    :param nombre_archivo:
    :return:
    '''
    try:
        archivo = open(nombre_archivo, 'r')
        diccionario_leido = json.load(archivo)
        archivo.close()
        return diccionario_leido
    except:
        return {}
if __name__=='__main__':
    nombre_archivo = 'prueba.json'
    print(guardar(nombre_archivo, diccionario))


