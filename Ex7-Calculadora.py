print('-Calculadora-')
print('+ Adição')
print('- Subtração')
print('* multiplicação')
print('/ Divisão')
print('Pressione outra tecla para sair')



while True:
    op = input('Qual operação você quer fazer?')
    if op == '+' or '-' or '*' or '/':
        x = int(input('Digite o primeiro número: '))
        y = int(input('Digite o segundo número: '))

    if (op == '+'):
        res = x + y
        print('Resultado: {} + {} = {}'.format(x, y, res))
        continue
    elif (op == '-'):
        res = x - y
        print('Resultado: {} - {} = {}'.format(x, y, res))
        continue
    elif (op == '*'):
        res = x * y
        print('Resultado: {} * {} = {}'.format(x, y, res))
        continue
    elif (op == '/'):
        res = x / y
        print('Resultado: {} / {} = {}'.format(x, y, res))
        continue
    elif (op == 's'):
        break
    else:
        print('Valor inválido!')



print('Fechando o programa...')