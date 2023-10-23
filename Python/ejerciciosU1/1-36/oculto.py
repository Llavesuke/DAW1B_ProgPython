import random #libreria para utilizar funciones

intento= 1
oculto = random.randint(1,100) #función de la librería random

respuesta= int(input("\n Introduce un número del 1 al 100 -> "))

while (respuesta!=oculto and (respuesta < 1 or respuesta > 100)): #mientras la respuesta sea distinta del valor del número oculto o menor que uno o mayor que 100, 
                                                                  #seguira el bucle
     intento= intento+1
     print('\n Incorrecto')
     if (respuesta > oculto):
        print('Tu numero es mayor que el número oculto \n')
     else: 
        print('Tu numero es menor que el número oculto \n ')
     respuesta= int(input("Introduce otro número de 1 a 100-> "))

print('\nCorrecto \n') 
if(intento==1): #condicional para que la respuesta sea en singular o plural
 print('Has tardado 1 intento \n')
else:
 print('Has tardado ' + str(intento) + ' intentos \n')
