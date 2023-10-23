print('------------------')
print('IDENTIFICADOR RAFAEL ALBERTI')
print('------------------') 

nombre=input('Introduce tu nombre completo -> ')
contador=nombre.split()
if len(contador) == 3:

    try:
        float(nombre)
        print('No puedes introducir numeros como nombres')

    except ValueError:
    
        print(nombre.upper())
        print(nombre.lower())
        print(nombre.title())
else:
    print('\nNo has introducido el nombre completo')