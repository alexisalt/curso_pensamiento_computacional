def factorial(n):
    """Calcula el factorial de n.
        n int > 0
        returns n!
    """
    if n == 1:
        return 1            #Este es el caso BASE, es necesario para evitar caer en un loop infinito o error"
                                   
    return n * factorial(n - 1)


n = int(input("Escribe un entero: "))

print(factorial(n))



