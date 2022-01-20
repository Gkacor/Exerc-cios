def soma(x=0, y=0, z=0):
    #Função criada para retornar a soma dos 3 valores.
    #DocString é a "help" que aparece quando pesquisado.
    #Para criar uma DocString utilizam-se as 3 aspas.
    """
    Retorna a soma de até 3 valores numéricos. Parâmetros opcionais.
    :param x: valor numério (opcional)
    :param y: valor numério (opcional)
    :param z: valor numério (opcional)
    return: soma inteira
    """
    return x+y+z

print(soma(3, 2))

help(soma)
#Pedindo para aparecer o "help"