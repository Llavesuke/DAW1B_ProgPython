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


importe= input('Introduce el importe completo -> ')
importe= respuesta(importe)



resultado = importe - (importe*(10/100))
iva= (importe*(10/100))

print('\nEl precio sin iva es de ' , '{:.2f}'.format(resultado))
print('Se ha pagado de iva -> ' , '{:.2f}'.format(iva) , '\n')