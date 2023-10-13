print('------------------')
print('SERIE DE 3 EN 3')
print('------------------')

num=3

total=int(input('Dime cuantos numeros debe tener la serie -> '))
cont=1
while cont <= total:
    print(num,end='')
    if cont < total:
        print (' ',end='')
    num+= 3
    cont+= 1
print('\n')