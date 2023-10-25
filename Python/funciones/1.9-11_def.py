print('------------------')
print('SUMA MADE IN RAFAEL ALBERTI')
print('------------------')

def suma():
    n= input('Introduce un entero positivo -> ')
    n= int(n)
    if n >= 0:
        lista= []
        for suma in range (1,n+1):
         lista.append(suma)
        print(lista)
         
        print('\n')
    
print('La suma de los numeros es {}'.format(suma()))
