"""
Inicio

    Escribe 'Numero de inicio -> '
    Lee inicio
    Escribe 'Numero de incremento -> '
    Lee incremento
    Escribe 'Numero total de la serie -> '
    Escribe total

    Mientras incremento < 0 o total < 0 hacer
        Escribe 'Introduce un numero de incremento valido -> '
        Lee incremento
        Escribe 'Introduce un numero total de la serie -> '
        Lee total


    Mientras inicio < total+1
        Escribe 'inicio = "incremento" + 1'


Fin
"""

print('------------------')
print('LISTA INCREMENTADA')
print('------------------')

inicio= int(input('Numero de inicio de la serie -> '))
incremento= int(input('Cada cuanto incrementara la serie -> '))
total= int(input('Con que numero acabara la serie -> '))


while incremento < 0 or total < 0:
    incremento= int(input('\nCada cuanto incrementara la serie -> '))
    total= int(input('Con que numero acabara la serie -> '))

frase= 'Serie -> '

while inicio < total:
    print(frase , inicio , '...')
    if inicio >= total:
        print('-', end='')
    inicio += incremento
    
print('\n')
