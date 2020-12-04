numero = int(input("Escribe un numero: "))

respuesta = 0

while respuesta**2 < numero:
    print(f'Intento nro {respuesta +1}')
    respuesta += 1

if respuesta**2 == numero:
    print(f'El numero {numero} tiene raiz cuadrada entera y es: {respuesta}')
else:
    print(f'El numero {numero} NO tiene raiz cuadrada entera')

#Este programa nos muestra el poder de lo que es la enumeracion exhaustiva. Es uno de los algoritmos
# de busqueda mas simples que existen pero mas importantes. Aprovechamos el poder de la PC
# de computar gran cantidad de iteraciones que para nosotros seria imposible de resolver en un tiempo
# razonable, es por esto que deberia ser uno de los primeros algoritmos a emplear para resolver un problema.