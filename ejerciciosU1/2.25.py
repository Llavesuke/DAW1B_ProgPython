print('------------------')
print('FECHAS RAFAEL ALBERTI')
print('------------------')

fecha=input('Fecha dd/mm/aaaa -> ')
fecha=fecha.split('/')

try:

    Dia=int(fecha[0])
    Mes=int(fecha[1])
    Año=int(fecha[2])

    if Dia >= 0 and Dia <= 31:
        print('Dia -> '+fecha[0])
    if Dia < 0 or Dia > 31:
        print('Dia invalido')
    if Mes >=1 and Mes <=12:
        print('Mes -> '+fecha[1])
    if Mes <1 or Mes >12:
        print('Mes invalido')
    if Año >1910 and Año <=2023:
        print('Año -> '+fecha[2])

except Exception:
    print('Numero no introducido')
