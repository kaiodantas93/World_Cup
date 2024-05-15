from random import choice, randint
from time import sleep
# iJogos = list()

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
    for c in range(1, 9):
        print(f'POTE {c} |')
        for k in iClassificao[f'iGrupoP{c}']:
            print(k)
            # sleep(0.5)


def iGrupo_Sel(iSelecao):
    for k, v in iClassificao.items():
        if iSelecao in v:
            print(f'A Seleção do {iSelecao} esta no Grupo {k[7]}', end='')
            print(f' e enfrentará as selecoes: ', end='')
            for j in v:
                if iSelecao in j:
                    continue
                else:
                    print(f'{j}, ', end='')
            print()
            iGrupoCopa()
            return True


def iGrupoCopa():
    Placar1 = 0
    Placar2 = 0
    iCount = 0
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
                        Placar1 = randint(1, 4)
                        Placar2 = randint(1, 4)
                        print(f'{Sel_Principal} {Placar1} x {Placar2} {k}')
                        iJogos[f'iGrupoP{c}'].append([Sel_Principal, k])
                        iPontuacao(Sel_Principal, k, Placar1, Placar2, c)
                        iCount += 1
                        sleep(0.1)
                    if iCount == 2:
                        break
            break


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
    iDerrota = 0
    Indice = 0
    Paises = []

    if len(Pontuacao_Grupo[f'iGrupoP{Count}']) == 0:
        Paises = (iClassificao[f'iGrupoP{Count}'])
        for c in Paises:
            Pontuacao_Grupo[f'iGrupoP{Count}'].append([c, 0])
            if c == 4:
                break
        

    for i, item in enumerate(Pontuacao_Grupo[f'iGrupoP{Count}']):
        if Placar1 > Placar2:
            if item[0] in Nome1:
                Pontuacao_Grupo[f'iGrupoP{Count}'][i][1] += iVitoria
                break
        elif Placar2 > Placar1:
            if item[0] in Nome2:
                Pontuacao_Grupo[f'iGrupoP{Count}'][i][1] += iVitoria
                break
        elif Placar1 == Placar2:
            if item[0] in Nome1:
               Pontuacao_Grupo[f'iGrupoP{Count}'][i][1] += iEmpate
            if item[0] in Nome2:
                Pontuacao_Grupo[f'iGrupoP{Count}'][i][1] += iEmpate
                break
            
