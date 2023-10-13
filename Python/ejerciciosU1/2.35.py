print('------------------')
print('DOS NUMEROS + MENU')
print('------------------')

num1=int(input('Numero 1 -> '))
num2=int(input('Numero 2 -> '))

opcion=0

while opcion <1 or opcion>4:
    opcion=int(input('Introduce una opción (1 = Suma / 2 = Resta / 3 = Multiplicación / 4 = División):'))
    if opcion <1 or opcion>4:
        print('Error - No es una opción correcta (1-4)')

match opcion:
    case 1:
        print(num1,'+',num2,'=',num1+num2)
    case 2:
        print(num1,'-',num2,'=',num1-num2)
    case 3:
        print(num1,'*',num2,'=',num1*num2)
    case 4:
        print(num1,'/',num2,'=',num1/num2)