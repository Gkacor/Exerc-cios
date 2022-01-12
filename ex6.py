#Validando a entrada. Usuário tem que colocar um número maior do que zero.

x = int(input('Digite um valor maior do que zero: '))

while (x <= 0):
    x = int(input('Digite um valor maior do que zero: '))
    continue
    if (x > 0):
     print('Você digitou {}. Fechando o programa...'.format(x))
