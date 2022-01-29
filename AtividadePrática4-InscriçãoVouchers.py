from random import seed
from random import randint

def validacao_int(pergunta, min, max):
    x = (int(input(pergunta)))

    while ((x < min) or (x > max)):
        x = (int(input(pergunta)))
    return x
#Função para validar a entrada do usuário.

inscricaodic = {}
inscricaolista = []
seed(100)
numero = randint(100, 400)

while True:
    print('*******' + 'Menu' + '********')
    print('1 - Fazer inscrição')
    print('2 - Ver inscrições')
    print('3 - Sair')
    escolha = validacao_int('Escolha uma das opções: ', 1, 3)
#Menu de escolhas.
    if escolha == 1:

        print('Escolheu a opção 1.')
        for i in range(1):
            nome = input('Qual seu nome?')
            email = input('Qual o seu email?')
            telefone = int(input('Qual o seu telefone?'))
            curso = input('Qual curso você faz?')
            voucher = numero

            inscricaodic['inscrito'] = inscricaolista
            inscricaolista.append(nome)
            inscricaodic['inscrito'] = inscricaolista
            inscricaolista.append(email)
            inscricaodic['inscrito'] = inscricaolista
            inscricaolista.append(telefone)
            inscricaodic['inscrito'] = inscricaolista
            inscricaolista.append(curso)
            inscricaodic['inscrito'] = inscricaolista
            inscricaolista.append(voucher)
#Input para o usuário digitar os dados pedidos.
#Adicionando os dados digitados no dicionário.

    elif escolha == 2:
        print('######' + 'Inscrições' + '######')

        for i in inscricaodic.items():
            print('******incricoes***** \n{}'.format(i))
        else:
         if inscricaodic.values() is None:
            print('Não existem inscrições ainda.')
#Se o usuário escolher a segunda opção, mostra todas as inscrições.
#Se não existirem inscrições ainda, mostra o print.

    elif escolha == 3:
        print('Fechando o programa...')
        break
#Finaliza o programa se a opcao 3 for escolhida.
    if escolha != 1 or 2 or 3:
        print('Escolha uma opção existente!')
#Se o usuário digitar outra coisa, mostra a mensagem de "erro".