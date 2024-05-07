from random import choice, randint
from time import sleep

iClassificao = {
    'iGrupoP1': [], 'iGrupoP2': [], 'iGrupoP3': [], 'iGrupoP4': [],
    'iGrupoP5': [], 'iGrupoP6': [], 'iGrupoP7': [], 'iGrupoP8': []
}


def iSelecao():

    iCopa = {
        'iSelecoesP1': ['Qatar', 'Brasil', 'Argentina', 'Belgica', 'Espanha', 'França', 'Inglaterra', 'Portugal'],
        'iSelecoesP2': ['Alemanha', 'Croacia', 'Dinamarca', 'Estados Unidos', 'Holanda', 'Mexico', 'Suica', 'Uruguai'],
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
    while True:
        for c in range(1, 9):
            print(f'Jogos do Grupo {c}')
            Sel_Principal = iClassificao[f'iGrupoP{c}'][0]
            for k in iClassificao[f'iGrupoP{c}']:
                Placar1 = randint(1, 4)
                Placar2 = randint(1, 4)
                if Sel_Principal in k:
                    continue
                else:
                    print(f'{Sel_Principal} {Placar1} x {Placar2} {k}')
        break
