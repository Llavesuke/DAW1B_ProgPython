print('\n --------------------')
print('SISTEMA DE COBRO RAFAEL ALBERTI')
print('--------------------\n')

def check(horas): #función para evitar repetir la comprobación del numero introducido
 
 while True:

    try:
        horas= int(horas)
        return horas #Devolver el número obtenido en la función fuera de la misma
    except ValueError:
        horas= input('Introduzca un número válido -> ')
            
horas= input('Horas de trabajo: ')
horas= check(horas)

coste= input('Coste por hora: ')
coste= check(coste)

total= horas * coste
print('\n Pago -> ' , total , '\n')