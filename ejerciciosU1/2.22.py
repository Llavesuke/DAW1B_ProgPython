print('------------------')
print('VOCAL MAYUSCULA RAFAEL ALBERTI')
print('------------------') 

frase= input('Introduce una frase y luego una vocal -> ')
contador=int(len(frase))
print(frase[0:contador-1]+frase[contador-1:contador].upper())