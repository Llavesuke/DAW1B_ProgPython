print('------------------')
print('NOMBRES * N RAFAEL ALBERTI')
print('------------------')

try:
    nombre=input('¿Cual es tu nombre -> ')
    try:
        while type(int(nombre)) == int:
            print('Introduce un nombre válido')
        
    except ValueError:
        veces=int(input('Cuantas veces quieres que salga tu nombre por pantalla -> '))

        while veces == 0:
            print('Debe de imprimirse al menos una vez')
            veces=int(input('Cuantas veces quieres que salga tu nombre por pantalla -> '))

        for veces in range(1,veces+1):
            print(veces, '-> ', nombre)

except ValueError:
    print('Error')