print('\n --------------------')
print('SISTEMA DE COBRO RAFAEL ALBERTI')
print('--------------------\n')

def total(horas:int,coste:int): #función para evitar repetir la comprobación del numero introducidoç
    horas= int(horas)
    coste= int(coste)
    return horas*coste
 
            
horas= input('Horas de trabajo: ')
coste= input('Coste por hora: ')



print('\n Pago -> ' , total(horas,coste) , '\n')