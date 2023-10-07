print('\n --------------------')
print('SUMA DE NUMEROS')
print('--------------------\n')

def respuesta(check):
 while True:
    try:

     check= float('{:.2f}'.format(float(check))) #Redondea a dos decimales la función en cuestión
     return check
    
    except ValueError:
      
      check= input('Introduzca un número valido-> ')

numero1= input('Introduce un número -> ')
numero1= respuesta(numero1)

numero2= input('Introduce un número -> ')
numero2= respuesta(numero2)

numero1= numero1 + numero2

numero2= input('Introduce un número -> ')
numero2= respuesta(numero2)
 
numero1= numero1 + numero2

print('Resultado -> ' , numero1)