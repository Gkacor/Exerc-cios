def borda(s1):
    tam = len(s1)

    if tam:
        print('+', '-', *tam, '+')
        print('|', s1, '|')
        print('+', '-', *tam, '+')

borda('Exercício 10')
borda('Python')


