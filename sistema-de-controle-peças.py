print('Sistema de controle de peças do Patrick Zanela Medeiros')
contador = 0    #DEIXEI A VARIAVEL CONTADOR FORA ANTES DAS FUNÇÕES PARA EVITAR ERROS
cadastro = {'peças': []}  #CRIEI UM DICIONARIO PEÇAS, DENTRO DA VARIAVEL CADASTRO ANTES DAS FUNÇÕES 

def cadastrarPeca(contador): #FUNÇÃO DE CADASTRO COM CONTADOR DE PARAMETRO COMO O EXERCÍCIO PEDE
    peca = {} #CRIEI UM OUTRO DICIONARIO PARA ARMAZENAR MAIS DE UM CADASTRO SEM HAVER CONFLITO ENTRE ELES 
    
    peca['nome'] = input('Escreva o nome da peça: ') #ESSES INPUTS RECEBEM OS VALORES 
    peca['fabricante'] = input('Qual seu fabricante ? ')
    peca['valor'] = input('Qual o seu valor em R$ ? ')
    contador += 1 #CONTADOR QUE SE TORNARÁ O CODIGO DO PRODUTO
    peca['código'] = contador
    print('Código do produto: {}.'.format(contador))
    cadastro['peças'].append(peca)  #AO FINAL PECA E PASSADO PARA DENTRO DE CADASTRO
    
    return cadastro, contador

def consultarPeca():#FUNÇÃO DE CONSULTA 
    while True: #LAÇO INFINITO PARA SÓ SAIR QUANDO FOR PASSADO A OPÇÃO RETORNAR

        try: #TRY E EXCEPT PARA QUE NÃO ACONTEÇA ERRO DE VALOR

            print('Escolha uma das opções abaixo: ') #LAYOUT DA FUNÇÃO
            print('1-Consultar todas as peças: ')
            print('2-Consultar peças por código: ')
            print('3-Consultar peças por fabricante: ')
            print('4-Retornar: ')
            opcao = int(input('>>'))
            if opcao == 1: #ESTRUTURA QUE MOSTRA AS PEÇAS CADASTRADAS
                print('Você digitou a opção de consultar todas as peças  ')
                for peca in cadastro['peças']:
                    print('-'*15, '\nCódigo: {}\nNome: {}\nFabricante: {}\nValor: {}R$\n'.format(peca['código'], peca['nome'],peca['fabricante'],peca['valor']))       

            elif opcao == 2: #ESTRUTURA QUE MOSTRA AS PEÇAS CADASTRADAS ATRAVÉS DO SEU CODIGO
                print('Você digitou a opção de consultar as peças cadastradas através do seu código  ')
                codigo = int(input('Digite o código da peça desejada: ')) 
                for peca in cadastro['peças']:
                     if peca['código'] == codigo:
                          print('-'*15, '\nCódigo: {}\nNome: {}\nFabricante: {}\nValor: {}\n'.format(peca['código'], peca['nome'],peca['fabricante'],peca['valor']))
                     

            elif opcao == 3: #ESTRUTURA QUE MOSTRA AS PEÇAS CADASTRADAS ATRAVÉS DO SEU FABRICANTE
                print('Você digitou a opção de consultar as peças cadastradas através do seu fabricante  ')
                codigo = input('Digite o nome do fabricante: ')
                for peca in cadastro['peças']:
                    if peca['fabricante'] == codigo:
                         print('-'*15, '\nCódigo: {}\nNome: {}\nFabricante: {}\nValor: {}\n'.format(peca['código'], peca['nome'],peca['fabricante'],peca['valor']))
                    
            elif opcao == 4: #OPÇÃO DE SAIR DO PROGRAMA 
                break
            
            else:
                print('Você digitou uma opção invalida!!')

        except:
            ValueError
            print('Você digitou um valor não numérico!! ')
            continue    

def removerPeca(): #FUNÇÃO DE REMOVER PEÇA ATRAVÉS DO SEU CÓDIGO
    codigo = int(input('Digite o código do produto que você quer remover: '))
    for peca in cadastro['peças']:
        if peca['código'] == codigo:
           cadastro['peças'].remove(peca)
           return cadastro
          

#PROGRAMA PRINCIPAL

while True: #LAÇO INFINITO PARA QUE O USUARIO SÓ SAIA QUANDO ESCOLHER A OPÇÃO SAIR

    

    print('Escolha uma das opções abaixo: ')
    print('1- Cadastrar peças: ')
    print('2- Consultar peças: ')
    print('3 - Remover peças: ')
    print('4 - Sair')
    x = int(input('>>'))
    if x == 1: #ACESSA FUNÇÃO CADASTRARPECA
           cadastro, contador = cadastrarPeca(contador)

    elif x == 2: #ACESSA FUNÇÃO CONSULTARPECA
            print(consultarPeca())

    elif x == 3: #ACESSA FUNÇÃO REMOVERPECA
            excluido = removerPeca()
            if excluido:
                print('Peça excluida!!')
                
               
    elif x == 4:
            break    

    else:
        print('Você digitou uma opção invalida!')