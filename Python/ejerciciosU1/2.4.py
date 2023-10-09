print('\n --------------------')
print('TEMPERATURA MADE IN RAFAEL ALBERTI')
print('--------------------\n')


temperatura= input('Introduce una temperatura (en ºC) -> ')


while True:
  
 
 try:

    fahrenheit = float(temperatura) * 1.8 + 32
    print('La temperatura en grados fahrenheit es -> ' , fahrenheit)
    break

 except ValueError: #Si el bloque try da un error, es que la variable temperatura no puede ser convertida en float y 
                    #por tanto se pide la entrada de variable otra vez
    temperatura= input('Introduce una temperatura (en ºC) -> ')