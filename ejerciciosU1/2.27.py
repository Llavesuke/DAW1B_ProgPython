print('------------------')
print('PRODUCTOS RAFAEL ALBERTI')
print('------------------')

nombre=input('Nombre del producto -> ')
precio=float(input('Precio del producto -> '))
unidades=int(input('Numero de unidades -> '))

print(nombre+' cuesta c/u','{:09.2f}'.format(precio), 'habiendo', '{:03d}'.format(unidades), 'todo esto cuesta', '{:011.2f}'.format(precio*unidades))
