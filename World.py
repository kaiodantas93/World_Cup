from Cup import dados

dados.iSelecao()

while True:
    iEscolha = str(input('Escolha a sua selecao: ')).lower()
    if dados.iGrupo_Sel(iEscolha.capitalize()):
        break
