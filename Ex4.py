km = int(input('Quantos Km foram percorridos? '))
dias = int(input('Por quantos dias o carro foi alugado? '))

preco = 60 * dias + 0.15 * km
print('Km = {} e Dias = {}'.format(km, dias))
print('O valor que você irá pagar será de: {}'.format(preco))