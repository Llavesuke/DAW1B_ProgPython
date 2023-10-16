print('\n --------------------')
print('TEMPERATURA MADE IN RAFAEL ALBERTI')
print('--------------------\n')

def conversion():
    temperatura= input('Introduce una temperatura (en ºC) -> ')
    temperatura=float(temperatura) * 1.8 + 32
    return temperatura

print('La temperatura en Farenheit es {:.2f}'.format(conversion()))