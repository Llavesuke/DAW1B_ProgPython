print('------------------')
print('CONTADOR CARACTERES RAFAEL ALBERTI')
print('------------------') 

nombre= input('¿Cual es tu nombre? -> ')
try:
    float(nombre)
    print('Introduce un texto válido')

except ValueError:

    print('\n',nombre.upper(), 'tiene', len(nombre), 'letras')