from random import choice, randint
from time import sleep
from prettytable import PrettyTable

iCopa = {
        'iSelecoesP1': ['Qatar', 'Brasil', 'Argentina', 'Belgica', 'Espanha', 'França', 'Inglaterra', 'Portugal'],
        'iSelecoesP2': ['Alemanha', 'Colombia', 'Dinamarca', 'Estados Unidos', 'Holanda', 'Mexico', 'Suica', 'Uruguai'],
        'iSelecoesP3': ['Coreia do Sul', 'Ira', 'Japao', 'Marrocos', 'Polonia', 'Senegal', 'Servia', 'Tunisia'],
        'iSelecoesP4': ['Arábia Saudita', 'Camaroes', 'Canada', 'Equador', 'Gana', 'Italia', 'Paraguai', 'Croacia']
}

class Menu: 
    def __init__(self, opcao1="TABELA DE GRUPO", opcao2="SELECAO ESCOLHIDA", opcao3="ADVERSARIOS", opcao4="JOGOS DO GRUPO", opcao5="CLASSIFICAÇAO FINAL", opcao6="CLASSIFICADOS", opcao7="SEGUIR", opcao8="SAIR"):
        self.opcoes = [opcao1, opcao2, opcao3, opcao4, opcao5, opcao6, opcao7, opcao8]
        self.iquant = len(self.opcoes)
        

iClassificacao = {
    'iGrupoP1': [], 'iGrupoP2': [], 'iGrupoP3': [], 'iGrupoP4': [],
    'iGrupoP5': [], 'iGrupoP6': [], 'iGrupoP7': [], 'iGrupoP8': []
}

iJogos_FaseGrupo = {
    'iGrupoP1': [], 'iGrupoP2': [], 'iGrupoP3': [], 'iGrupoP4': [],
    'iGrupoP5': [], 'iGrupoP6': [], 'iGrupoP7': [], 'iGrupoP8': []
}

Pontuacao_Grupo = {
    'iGrupoP1': [], 'iGrupoP2': [], 'iGrupoP3': [], 'iGrupoP4': [],
    'iGrupoP5': [], 'iGrupoP6': [], 'iGrupoP7': [], 'iGrupoP8': []
}

iClassificados =  {
    'iGrupoP1': [], 'iGrupoP2': [], 'iGrupoP3': [], 'iGrupoP4': [],
    'iGrupoP5': [], 'iGrupoP6': [], 'iGrupoP7': [], 'iGrupoP8': []
}

iOitavas =  []
iJogos_Oitavas = {
    'iJogos':[]
}

menu = Menu()
tabela = {}
Placar1 = 0
Placar2 = 0
Prorrogacao_Placar1 = 0
Prorrogacao_Placar2 = 0

# Fase_Final = {
#     'iQuartas': [],
#     'iSemifinais': [],
#     'iFinal': []
# }


def iSelecao():
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
            iExibicao(f'Fase de Grupo {c}', k)
        sleep(1)
        Imprime(f'Fase de Grupo {c}')


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
                Imprime("Proximos Adversários")
                iGrupoCopa()
                for c in range(menu.iquant):
                    iExibicao("MENU", f"{c+1}: {menu.opcoes[c]}")
               
                if iOpcaoMenu() != 7:
                    return True
                else:
                    Fase_Final()
                    return True


def iGrupoCopa():
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
                        Placar1 = randint(1, 5)
                        Placar2 = randint(1, 5)
                        Rodada = (f'{Sel_Principal} {Placar1} x {Placar2} {k}')
                        iExibicao(f'Jogos do Grupo {c}',Rodada )
                        iJogos_FaseGrupo[f'iGrupoP{c}'].append([Sel_Principal, k])
                        iPontuacao(Sel_Principal, k, Placar1, Placar2, c)
                        iCount += 1
                    if iCount == 2:
                        break
                    if iPartida == 6:
                        iOrganizaPontuacao(c)
                        iPartida = 0
            sleep(2)
            Imprime(f'Jogos do Grupo {c}')
            break
    iApresenta()
    

def iCompara(Nome1, Nome2, Count):
    iRet = 0
    for j in iJogos_FaseGrupo[f'iGrupoP{Count}']:
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
    selecoes_ordenadas = sorted(selecoes, key=lambda item: (item[1], item[3], item[13], item[9], item[11], item[7] ), reverse=True)
    Pontuacao_Grupo[grupo_key] = []

    for j in range(0, 4):
        iPosicao = 0
        for k in selecoes_ordenadas:
            Pontuacao_Grupo[grupo_key].append(k)
            iPosicao += 1
            if iPosicao == 1:
                iClassificados[f'iGrupoP{c}'].append(k[0])
            elif iPosicao == 2:
                iClassificados[f'iGrupoP{c}'].append(k[0])
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
            iExibicao(f'Classificacao {k}', statistica)
            iPosicao += 1
            if iPosicao == 4:
                break
        Imprime(f'Classificacao {k}', 1)
        


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


