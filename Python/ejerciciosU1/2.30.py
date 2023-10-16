"""
Inicio

    Escribe 'Numero de inicio -> '
    Lee inicio
    Escribe 'Numero de incremento -> '
    Lee incremento
    Escribe 'Numero total de la serie -> '
    Escribe total
    contador=0

    Mientras incremento < 0 o total < 0 hacer
        Escribe 'Introduce un numero de incremento valido -> '
        Lee incremento
        Escribe 'Introduce un numero total de la serie -> '
        Lee total

    Escribe 'Serie' + inicio + '-'
    Mientras contador != total-2 hacer
        contador= contador + 1
        inicio = incremento + 1
        Si contador != 2 entonces
            Escribe '...'

Escribe '-'
inicio = inicio + incremento
Escribe 'inicio'


Fin
"""

print('------------------')
print('LISTA INCREMENTADA')
print('------------------')

inicio= int(input('Numero de inicio de la serie -> '))
incremento= int(input('Cada cuanto incrementara la serie -> '))
total= int(input('Cuantos números tendra-> '))
contador= 0

while incremento < 0 or total < 0:
    incremento= int(input('\nCada cuanto incrementara la serie -> '))
    total= int(input('Cuantos números tendra -> '))

print('\nSerie ->'+str(inicio)+'-',end='')
while contador != total-2:
        contador += 1
        inicio += incremento
        print(inicio, end='')
        if contador != total-2:
            print('...', end='')

print('-', end='')
inicio += incremento
print(inicio, end='')

print('\n')
