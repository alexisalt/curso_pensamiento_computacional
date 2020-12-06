my_dict = {
    'David' : 35, #Se denominan llaves del diccionario (componentes del diccionario)
    'Erika' : 32,
    'Jaime' : 50,
}

#Como observamos es muy parecida a struct del lenguaje C. Nos permite estructurar una cantidad de datos y variables juntas.

print(my_dict['David'])

#Si no sabemos que llaves tiene el diccionario y evitar errores,
#empleamos el metodo GET.

print(my_dict.get('Juan', 30))
#Le estamos diciendo que si existe Juan devuelva el valor correspondiente,
#de lo contrario puede usar el valor de 30 que le damos a la funcion

#Podemos reasignar una llave del diccionario:

my_dict['Jaime'] = 20

print(my_dict['Jaime'])

#Si queremos imprimir toda la estructura:

print(my_dict)

#Si queremos acceder a una nueva llave en este diccionario:

my_dict['Pedro'] = 70

print(my_dict)

#Para eliminar una llave se utiliza 'del':

del my_dict['Jaime']

print(my_dict)

### Iteracion en Diccionarios ###

#Iterar por llave en todo el diccionario:
for llave in my_dict.keys(): #Empleo el metodo 'keys'
    print(llave)
#Iterar por valores en todo el diccionario:

for valor in my_dict.values():
    print(valor)

#Iterar por valores y llave:

for llave, valor in my_dict.items():
    print(llave, valor)

#A menudo es necesario saber si existe una llave en el diccionario con una comparacion logica:

print('David' in my_dict)
#Devuelve True

print('Tomas' in my_dict)
#Devuelve False



