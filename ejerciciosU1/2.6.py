print('\n --------------------')
print('CALCULADORA DE IVA')
print('--------------------\n')

def respuesta(iva):
 while True:
    try:

     iva= int(iva)
     return iva
    
    except ValueError:
      
      iva= input('-> ')


importe= input('Introduce el importe completo -> ')
importe= respuesta(importe)



resultado = importe - (importe*(10/100))
iva= (importe*(10/100))

print('\nEl precio sin iva es de ' , resultado)
print('Se ha pagado de iva -> ' , iva , '\n')



