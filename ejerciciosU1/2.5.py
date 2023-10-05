print('\n --------------------')
print('CALCULADORA DE IVA')
print('--------------------\n')

def respuesta(iva):
 while True:
    try:

     iva= float(iva)
     return iva
    
    except ValueError:
      
      iva= input('-> ')


importe= input('Introduce el importe sin iva -> ')
importe= respuesta(importe)

iva= input('Introduce el IVA a aplicar (ejemplo 10%) -> ')
iva=respuesta(iva)

resultado = importe + (importe*(iva/100))

print('El precio completo es' , resultado)






