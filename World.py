from Cup import dados

dados.iSelecao()

while True:
    #iEscolha = str(input('Escolha a sua selecao: ')).lower()
    iEscolha = "Colombia"
    if dados.iGrupo_Sel(iEscolha.capitalize()):
        break
