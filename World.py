from Cup import dados

dados.iSelecao()

while True:
    #iEscolha = str(input('Escolha a sua selecao: ')).lower().capitalize()
    iEscolha = "Brasil"
    for k in range(1 , 9):
        if iEscolha in dados.iClassificacao[f'iGrupoP{k}']:
            if dados.iGrupo_Sel(iEscolha):
                break
    break
        
