print('------------------')
print('CESTA RAFAEL ALBERTI')
print('------------------')

cesta=input('Introduce la lista de la compra separados por , -> ')
cesta=cesta.split(',')
contador=len(cesta)
for contador in range(0,contador):
    print('Producto',contador+1, '-> ', cesta[contador])


