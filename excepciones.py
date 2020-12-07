
#def divide_elementos_de_lista(lista, divisor):
    #return [i / divisor for i in lista]


#lista = list(range(10))
#divisor = 0

#print(divide_elementos_de_lista(lista, divisor))

#Si tratamos de dividir por cero, tenemos una excepcion:
#ZeroDivisionError: division by zero
#ESto implica que el programa crasheo. Para evitar que esto suceda a nivel de usuario,
#y para tener control sobre el uso de la funcion, podemos utilizar programacion defensiva
#con las keyword 'try' y 'except':

def divide_elementos_de_lista(lista, dividor):
    try:
        return [i / divisor for i in lista]
    except ZeroDivisionError as e:
        print(e)
        return lista

lista = list(range(10))
divisor = 0

print(divide_elementos_de_lista(lista, divisor))

#En este caso en primer lugar, con try intentara ejecutar la division
#sin embargo, si por alguna razon surge la excepcion de ZeroDivisionError,
#se le pide que retorne simplmente la lista para evitar el codigo de error y el crasheo.
#Esto evidenciaria al usuario un error pero sin tirar abajo el programa.
#De esta manera se hace el manejo de las excepciones.

