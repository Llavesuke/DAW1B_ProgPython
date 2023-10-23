print('------------------')
print('SERIE ENTRE DOS NUMEROS')
print('------------------')

num1=int(input('Introduce un numero -> '))
num2=int(input('Introduce otro numero -> '))

if num1<=num2:
    numini= num1
    numfin= num2
else:
    numini= num2
    numfin= num1
    
print('\n')
for i in range(numini,numfin+1):
    print(i, end='')
    if i != numfin:
        print('-', end='')
print('\n')