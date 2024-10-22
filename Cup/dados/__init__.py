from random import choice, randint
from time import sleep
from prettytable import PrettyTable

tabela = {}
class Menu: 
    def __init__(self, opcao1="TABELA DE GRUPO", opcao2="SELECAO ESCOLHIDA", opcao3="ADVERSARIOS", opcao4="JOGOS DO GRUPO", opcao5="CLASSIFICAÇAO FINAL", opcao6="SEGUIR", opcao7="SAIR"):
        self.opcoes = [opcao1, opcao2, opcao3, opcao4, opcao5, opcao6, opcao7]
        self.iquant = len(self.opcoes)
        
        
menu = Menu()

iClassificacao = {
    'iGrupoP1': [], 'iGrupoP2': [], 'iGrupoP3': [], 'iGrupoP4': [],
    'iGrupoP5': [], 'iGrupoP6': [], 'iGrupoP7': [], 'iGrupoP8': []
}

iJogos = {
    'iGrupoP1': [], 'iGrupoP2': [], 'iGrupoP3': [], 'iGrupoP4': [],
    'iGrupoP5': [], 'iGrupoP6': [], 'iGrupoP7': [], 'iGrupoP8': []
}

Pontuacao_Grupo = {
    'iGrupoP1': [], 'iGrupoP2': [], 'iGrupoP3': [], 'iGrupoP4': [],
    'iGrupoP5': [], 'iGrupoP6': [], 'iGrupoP7': [], 'iGrupoP8': []
}

iOitavas =  {
    'iGrupoP1': [], 'iGrupoP2': [], 'iGrupoP3': [], 'iGrupoP4': [],
    'iGrupoP5': [], 'iGrupoP6': [], 'iGrupoP7': [], 'iGrupoP8': []
}
# Fase_Final = {
 
#     'iQuartas': [],
#     'iSemifinais': [],
#     'iFinal': []
# }
#

def iSelecao():
    iCopa = {
        'iSelecoesP1': ['Qatar', 'Brasil', 'Argentina', 'Belgica', 'Espanha', 'França', 'Inglaterra', 'Portugal'],
        'iSelecoesP2': ['Alemanha', 'Colombia', 'Dinamarca', 'Estados Unidos', 'Holanda', 'Mexico', 'Suica', 'Uruguai'],
        'iSelecoesP3': ['Coreia do Sul', 'Ira', 'Japao', 'Marrocos', 'Polonia', 'Senegal', 'Servia', 'Tunisia'],
        'iSelecoesP4': ['Arábia Saudita', 'Camaroes', 'Canada', 'Equador', 'Gana', 'Italia', 'Paraguai', 'Croacia']}

    for k in range(1, 5):
        for c in range(1, 9):
            iEscolhido = choice(iCopa[f'iSelecoesP{k}'])
            iCopa[f'iSelecoesP{k}'].remove(iEscolhido)
            iClassificacao[f'iGrupoP{c}'].append(iEscolhido)

    for c in range(1, 9):
        iTabelas()
        break


def iTabelas():
    for c in range(1, 9):
        for k in iClassificacao[f'iGrupoP{c}']:
            iExibicao(f'Grupo{c}', k)
        Imprime(f'Grupo{c}')
        #sleep(1)


def iGrupo_Sel(iSelecaoEscolhida):
    for c in range (1,9):
        for selecao in iClassificacao[f'iGrupoP{c}']:
            if iSelecaoEscolhida in selecao:
                grupo = c
                for k in iClassificacao[f'iGrupoP{grupo}']:
                    if k in iSelecaoEscolhida:
                        iExibicao("Selecao Escolhida", iSelecaoEscolhida)
                    else:                        
                        iExibicao("Proximos Adversários", k)
                Imprime("Selecao Escolhida")
                # sleep(1)                
                Imprime("Proximos Adversários")
                # sleep(1)
                iGrupoCopa()
                for c in range(menu.iquant):
                    iExibicao("MENU", f"{c+1}: {menu.opcoes[c]}")
                    
                if iOpcaoMenu() != 6:
                    return True
                else:
                    Fase_Final()

