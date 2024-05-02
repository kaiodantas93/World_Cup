from Cup import dados

dados.iSelecao()

while True:
    iEscolha = str(input('Escolha a sua selecao: ')).strip()
    if dados.iGrupo(iEscolha.capitalize()):
        break
