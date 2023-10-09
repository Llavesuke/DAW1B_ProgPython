print('------------------')
print('CUENTA DE AHORROS RAFAEL ALBERTI')
print('------------------')


while True:
    try:
        depositado= float(input('Dinero depositado -> '))
        for i in range (1,4):
            print('Año', i, '->' , '{:.2f}'.format(i*depositado*0.04))
        break
    except ValueError:

        print('Número invalido')
            
        