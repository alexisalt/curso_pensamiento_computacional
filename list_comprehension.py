#Generamos una nueva lista de un rango:

my_list = list(range(100))

print(my_list)

print(id(my_list))

#Secuencia del 0 al 99 contenida en las lista.

#Si queremos doblar esta lista

double = [i * 2 for i in my_list]

print(id(double))

print(double)

#Empleamos la notacion de 'list comprehension' donde 
#formularemos un for que recorra la lista mientras multiplica
#por 2 cada elemento de la lista

#Ahora para generar una lista de un rango solo de numeros pares,
#deberemos formular una condicion en linea de manera:

pares = [i for i in my_list if i % 2 == 0]

print(pares)

#Estoy clonando la lista my_list y filatrandola
