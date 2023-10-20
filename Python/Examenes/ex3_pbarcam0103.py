"""
Escribe un programa en Python que lea una palabra y la encripte:

    1. Pedir la palabra hasta que cumpla que tiene un mínimo de 8 letras.
    
    2. Después, transformar o encriptar la palabra de la siguiente manera:
        - Sin bucles, pero escribiendo varias instrucciones si lo necesitáis.
        - Eliminar espacios.
        - Consonantes a mayúsculas
        - La vocal a pasa a ser una @.
        - La vocal e pasa a ser un 3.
        - La vocal i pasa a ser un 1.
        - El resto de vocales serán minúsculas.
        - Si tiene solo 8 letras, añade un * al principio y un # al final.

    3. Ejemplos:

    > Introduzca una palabra: Pedro PAblO    1984
    > Su palabra encriptada es P3DRoP@BLo1984

    > Introduzca una palabra: ArIADNa2
    > Su palabra encriptada es *@R1@DN@2#

    > Introduzca una palabra: USER       89
    > Introduzca una palabra *mínimo 8 letras*: USER  893465
    > Su palabra encriptada es uS3R893465

"""

print('-----------')
print('ENCRIPTACION')
print('-----------')

respuesta= input('Introduzca una palabra -> ')
respuesta= respuesta.replace(' ','')#eliminamos los espacios que haya podido introducir el usuario para solo contar las letras

while len(respuesta)<8:
    respuesta= input('Introduzca una palabra *minimo de 8 letras* -> ')

respuesta=respuesta.upper() #ya transformo las consonantes a mayusculas y cambio las que tengan unicamente las que tengan una regla

if 'A' in respuesta[0:len(respuesta)]:
    respuesta=respuesta.replace('A','@')

if 'E' in respuesta[0:len(respuesta)]:
    respuesta=respuesta.replace('E','3')

if 'I' in respuesta[0:len(respuesta)]:
    respuesta=respuesta.replace('I','3')

if 'O' in respuesta[0:len(respuesta)]:
    respuesta=respuesta.replace('O','o')

if 'U' in respuesta[0:len(respuesta)]:
    respuesta=respuesta.replace('U','u')

if len(respuesta) ==8:
    print('*',end='')
    print(respuesta,end='')
    print('#',end='')
    print('\n')
else:
    print(respuesta, '\n')