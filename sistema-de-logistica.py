print('Sistema de Logística do Patrick Zanela Medeiros')

def dimensoesObjeto(): #ESSA FUNÇÃO CALCULA O VALOR ATRAVES DO TAMANHO DO VOLUME
    global valor # DEIXEI ESSA VARIAVEL COMO GLOBAL PARA ACESSA-LA FORA DA FUNÇÃO

    while True: #FIZ ESSE LAÇO COM TRY E EXCEPT PARA FAZER UM CONTROLE SOBRE OS POSSIVEIS ERROS DE TIPO DE DADOS

        try:

            alt = int(input('Digite a altura em centimetros do objeto: ')) #ESSES INPUTS SERVEM PARA PASSAR AS DIMENSÕES DO VOLUME
            comp = int(input('Digite a comprimento em centimetros do objeto: '))
            larg = int(input('Digite a largura em centimetros do objeto: '))
            dimensoestotal= alt*comp*larg #ESSA VARIAVEL FAZ O CALCULO DO VOLUME TOTAL 
            
            if dimensoestotal < 1000:  #ESSA ESTRUTURA PASSA O VALOR DE ACORDO COM O TAMANHO TOTAL DO VOLUME
                valor = 10
            elif dimensoestotal >= 1000 and dimensoestotal < 10000:
                valor = 20
            elif dimensoestotal >= 10000 and dimensoestotal < 30000:
                valor = 30
            elif dimensoestotal >= 30000 and dimensoestotal < 100000:
                valor = 20    
            else:
                print('Não aceitamos objetos com essas dimensões!')
                continue     
        

        except:
            ValueError
            print('Você digitou alguma das dimensões com valor não numérico!! ')
            continue
            
        else:
            print('O valor ficou: R${:.2f}'.format(valor)) #AO FINAL A FUNÇÃO FAZ O RETORNO DO VALOR 
            return valor
            
    
def pesoObjeto(): #ESSA FUNÇÃO CALCULA O VALOR DO MULTIPLICADOR ATRAVÉS DO PESO DO PRODUTO
     global pesomulti # DEIXEI ESSA VARIAVEL COMO GLOBAL PARA ACESSA-LA FORA DA FUNÇÃO

     while True: #FIZ ESSE LAÇO COM TRY E EXCEPT PARA FAZER UM CONTROLE SOBRE OS POSSIVEIS ERROS DE TIPO DE DADOS

        try:

            peso = float(input('Digite o peso do objeto(KG): ')) #ESSE INPUT RECEBE O PESO DO OBJETO
            if peso < 0.1: #ESSA ESTRUTURA FAZ A VERIFICAÇÃO DO MULTIPLICADOR E SE O PRODUTO ESTÁ COM O PESO ACEITAVEL
                pesomulti = peso

            elif peso >= 0.1 and peso < 1:
                pesomulti = peso * 1.5  

            elif peso >= 1 and peso < 10:
                pesomulti = peso * 2 

            elif peso >= 10 and peso < 30:
                pesomulti = peso * 3
            else:
                print('Peso superior ao permitido.')  
                continue  
          
        except:

            ValueError
            print('Você digitou algum valor não numérico!! ')
            continue
            
        else:
            print('O valor do multiplicador ficou: {}'.format(pesomulti)) #AO FINAL A FUNÇÃO RETORNA O VALOR DO MULTIPLICADOR
            return pesomulti
        
def rotaObjeto(): #ESSA FUNÇÃO CALCULA O VALOR DO MULTIPLICADOR ATRAVÉS DA ROTA DESEJADA
    global rotamulti # DEIXEI ESSA VARIAVEL COMO GLOBAL PARA ACESSA-LA FORA DA FUNÇÃO
    while True: #FIZ ESSE LAÇO COM TRY E EXCEPT PARA FAZER UM CONTROLE SOBRE OS POSSIVEIS ERROS DE TIPO DE DADOS

        try:

            print('ROTAS DISPOPONIBILIZADAS PELA EMPRESA:') # ESSE E O LAYOUT DA FUNÇÃO 
            print('RS- De Rio de Janeiro até São Paulo')
            print('SR- De São Paulo até Rio de Janeiro')
            print('BS- De Brasília até São Paulo')
            print('SB- De São Paulo até Brasília')
            print('BR- De Brasília até Rio de Janeiro ')
            print('RB- De Rio de Janeiro até Brasília')

            rota = input('Digite a rota que você deseja através de suas siglas: EXEMPLO(SR): ')

            if rota.upper() == 'RS' or rota.upper() == 'SR': #ESSA ESTRUTURA FAZ A VERIFICAÇÃO DO MULTIPLICADOR DE ACORDO COM A ROTA ESCOLHIDA
                rotamulti = 1                                #USEI O UPPER PARA EVITAR ERROS DE LETRA MAIUSCULA E MINUSCULA 
            elif rota.upper() == 'BS' or rota.upper() == 'SB':
                rotamulti = 1.2
            elif rota.upper() == 'BR' or rota.upper() == 'RB':
                rotamulti = 1.5
            else:
                print('Valor inválido, verifique se digitou corretamente...')
                continue            
        except:

            ValueError
            print('Você digitou um valor numérico!! ')
            continue
        else:
            print('O valor do multiplicador ficou: R${}'.format(rotamulti)) #AO FINAL A FUNÇÃO RETORNA O VALOR DO MULTIPLICADOR
            return rotamulti
        
#PROGRAMA PRINCIPAL

dimensoesObjeto() #EXECUTO AS FUNÇÕES 
pesoObjeto()
rotaObjeto() 
    
valortotal = valor * pesomulti * rotamulti    #CALCULO DO VALOR TOTAL 
print('O valor total a ser pago é de: R${}. (dimensâo: {}   peso: {}   rota:{})'.format(valortotal, valor, pesomulti, rotamulti)) # VALOR TOTAL AO FINAL DO PROGRAMA
    

