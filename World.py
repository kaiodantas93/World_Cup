from Cup import dados

dados.iSelecao()
resultado = False

while True:
    iEscolha = str(input('Escolha a sua selecao: ')).lower().capitalize()
    for k in range(1 , 9):
        if iEscolha in dados.iClassificacao[f'iGrupoP{k}']:
            if dados.iGrupo_Sel(iEscolha):
                resultado = True
                break
       
    if resultado:
        break
    
        

