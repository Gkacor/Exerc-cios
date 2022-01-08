preco = float(input('Digite o preço do produto: '))
p = float(input('Digite o percentual do desconto: '))

desconto = preco * (p/100)

final = preco - desconto
print('O preço do produto é {} e o desconto sobre o produto é de {}% '.format(preco, p))
print('O preço final do produto fica {} com o desconto sendo de {}'.format(final, desconto))