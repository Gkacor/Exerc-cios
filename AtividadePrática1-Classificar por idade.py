def validacao_int(pergunta, min, max):
    x = (int(input(pergunta)))
    while ((x < min) or (x > max)):
        x = (int(input(pergunta)))
    return x
#Função para validar a entrada de idade como número inteiro.

while True:
    print('MENU')
    print('1 - Procurar aluno(a)')
    print('2 - Sair')
#Como no enunciado apenas pede para dar a opção ao usuário de sair ou continuar,
#decidi utilizar esse formato de menu para diferenciar um pouco.

    escolha = validacao_int('Escolha uma opção: ', 1, 3)
    if escolha == 1:
        print('Procurar aluno(a): ')
        alunoNome = input('Nome do aluno(a): ')
        alunoIdade = int(input('Idade do aluno(a): '))
        print('O aluno(a) procurado(a) se chama {} e tem {} anos.'.format(alunoNome, alunoIdade))
#Código de entrada do menu, pedindo nome e idade, e depois mostrando
#ao usuário o que foi digitado.

        if (alunoIdade >= 1) and (alunoIdade <= 5):
             print('O aluno(a) {} está na Educação Infatil.'.format(alunoNome))
        elif (alunoIdade >= 6) and (alunoIdade <= 10):
             print('O aluno(a) {} está no Ensino Fundamental I.'.format(alunoNome))
        elif (alunoIdade >= 11) and (alunoIdade <= 14):
             print('O aluno(a) {} está no Ensino Fundamental II.'.format(alunoNome))
        elif (alunoIdade >= 15):
             print('O aluno(a) {} está no Ensino Médio.'.format(alunoNome))
#Condições para classificar em qual ensino o aluno está, de acordo com a idade.

    elif escolha == 2:
        print('Saindo...')
        break
#break final para validar e finalizar o programa, se o usuário escolher.