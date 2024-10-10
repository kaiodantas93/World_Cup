from random import choice, randint
from time import sleep
from prettytable import PrettyTable

iClassificao = {
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
            iClassificao[f'iGrupoP{c}'].append(iEscolhido)

    for c in range(1, 9):
        iTabelas()
        break


def iTabelas():
    tabela = PrettyTable()
    for c in range(1, 9):
        tabela.clear()
        tabela.field_names = [f"Grupo{c}"]
        for k in iClassificao[f'iGrupoP{c}']:
            tabela.add_row([k])
        print(tabela)
            # sleep(0.5)


def iGrupo_Sel(iSelecao):
    tabela = PrettyTable()
    
    for c in range (1,9):
        for selecao in iClassificao[f'iGrupoP{c}']:
            if iSelecao in selecao:
                grupo = c
                for k in iClassificao[f'iGrupoP{grupo}']:
                    if k in iSelecao:
                        tabela.field_names = ["Selecao"]
                        tabela.add_row([iSelecao])
                        print(tabela)
                        tabela.clear()
                    else:
                        tabela.field_names = ["Adversários"]
                        tabela.add_row([k])
                print(tabela)
                iGrupoCopa()
                return True


def iGrupoCopa():
    Placar1 = 0
    Placar2 = 0
    iCount = 0
    iPartida = 0
    Principal = list()

    for c in range(1, 9):
        print(f'Jogos do Grupo {c}')
        Principal = iClassificao[f'iGrupoP{c}']    
        while True:
            for v in range(0, 4):
                iCount = 0
                Sel_Principal = Principal[v]
                for k in iClassificao[f'iGrupoP{c}']:
                    if iCompara(Sel_Principal, k, c):
                        continue
                    elif Sel_Principal in k:
                        continue
                    else:
                        iPartida += 1
                        Placar1 = randint(1, 4)
                        Placar2 = randint(1, 4)
                        print(f'{Sel_Principal} {Placar1} x {Placar2} {k}')
                        iJogos[f'iGrupoP{c}'].append([Sel_Principal, k])
                        iPontuacao(Sel_Principal, k, Placar1, Placar2, c)
                        iCount += 1
                        #sleep(0.1)
                    if iCount == 2:
                        break
                    if iPartida == 6:
                        iOrganiza(c)
                        iPartida = 0
            
            break
    print('Classificação final')
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
    iVitoria = 3
    iEmpate = 1
    Paises = []

    if len(Pontuacao_Grupo[f'iGrupoP{Count}']) == 0:
        Paises = (iClassificao[f'iGrupoP{Count}'])
        for c in Paises:
            Pontuacao_Grupo[f'iGrupoP{Count}'].append([ c, 0, 'iVitoria', 0 , 'Empate' ,0  , 'Derrota', 0 , 'iGols_Feitos', 0, 'iGols_Sofridos' , 0, 'Saldo', 0])
            if c == 4:
                break
        
    for i, item in enumerate(Pontuacao_Grupo[f'iGrupoP{Count}']):
        if item[0] in Nome1:
            if Placar1 > Placar2:
                Pontuacao_Grupo[f'iGrupoP{Count}'][i][1] += iVitoria
                Pontuacao_Grupo[f'iGrupoP{Count}'][i][3] += 1
            elif Placar1 == Placar2:
                Pontuacao_Grupo[f'iGrupoP{Count}'][i][1] += iEmpate
                Pontuacao_Grupo[f'iGrupoP{Count}'][i][5] += 1
            else:
                Pontuacao_Grupo[f'iGrupoP{Count}'][i][7] += 1

            Pontuacao_Grupo[f'iGrupoP{Count}'][i][9] += Placar1
            Pontuacao_Grupo[f'iGrupoP{Count}'][i][11] += Placar2
            Pontuacao_Grupo[f'iGrupoP{Count}'][i][13] += (Placar1 - Placar2)
        elif item[0] in Nome2:
            if Placar2 > Placar1:
                Pontuacao_Grupo[f'iGrupoP{Count}'][i][1] += iVitoria
                Pontuacao_Grupo[f'iGrupoP{Count}'][i][3] += 1
            elif Placar1 == Placar2:
                Pontuacao_Grupo[f'iGrupoP{Count}'][i][1] += iEmpate
                Pontuacao_Grupo[f'iGrupoP{Count}'][i][5] += 1
            else:
                Pontuacao_Grupo[f'iGrupoP{Count}'][i][7] += 1

            Pontuacao_Grupo[f'iGrupoP{Count}'][i][9] += Placar2
            Pontuacao_Grupo[f'iGrupoP{Count}'][i][11] += Placar1
            Pontuacao_Grupo[f'iGrupoP{Count}'][i][13] += (Placar2 - Placar1)


def iOrganiza(c):
    grupo_key = f'iGrupoP{c}'
    selecoes = Pontuacao_Grupo.get(grupo_key, [])
    selecoes_ordenadas = sorted(selecoes, key=lambda item: (item[1], item[3], item[13], item[9] ), reverse=True)
    Pontuacao_Grupo[grupo_key] = []

    for j in range(0, 4):
        for k in selecoes_ordenadas:
            Pontuacao_Grupo[grupo_key].append(k)
        break

def extrair_valores(dados):
        return [dados[0], dados[1], dados[3], dados[5], dados[7], dados[9], dados[11], dados[13]]


def iApresenta():
    tabela = PrettyTable()
    for k in range(1,9):
        tabela.clear()
        tabela.field_names = ["Classificação", "P", "V", "E", "D", "GP", "GC", "SG"]
        iPosicao = 0
        selecao = []
        print(f'POTE {k} |')
        for selecao in Pontuacao_Grupo[f'iGrupoP{k}']:
            statistica = extrair_valores(selecao)
            tabela.add_row([f"{iPosicao+1}: {statistica[0]}"] + statistica[1:])
            iPosicao += 1
            if iPosicao == 4:
                break
        print(tabela)

        


# def iGrupo_Sel(iSelecao):
#     tabela = PrettyTable()
#     for k, v in iClassificao.items():
#         tabela.field_names = ["Selecao", "Adversários"]
#         if iSelecao in v:
#             print(f'A Seleção do {iSelecao} esta no Grupo {k[7]}', end='')
#             print(f' e enfrentará as selecoes: ', end='')
#             for j in v:
#                 if iSelecao in j:
#                     continue
#                 else:
#                     print(f'{j}, ', end='')
#             print()
#             iGrupoCopa()
#             return True