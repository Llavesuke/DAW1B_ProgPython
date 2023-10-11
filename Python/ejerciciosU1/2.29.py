"""
Inicio

    Escribe 'Nombre -> '
    Lee nombre
    Escribe 'Edad -> '
    Lee edad
    Mientras edad < 0 or edad > 125 hacer 
        Escribe 'Edad invalida, introduzca una correcta -> '
        Lee edad
    Si nombre == '' entonces
        Escribe 'Te llamas Desconocido y tienes' , edad, 'te quedan', 125-edad , 'por cumplir'
    Sino 
        Escribe 'Te llamas', nombre,  'y tienes' , edad, 'te quedan', 125-edad , 'por cumplir'

Fin
"""

print('------------------')
print('Nombres y edades')
print('------------------')

nombre= input('Nombre -> ')
edad= int(input('Edad -> '))

while edad < 0 or edad > 125:
    edad= int(input('Edad invalida, introduzca una correcta -> '))
if nombre == '':
    print('Te llamas Desconocido y tienes', edad , 'te quedan' , 125-edad, 'por cumplir')
else:
    print('Te llamas', nombre,  'y tienes' , edad, 'te quedan', 125-edad , 'por cumplir')