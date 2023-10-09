print('------------------')
print('JUGUETERIA RAFAEL ALBERTI')
print('------------------')

while True:
    try:
        payasos=int(input('¿Cuantos payasos van en el paquete? -> '))
        muñecas=int(input('¿Cuantas muñecas van en el paquete -> '))
        print('\nPeso payasos (g)-> ', payasos*112, '\nPeso muñecas (g) ->' , muñecas*75, '\n\nPeso total -> ', payasos*112+muñecas*75)
        break
        


    except ValueError:

        print('Número introducido invalido')

