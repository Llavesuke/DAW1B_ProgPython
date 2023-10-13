print('------------------')
print('ORDENADOR DE NUMEROS')
print('------------------')


n1= int(input('Numero 1 -> '))
n2= int(input('Numero 2 -> '))
n3= int(input('Numero 3 -> '))

if n1 < n2 and n1 < n3:
    if n2<n3:
        print(n1,'<',n2,'<',n3)
    else:
        print(n1,'<',n3,'<',n2)
else:
    if n2 < n1 and n2 < n3:
        if n1<n3:
            print(n2,'<',n1,'<',n3)
        else:
            print(n2,'<',n3,'<',n1)
    else:
        if n3<n1 and n3<n2:
            if n1<n2:
                print(n3,'<',n1,'<',n2)
            else:
                print(n3,'<',n2,'<',n1)