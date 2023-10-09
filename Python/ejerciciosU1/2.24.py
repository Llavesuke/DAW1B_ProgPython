print('------------------')
print('DINERO EXPOSE RAFAEL ALBERTI')
print('------------------') 


precio=input('Introduce el precio del producto ej (1.99) -> ')
try:
    float(precio)
    precio= precio.split('.')
    print(precio[0]+' euros')
    print(precio[1]+' centimos')
except ValueError:
    print('Formato erroneo')