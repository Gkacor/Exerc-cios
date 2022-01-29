def jogo(nivel, tabuleiro, opcoes, testar):
    respostajogador = []
#Lista para armazenar as vitórias. Embaixo o print de apresentação.
#Função para utilizar no programa principal.

    print('\nFase {}. Você deve colocar nos espaços:'.format(nivel + 1))

    for item in opcoes:
        print(item)
    for linha in tabuleiro:
        print(linha)
    for item in opcoes:
        respostajogador.append(input('\nOnde deve ser colocado o {}?\n'.format(item)))
#Começo do jogo. Mostra na tela o tabuleiro para o jogador.

    if respostajogador == testar and tabuleiro < 3:
        return True
#Se der true, muda de nível.

    elif respostajogador == testar and tabuleiro == 3:
        print('-----------------------------------')
        print('***** ~VOCÊ VENCEU! PARABÉNS!~ *****')
        print('-----------------------------------')
        return True
#Mensagem que aparece se o jogador vencer.
    else:
        print('Game Over. Resposta errada.')  #Mensagem que aparece se o jogador errar.
        return False

#Principal
nivel = 0

tabuleiro = [['', '', '', 'G'], ['R', '', '', '']], [['', '', '', ''], ['', 'C', '', '_']], \
        [['-', '', '', ''], ['-', 'G', '-', '']], [['-', '-', '-', ''], ['', 'R', '', '']]
opcoes = [['RATO', 'GATO'], ['CÃO', 'CÃO', 'OSSO'], ['GATO', 'RATO', 'OSSO'], ['QUEIJO', 'QUEIJO', 'OSSO']]
testar = [['6', '3'], ['7', '8', '1'], ['7', '1', '5'], ['1', '3', '2']]
#Tabuleiro para o jogador e layout.
print('******************************')
print('       *HOTEL ANIMAL*')
print('******************************\n')
print('Você deve colocar os animais dentro dos quartos.'
      '\nOs números dos quartos são:\n')
print([1, 2, 3, 4])
print([5, 6, 7, 8])
print('\n=- =- =- *REGRAS* -= -= -=')
print('ATENÇÃO:')
print(
    '-> O rato não deve ficar ao lado do gato. <- '
    '\n-> O queijo não deve ficar ao lado do rato. <-'
    '\n-> O cão não deve ficar ao lado do osso. <-'
    '\n-> O gato não deve ficar ao lado do cão. <-')
print()
print(
    '[G] - GATO          [C] - CÃO                   [R] - RATO          [O] - OSSO'
    '\n[Q] - QUEIJO        [*] - OCUPADO          [-] - DISPONÍVEL')
#Layout de regras e opções para o jogador.

while nivel <= 3:
    respostajogador1 = jogo(nivel, tabuleiro[nivel], opcoes[nivel], testar[nivel])
    if respostajogador1:
        nivel += 1
    #Muda de nível.
    else:
        break
    #Chamando a função e rodando o jogo.
    #Se o jogador errar, o break encerra o jogo.
