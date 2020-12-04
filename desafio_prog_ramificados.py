import time

print('Hola, por favor indica tu nombre y tu edad a continuacion...')

my_name_1 = input('Escribe tu nombre: ')

my_age_1 = int(input('Escribe tu edad por favor: '))

print('Muy bien, ahora que tu amigo escriba su nombre y edad: ')

my_name_2 = input('Escribe tu nombre y veremos: ')

my_age_2 = int(input('Escribe tu edad ahora y veremos si eres mayor que tu amigo!!! :'))

print(' Calculando...')

time.sleep(5)

if my_age_1 > my_age_2:
    print(f'FELICIDADES {my_name_1} tu tienes {my_age_1} y tu eres mas grande que {my_name_2} que tiene solo {my_age_2}')
elif my_age_1 < my_age_2:
    print(f'LO LAMENTO!, pero tu amigo {my_name_2} tiene {my_age_2} y es mayor que tu')
else:
    print('QUE DIFICIL!!! Ambos tienen la misma edad')    


