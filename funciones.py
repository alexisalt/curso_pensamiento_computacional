def enumeracion_exhaustiva(objetivo):
    respuesta = 0

    while respuesta**2 < objetivo:
        respuesta += 1

    if respuesta**2 == objetivo:
        return respuesta
    else:
        return -1

def aproximacion_soluciones(objetivo):
    respuesta = 0.0
    epsilon = 0.01
    paso = epsilon**2

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:

        respuesta += paso

    if abs(respuesta**2 - objetivo) >= epsilon:
        return -1
    else:
        return respuesta

def busqueda_binaria(objetivo):
    
    epsilon = 0.01
    alto = max(1.0, objetivo)
    bajo = 0.0
    respuesta = (alto + bajo) / 2

    while abs(respuesta**2 - objetivo) >= epsilon:
    
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta
        
        respuesta = (alto + bajo) / 2
    
    return respuesta



objetivo = int(input("Ingresa un numero: "))
opcion = int(input(f'Selecciona el metodo de busqueda que desea utilizar: 1. Enumeracion Exhaustiva 2. Aprox. de soluciones 3. Busqueda Binaria: '))

if opcion == 1:
    result = enumeracion_exhaustiva(objetivo)
    if result ==-1:
        print(f'No se encuentra solucion con el metodo')
    else:
        print(f'La raiz cuadrada de {objetivo} es: {result}')
elif opcion == 2:
    result = aproximacion_soluciones(objetivo)

    if result == -1:
        print(f'No se halla solucion con este parametro de error valido o usted intenta emplear un numero negativo')
    else:
        print(f'La raiz cuadrada de {objetivo} con el metodo de A.S es: {result}')
else:
    result = busqueda_binaria(objetivo)

    if result == -1:
        print(f'No se halla solucion con este parametro de error valido o usted intenta emplear un numero negativo')
    else:
        print(f'La raiz cuadrada de {objetivo} con el metodo de B.B es: {result}')



