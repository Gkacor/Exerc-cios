def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while ((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

def criaArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'wt+')
        a.close()
    except:
        print('Erro na criação do arquivo.')
    else:
        print('Arquivo {} foi criado com sucesso.\n'.format(nomeArquivo))

 #Função para criar o arquivo .txt, caso não exista.

def existeArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    #Função para verificar se o arquivo que eu estou pedindo existe.

def listarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
    except:
        print('Erro ao ler arquivo.')
    else:
        print(a.read())
    finally:
        a.close()



def cadastrarJogo(nomeArquivo, nomeJogo, nomeVideogame):
    try:
        a = open(nomeArquivo, 'at')

    except:
        print('Erro ao abrir o arquivo.')
    else:
        a.write('{};{}\n'.format(nomeJogo,nomeVideogame))
    finally:
        a.close()

arquivo = 'games.txt'
if existeArquivo(arquivo):
    print('Arquivo existe no computador.')
else:
    print('Arquivo não existe.')
    criaArquivo(arquivo)


while True:
    print('MENU')
    print('1 - Cadastrar novo item')
    print('2 - Mostrar Cadastros')
    print('3 - Fechar')

    op = valida_int('Escolha uma opção: ', 1, 3)
    if op == 1:
        print('Escolheu cadastrar novos itens.\n')
        nomeJogo = input('Nome do jogo: ')
        nomeVideogame = input('Nome do videogame: ')
        cadastrarJogo(arquivo, nomeJogo, nomeVideogame)


    elif op == 2:
        print('Escolheu Listar itens.\n')
        listarArquivo(arquivo)


    elif op == 3:
        print('Fechando o programa...')
        break