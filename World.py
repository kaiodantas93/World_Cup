from Cup import dados

dados.iSelecao()
resultado = False

while not resultado:
    dados.iEscolha_Selecao = str(input('Escolha a sua selecao: ')).lower().capitalize()
    for k in range(1 , 9):
        if dados.iEscolha_Selecao in dados.iClassificacao[f'iGrupoP{k}']:
            if dados.iGrupo_Sel():
                resultado = True
                break
    
        

