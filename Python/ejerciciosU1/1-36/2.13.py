print('------------------')
print('DIVISIÓN RAFAEL ALBERTI')
print('------------------')

while True:
    try:
        numero1= int(input('Introduce el primer número -> '))
        numero2= int(input('Introduce el segundo número -> '))

        cociente= numero1/numero2
        resto= numero1%numero2
        
        print('La división entre', numero1, 'entre' , numero2, 'da un cociente', cociente , 'y un resto', resto)
    
    except ValueError:
        print('\nNúmero invalido\n')