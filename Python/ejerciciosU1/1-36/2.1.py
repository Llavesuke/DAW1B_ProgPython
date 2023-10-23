
print('\n SISTEMA DE NOMBRES RAFAEL ALBERTI \n')

Nombre=input('INTRODUZCA SU NOMBRE ---> ')

while True:
    
    try: 
        int(Nombre)

        print('Introduzca un nombre válido \n')
        Nombre=input('INTRODUZCA SU NOMBRE ---> ')

    except ValueError: #Sino se puede convertir la variable en tipo integer significa que string y por tanto, un texto

        print('Hola', Nombre)
        break