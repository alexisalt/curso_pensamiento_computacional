objetivo = int(input("Ingresa un numero: "))

epsilon = 0.01 #Error permitidio o admisible
paso = epsilon**2
respuesta = 0.0
contador= 0
#Esta ultima condicion se pone para evitar que el objetivo sea negativo En ese caso se sumarian ambos terminos y nunca seria menores a epsilon (bucle infinito)
while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    respuesta += paso
    contador += 1
    print(f'Interacion nro:{contador} solucion iterada: {respuesta} error(e): {abs(respuesta**2 - objetivo)}')

if abs(respuesta**2 - objetivo) >= epsilon:
    print(f'No se encuentra solucion a {objetivo}')
else:
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')
 
                                        
    