def iClass_Final(iGrupo):
    Apresentacao = (f'Grupo {iGrupo}')
    Cont = len(iClassificados)
    if iGrupo > 0 and iGrupo <= Cont:
        for k in range (0, 2):
            iClass = iClassificados[f'iGrupoP{iGrupo}'][k]
            iExibicao(f'Grupo {iGrupo}', iClass)
        Imprime(f'Grupo {iGrupo}')
        tabela[Apresentacao].clear()
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
                                if Imprime(f'Fase de Grupo {iGrupo}'):
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
                        while True:
                            iEscolha_Grupo  = input("Qual Grupo voce deseja ver os Classificados? : ")
                            try:
                                iClass_Grupo = int(iEscolha_Grupo)
                                if iClass_Final(iClass_Grupo):
                                    break
                            except:
                                continue
                    case 7:
                        return 7
                    case 8:
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
    iMata = {
        'iPrimeiraParte': [],
        'iSegundaParte': []
    }
    for k in range(1, 9):
        for c in range(0, 2):
            Selecao = iClassificados[f'iGrupoP{k}'][c]
            if k % 2 == 0 and c == 0:
                iMata['iPrimeiraParte'].append(Selecao)
            elif k % 2 == 1 and c == 1:
                iMata['iPrimeiraParte'].append(Selecao)
            else:
                iMata['iSegundaParte'].append(Selecao)
    
    for i in range(0, 7, 2):
        iOitavas.append([iMata['iSegundaParte'][i], iMata['iSegundaParte'][i+1]])
        iOitavas.append([iMata['iPrimeiraParte'][i], iMata['iPrimeiraParte'][i+1]])

    while True:
        for k in iOitavas:
            P_Selecao = k[0]
            S_Selecao = k[1]
            Placar1 = randint(1, 5)
            Placar2 = randint(1, 5)
            Rodada = (f'{P_Selecao} {Placar1} x {Placar2} {S_Selecao}')
            iExibicao(f'Jogos Oitavas', Rodada )
            iJogos_Oitavas['iJogos'].append(Rodada)
            if Placar1 == Placar2:
                Prorrogacao = ("Prorrogacao:")
                iExibicao(f'Jogos Oitavas', Prorrogacao)
                Prorrogacao_Placar1 = randint(1, 2)
                Prorrogacao_Placar2 = randint(1, 2)
                Rodada = (f'{P_Selecao} {Prorrogacao_Placar1} x {Prorrogacao_Placar2} {S_Selecao}')
                iExibicao(f'Jogos Oitavas', Rodada )
                iJogos_Oitavas['iJogos'].append(Rodada)
                if Prorrogacao_Placar1 == Prorrogacao_Placar2:
                    iPenalti(P_Selecao, S_Selecao,"Jogos Oitavas")
        sleep(2)
        Imprime("Jogos Oitavas")
        break
    

def iPenalti(Selecao1, Selecao2, Fase):
    Penalti_Prorrogacao_Placar1 = 0
    Penalti_Prorrogacao_Placar2 = 0
    Contador_Penalti = 5
    iChute_Selecao1 = 0
    iChute_Selecao2 = 0
    
    for c in range(0,50):
        if not iDiferenca(Penalti_Prorrogacao_Placar1, Penalti_Prorrogacao_Placar2, Contador_Penalti):
            if Contador_Penalti == 0 and Penalti_Prorrogacao_Placar1 == Penalti_Prorrogacao_Placar2:
                Contador_Penalti += 1
            Contador_Penalti -= 1
            if Contador_Penalti >= 0:
                iChute_Selecao1 = ""
                iChute_Selecao1 = choice([True, False])
                if iChute_Selecao1 == True:
                    iExibicao(Fase, f'{Selecao1}: Acertou')
                    Penalti_Prorrogacao_Placar1 += 1
                else:
                    iExibicao(Fase, f'{Selecao1}: Errou')

            if Contador_Penalti >= 0:
                iChute_Selecao2 = ""
                iChute_Selecao2 = choice([True, False])
                if iChute_Selecao2 == True:
                    iExibicao(Fase, f'{Selecao2}: Acertou')
                    Penalti_Prorrogacao_Placar2 += 1
                else:
                    iExibicao(Fase, f'{Selecao2}: Errou')
        else:
            break
        
    iExibicao(f'Jogos Oitavas', "Final:")
    Penalti_Rodada = (f'{Selecao1} {Penalti_Prorrogacao_Placar1} x {Penalti_Prorrogacao_Placar2} {Selecao2}')
    iExibicao(f'Jogos Oitavas', Penalti_Rodada)

    
def iDiferenca(Penalti_Prorrogacao_Placar1, Penalti_Prorrogacao_Placar2, Contador_Penalti):
    Total = 0
    if Penalti_Prorrogacao_Placar1 > Penalti_Prorrogacao_Placar2 :
        Total = Penalti_Prorrogacao_Placar1 - Penalti_Prorrogacao_Placar2
    if Penalti_Prorrogacao_Placar2 > Penalti_Prorrogacao_Placar1:
        Total = Penalti_Prorrogacao_Placar2 - Penalti_Prorrogacao_Placar1
        
    if Total > Contador_Penalti:
        return True
    else:
        return False

    