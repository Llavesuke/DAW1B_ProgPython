print('\n --------------------')
print('TEMPERATURA MADE IN RAFAEL ALBERTI')
print('--------------------\n')



while True:
  
 
 try:
    temperatura= float(input('Introduce una temperatura (en ºC) -> '))
    fahrenheit = temperatura * 1.8 + 32
    print('La temperatura en grados fahrenheit es -> {:.2f}'.format(fahrenheit),(('({:.2f}''ºC)').format(temperatura)))
    break

 except ValueError: #Si el bloque try da un error, es que la variable temperatura no puede ser convertida en float y 
                    #por tanto se pide la entrada de variable otra vez
    print('Temperatura introducida erronea')