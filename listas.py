my_list = [1, 2, 3]

print(my_list[0])

print(my_list[1:])

#Veremos ahora los metodos de las listas y sus side-effects

my_list.append(4)
print(my_list)
#NO EXISTIO una reasignacion, simplemente la modificamos a la lista
#agreganndole el numero 4 al final.

#modificar ahora una de las posiciones

my_list[0] = 'a' #A diferencia de otros lenguajes Python permite mezclar tipo de datos
print(my_list)

my_list.pop()

print(my_list)

#El metodo pop elimina el ultimo objeto de la lista.

print('Tambien se puede iterar con las listas')

for element in my_list:
    print(element)
print('Efectos secundarios')

a = [1, 2, 3]
b = a
#Lo que estamos haciendo aqui es asignar a 'b' la lista de 'a'
#quiere decir que estamos apuntando las dos variables al mismo lugar en memoria.
print(id(a))
print(id(b))

#Por ejemplo si queremos generar una lista de listas:

c = [a, b]
print(c)

# Si al avanzar por el programa olvidamos que generamos un alias (b) y empleamos el metodo append:

a.append(5)

print(a)

#Verifiquemos:

print(c)

#Como vemos se modificaron ambas listas, porque se modifico el mismo espacio de memoria
#y dado que b apunta al mismo lugar que a, el cambio tambien se produjo sobre b. 
#Para que esto no ocurra es mejor generar a 'b' como una lista independiente con su propio espacio de memoria.

b = [1, 2, 3]
print(b)

#Por esta razon usualmene se prohiben utilizar tipo de datos mutables y en cambio se utiliza
#el metodo de clonacion para generar una copia. Se vera en un archivo diferente