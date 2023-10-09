print('\n --------------------')
print('SUMA DE NUMEROS')
print('--------------------\n')

def respuesta(check):
 while True:
    try:

     check= int(check)
     return check
    
    except ValueError:
      
      check= input('Introduzca un número valido-> ')

numero1= input('Introduce un número -> ')
numero1= respuesta(numero1)

numero2= input('Introduce un número -> ')
numero2= respuesta(numero2)

numero3= input('Introduce un número -> ')
numero3= respuesta(numero3)

suma= numero1+numero2+numero3
print('\n La suma de los tres números es -> ' , suma , '\n')