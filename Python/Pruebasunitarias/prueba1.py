from funcion import suma_de_piramides


num= int(input('->'))
num=abs(num)
while num<-100 or num> 100:
    print('Numero incorrecto')
    num= int(input('->'))
    num=abs(num)

print(suma_de_piramides(num))