def iGrupoCopa():
    Placar1 = 0
    Placar2 = 0
    iCount = 0
    iPartida = 0
    Principal = list()
    for c in range(1, 9):
        Principal = iClassificacao[f'iGrupoP{c}']    
        while True:
            for v in range(0, 4):
                iCount = 0
                Sel_Principal = Principal[v]
                for k in iClassificacao[f'iGrupoP{c}']:
                    if iCompara(Sel_Principal, k, c):
                        continue
                    elif Sel_Principal in k:
                        continue
                    else:
                        iPartida += 1
                        Placar1 = randint(1, 4)
                        Placar2 = randint(1, 4)
                        Rodada = (f'{Sel_Principal} {Placar1} x {Placar2} {k}')
                        iExibicao(f'Jogos do Grupo {c}',Rodada )
                        #sleep(1)
                        iJogos[f'iGrupoP{c}'].append([Sel_Principal, k])
                        iPontuacao(Sel_Principal, k, Placar1, Placar2, c)
                        iCount += 1
                        #sleep(0.1)
                    if iCount == 2:
                        break
                    if iPartida == 6:
                        iOrganizaPontuacao(c)
                        iPartida = 0
            Imprime(f'Jogos do Grupo {c}')
            break
    #iExibicao("Classificação final", "Fase De Grupos")
    #Imprime("Classificação final")
    iApresenta()
    

def iCompara(Nome1, Nome2, Count):
    iRet = 0
    for j in iJogos[f'iGrupoP{Count}']:
        if sorted([Nome1, Nome2]) == sorted(j):
            iRet = 1
            break
        elif sorted([Nome2, Nome1]) == sorted(j):
            iRet = 1
            break

    return iRet


def iPontuacao(Nome1, Nome2, Placar1, Placar2, Count):
    iPontosVitoria = 3
    iVitoriaConquistada = 1
    iEmpate = 1
    iEmpateConquistado = 1
    iDerrota = 1
    Paises = []

    if len(Pontuacao_Grupo[f'iGrupoP{Count}']) == 0:
        Paises = (iClassificacao[f'iGrupoP{Count}'])
        for c in Paises:
            Pontuacao_Grupo[f'iGrupoP{Count}'].append([ c, 0, 'iVitoria', 0 , 'Empate' ,0  , 'Derrota', 0 , 'iGols_Feitos', 0, 'iGols_Sofridos' , 0, 'Saldo', 0])
            if c == 4:
                break
        
    for i, item in enumerate(Pontuacao_Grupo[f'iGrupoP{Count}']):
        if item[0] in Nome1:
            if Placar1 > Placar2:
                Pontuacao_Grupo[f'iGrupoP{Count}'][i][1] += iPontosVitoria
                Pontuacao_Grupo[f'iGrupoP{Count}'][i][3] += iVitoriaConquistada
            elif Placar1 == Placar2:
                Pontuacao_Grupo[f'iGrupoP{Count}'][i][1] += iEmpate
                Pontuacao_Grupo[f'iGrupoP{Count}'][i][5] += iEmpateConquistado
            else:
                Pontuacao_Grupo[f'iGrupoP{Count}'][i][7] += iDerrota

            Pontuacao_Grupo[f'iGrupoP{Count}'][i][9] += Placar1
            Pontuacao_Grupo[f'iGrupoP{Count}'][i][11] += Placar2
            Pontuacao_Grupo[f'iGrupoP{Count}'][i][13] += (Placar1 - Placar2)
        elif item[0] in Nome2:
            if Placar2 > Placar1:
                Pontuacao_Grupo[f'iGrupoP{Count}'][i][1] += iPontosVitoria
                Pontuacao_Grupo[f'iGrupoP{Count}'][i][3] += iVitoriaConquistada
            elif Placar1 == Placar2:
                Pontuacao_Grupo[f'iGrupoP{Count}'][i][1] += iEmpate
                Pontuacao_Grupo[f'iGrupoP{Count}'][i][5] += iEmpateConquistado
            else:
                Pontuacao_Grupo[f'iGrupoP{Count}'][i][7] += iDerrota

            Pontuacao_Grupo[f'iGrupoP{Count}'][i][9] += Placar2
            Pontuacao_Grupo[f'iGrupoP{Count}'][i][11] += Placar1
            Pontuacao_Grupo[f'iGrupoP{Count}'][i][13] += (Placar2 - Placar1)


def iOrganizaPontuacao(c):
    grupo_key = f'iGrupoP{c}'
    selecoes = Pontuacao_Grupo.get(grupo_key, [])
    selecoes_ordenadas = sorted(selecoes, key=lambda item: (item[1], item[3], item[13], item[9], item[11] ), reverse=True)
    Pontuacao_Grupo[grupo_key] = []

    for j in range(0, 4):
        iPosicao = 0
        for k in selecoes_ordenadas:
            Pontuacao_Grupo[grupo_key].append(k)
            iPosicao += 1
            if iPosicao == 1:
                iOitavas[f'iGrupoP{c}'].append(k[0])
            elif iPosicao == 2:
                iOitavas[f'iGrupoP{c}'].append(k[0])
        break


