
def resultado(importe: float, iva: int):
    print(importe + (importe*(iva/100)))
    importe= float(input('Introduce el importe sin iva -> '))
    iva= int(input('Introduce el IVA a aplicar (ejemplo 10%) -> '))

importe= float(input('Introduce el importe sin iva -> '))
iva= int(input('Introduce el IVA a aplicar (ejemplo 10%) -> '))

resultado(importe,iva)