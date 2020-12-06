a = [1, 2, 3]
print(id(a))
b = a
print(id(b))
#Aplicando un metodo de las list:
c = list(a)
print(id(c))

#Observamos que el id de a y b son iguales. Sin embargo c es una lista con
#un id diferente aunque con los mismos objetos.
#Otra forma de clonar a es con slices:

d = a[::]
print(d)

