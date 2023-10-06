print('------------------')
print('PANADERÍA RAFAEL ALBERTI')
print('------------------')


while True:
    
    try:
        pan=3.49
        panantiguo= int(input('¿Cuántas barras vendidas hoy no son del día? -> '))
        total=panantiguo*(pan*0.60)
        print('Precio de una barra -> ', pan)
        print('Descuento (60%) -> ', pan*0.60)
        print('Precio de todas las barras que no son frescas -> ' , '{:.2f}'.format(total), '\n')
        break
        



    except ValueError:
        print('Valor introducido erroneo')