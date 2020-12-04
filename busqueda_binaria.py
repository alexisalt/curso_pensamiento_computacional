objetivo = int(input('Escoge un numero: '))
epsilon = 0.01
bajo = 0.0
alto = max(1.0, objetivo) #La funcion max me devuelve el valor mas alto entre dos. Si el objetivo es menor a 1, debe devolver 1 al menos.
respuesta = (alto + bajo) / 2
contador = 0

while abs(respuesta**2 - objetivo) >= epsilon:
    print(f'bajo: {bajo}, alto: {alto}, respuesta: {respuesta}, iteracion nro: {contador}')
    if respuesta**2 < objetivo:
        bajo = respuesta
    else:
        alto = respuesta
    
    respuesta = (alto + bajo) / 2

    contador += 1

print(f'La raiz cuadrada de {objetivo} es {respuesta}')
