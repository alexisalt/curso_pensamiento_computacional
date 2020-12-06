# range(comienzo, final, pasos)
my_range = range(1, 5)
print(type(my_range))

for i in my_range:
    print(i)            #Igual que en la funcion Slices de 1 a 5 NO INCLUSIVO

#Re asignamos la variable my_range (apuntamos a otro pedazo de memoria con otro rango diferente)

my_range = range(0, 7, 2)
my_other_range = range(0, 8, 2)

print(my_range == my_other_range) # Por LC se puede hacer comparacion en linea #EVALUAMOS VALUE EQUALITY
                                    #Sorprendentemente es TRUE
print('Vamos a imprimir todos los valores de my_range')

for i in my_range:
    print(i)

print('Vamos a imprimir todos los valores de my_other_range') 

for i in my_other_range:
    print(i)


#Por esta razon la comparacion es TRUE.

print(id(my_range)) #Direccion en memoria donde esta el objeto rango 'my_range'

print(id(my_other_range)) #Direccion en memoria donde esta el objeto rango 'my_other_range

#Como podiamos esperar son diferentes objetos.

#Ahora chequeamos OBJECT EQUALITY empleares el operador logico 'is'

print('Evaluamos la igualda de objetos - OBJECT EQUILITY')

print(my_range is my_other_range)

#Son objetos DIFERENTES.

print('Generamos una secuencia de numeros pares del 0 al 100: ')

for i in range(0, 101, 2):
    print(i)


print('RETO: Imprime todos los numeros nones (impares) del 1 al 99: ')

for i in range(1, 100, 2):
    print(i)
    