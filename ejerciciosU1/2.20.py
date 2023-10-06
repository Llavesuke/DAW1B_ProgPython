print('------------------')
print('TELEFONO RAFAEL ALBERTI')
print('------------------') 

numero=input('Introduce un numero con el formato (+34-111111111-00) -> ')
contador=numero.split('-')
if len(numero)== 16 and numero[0] == '+':
    if len(contador[1]) == 9:
        print(contador[1])  
else:
    print('Formato incorrecto')



