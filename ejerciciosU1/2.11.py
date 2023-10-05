print('------------------')
print('SUMA MADE IN RAFAEL ALBERTI')
print('------------------')

while True:

 n= input('Introduce un entero positivo -> ')

 try:
    n= int(n)
    if n >= 0:
        lista= []
        for suma in range (1,n+1):
         lista.append(suma)
        print(lista)
         
        print('\n')
        break
    else:
        print('\n Has introducido un número negativo \n ')

 except ValueError:
    
    print('\n Has introducido texto, prueba otra vez \n')