def extrair_valores(dados):
        return [dados[0], dados[1], dados[3], dados[5], dados[7], dados[9], dados[11], dados[13]]


def iApresenta():
    selecao = []
    iPosicao = 0
    selecao = []
    for k in range(1,9):
        print(f'                     GRUPO {k}      ')
        for selecao in Pontuacao_Grupo[f'iGrupoP{k}']:
            statistica = extrair_valores(selecao)
            #iExibicao(f'Classificacao {k}', [f"{iPosicao+1}: {statistica[0]}"] + statistica[1:])
            iExibicao(f'Classificacao {k}', statistica)
            iPosicao += 1
            if iPosicao == 4:
                break
        Imprime(f'Classificacao {k}', 1)
        
        
    # tabela = PrettyTable()
    # for k in range(1,9):
    #     tabela.clear()
    #     tabela.field_names = ["Classificação", "P", "V", "E", "D", "GP", "GC", "SG"]
    #     iPosicao = 0
    #     selecao = []
    #     print(f'                     GRUPO {k}      ')
    #     for selecao in Pontuacao_Grupo[f'iGrupoP{k}']:
    #         statistica = extrair_valores(selecao)
    #         tabela.add_row([f"{iPosicao+1}: {statistica[0]}"] + statistica[1:])
    #         iPosicao += 1
    #         if iPosicao == 4:
    #             break
    #     print(tabela)


def iExibicao(Apresentacao, cliente):
    if tabela.get(Apresentacao) is None:
            tabela[Apresentacao] = [cliente]
    else:
        tabela[Apresentacao].append(cliente)
    

def Imprime(Apresentacao, opcional=0):
    Mensagem = PrettyTable()
    iPosicao = 0
    for c in tabela[Apresentacao]:
        if opcional == 0:
            Mensagem.field_names = [Apresentacao]
            Mensagem.add_row([c])
        else:
            Mensagem.field_names = ["Classificação", "P", "V", "E", "D", "GP", "GC", "SG"]
            Mensagem.add_row([f"{iPosicao+1}: {c[0]}"] + c[1:])
            iPosicao += 1
            
    print(Mensagem)
    return True


def iOpcaoMenu():

    iEscolha_Menu = 0
    Imprime("MENU")
    while True:
        iEscolha_Menu = input('Escolha a opcao desejada: ')
        try: 
            iEscolha = int(iEscolha_Menu)
            if iEscolha > 0 and iEscolha <= 7:
                match (iEscolha):
                    case 1:
                        while True:
                            iGrupo = input("Qual tabela de Grupos: ")
                            try:
                                if Imprime(f'Grupo{iGrupo}'):
                                    break
                            except:
                                continue
                    case 2:
                        Imprime("Selecao Escolhida")
                    case 3:
                        Imprime("Proximos Adversários")
                    case 4:
                        while True:
                            iJogos = input("Qual Grupo voce deseja ver os jogos? : ")
                            try:
                                if Imprime(f'Jogos do Grupo {iJogos}'):
                                    break
                            except:
                                continue
                    case 5:
                        while True:
                            iNumber = input("Qual Grupo voce deseja ver a Classificação? : ")
                            try:
                                if Imprime(f'Classificacao {iNumber}', 1):
                                    break
                            except:
                                continue
                    case 6:
                        #VERIFICAR
                        return 6
                    case 7:
                        return
                
                while True:
                    iRetorna = (input("Deseja voltar para o Menu: [SIM/NAO]: ")).upper()
                    try:
                        if iRetorna in 'SIM':
                            Imprime("MENU")
                            break
                        if iRetorna in 'NAO':
                            return
                    except:
                        continue
        except:
            continue


def Fase_Final():
    for k in range(1, 9):
            iEscolhido = choice(Pontuacao_Grupo[f'iGrupoP{k}'])
            for c in range(1, 3):
                if c == 1:
                    iOitavas['Primeiros'].append(iEscolhido[0])
                else:
                    iOitavas['Segundos'].append(iEscolhido[0])

    for c in range(1, 9):
        iTabelas()
        break
    iClassificacao[f'iGrupoP{c}'].append(iEscolhido)
                
        
                
        
        