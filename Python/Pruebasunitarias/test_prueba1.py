
def suma_de_piramides(num:int):
    contadorglobal= num # tendra el valor del numero introducido
    contadorInterno= 0
    resultado= 0
    lista= '' #lista que se ira llenando con la suma de los numeros
    returnText='' #para devolver el valor de la funcion
    num2=-num #para la parte en la que se utilizan los numeros negativos

    while contadorglobal != -1: #se le ira restando valor al contador, hasta que llegue al -1 para que se muestre el valor 0
        while contadorInterno != num+1: #la variable contadorInterno ira sumando valor hasta llegar al de la variable num
            resultado += contadorInterno #Para mostrar la suma de valores que componen el numero
            lista += str(contadorInterno) #Para mostrar los numeros que se suman
            if contadorInterno != num: #No introducir el + cuando sea el ultimo numero de la lista
                lista+= '+'
            contadorInterno+=1 #Se va sumando uno al contadorInterno hasta que llegue al valor de num
        returnText+=f"{num} = {lista} = {resultado}\n" #Se suma a la variable returnText que despues se mostrara a la hora de llamar la función
        lista= ''
        num-= 1
        contadorglobal-=1
        contadorInterno=0
        resultado=0 #Todo lo anterior es para resetear todos los valores para volver al bucle hasta que contadorglobal sea igual a -1

    if num == -1: #Cuando el valor num sea -1 se ejecuta este bloque de instrucciones que mostrara lo mismo pero con valores negativos
        while contadorglobal != num2-1: #El valor de contador global sigue siendo -1 por las instrucciones de los anteriores bucles
            while contadorglobal-1!= contadorInterno: #Ahora el que se usara como referencia como valor objetivo sera contadorglobal
                resultado+= abs(contadorInterno)
                lista+=f"({contadorInterno})"
                if contadorInterno != contadorglobal:
                    lista+= '+'
                contadorInterno-=1
            returnText+=f"{contadorInterno+1} = {lista} = -{resultado}\n" #ContadorInterno se suma uno para mostrar el valor correcto, ya que sino 
                                                                          #mostraria el valor que estamos tratando pero con una unidad de más
            contadorglobal-= 1
            contadorInterno=0
            lista=''
            resultado=0
            
    return returnText
