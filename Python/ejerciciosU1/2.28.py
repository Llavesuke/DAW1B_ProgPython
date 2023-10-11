"""
Inicio
    Escribe 'Numero 1-> '
    Lee num1
    Escribe 'Numero 2-> '
    Lee num2
    Mientras num1==num2 hacer
        Escribe 'Los dos numeros no pueden ser iguales'
        Escribe 'Numero 1-> '
        Escribe 'Numero 2-> '
        Si num1 > num2 entonces
            Escribe 'El numero menor es' , num2 , 'y entre ellos existen' , num1-num2 , 'numeros enteros'
            Si num2 > num1 
                Escribe 'El numero menor es' , num1 , 'y entre ellos existen' , num2-num1 , 'numeros enteros'

Fin
"""

print('------------------')
print('Numeros mayores')
print('------------------')

num1= int(input('Numero 1-> '))
num2= int(input('Numero 2-> '))

while num1==num2:
    print('Los dos numeros no pueden ser iguales')
    num1= int(input('Numero 1-> '))
    num2= int(input('Numero 2-> '))
if num1 > num2:
    print('\nEl numero menor es' ,num2 , 'y entre ellos existen' , num1-num2 , 'numeros enteros')
elif num2>num1:
    print('\nEl numero menor es' , num1 , 'y entre ellos existen' , num2-num1 , 'numeros enteros')