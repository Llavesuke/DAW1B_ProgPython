print('------------------')
print('IMC RAFAEL ALBERTI')
print('------------------')



while True:

    try:
        peso= float(input('Introduce tu peso (en kg) -> '))
        estatura= float(input('¿Cuanto mides? (en m) -> '))
        imc= peso / (estatura*estatura)
        print('\nTu indice de masa corporal es -> ', round(imc,2))
        break

    except ValueError:

        print('\nReintroduce los valores en un formato válido\n')