
print('\n SISTEMA DE NOMBRES RAFAEL ALBERTI \n')

def nombre(respuesta :str ):
    while True:
    
        try: 

            print('Introduzca un nombre válido \n')
            respuesta=input('INTRODUZCA SU NOMBRE ---> ')
            int(respuesta)
            print('ERROR')
        except ValueError: #Sino se puede convertir la variable en tipo integer significa que string y por tanto, un texto

            print('ERROR')
            return respuesta

respuesta=0

print('Hola ' + nombre(respuesta))
