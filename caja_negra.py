#Se empleara POO con clases en este codigo.
import unittest #Modulo de Python que nos permite generar pruebas.
def suma(num_1, num_2):
    return num_1 + num_2               #Es un placeholder que se emplea en Python para dejar vacio.

#La forma en que nos permite realizar pruebas es con una clase que definimos de la siguiente manera:
class CajaNegraTest(unittest.TestCase): #Caso de prueba
    def test_suma_dos_positivos(self):
        num_1 = 10
        num_2 = 5

        resultado = suma(num_1, num_2)

        self.assertEqual(resultado, 15)
    def test_suma_dos_negativos(self):
        num_1 = -10
        num_2 = -7

        resultado = suma(num_1, num_2)

        self.assertEqual(resultado, -17)


#Esta forma se denomina test driven development en donde antes de escribir
#la funcion, vamos a escribir las pruebas que nosotros esperamos de esta funcion.
#En este caso seria la funcion de suma. Cuando nosotros queremos plantear nuestras pruebas
#podemos planearnos cuales son los casos posibles de uso de tal funcion.
# - Dos positivos
# - Dos negativos
# - Un negativo y un positivo

#Al correr el test:
# 1. error: debido a que la funcion suma no esta definida.
# 2. error: la funcion suma no tiene ningun argumento.
# 3. error: Nos dice que NONE != 15. Porque la funcion esta vacia.
# 4. OK. El programa funciona OK.

#Porque una vez que tenemos un test funcionando, tenemos la garantia
#que si alguna vez se modifica algo en esta funcion, nuestro test de suite nos
#va a alertar del error o bug existente.S


if __name__ == '__main__':
    unittest.main()

