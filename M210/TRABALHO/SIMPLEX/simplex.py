import numpy as np
import math

def simplex(table, lines, columns, decisions_variables, constraints):
    columns = columns - 1                                                       #O NÚMERO DE COLUNAS É REDUZIDO POR 1 P/ EXCLUIR A COLUNA DE RESULTADOS
    pivotColumnIndex = findPivotColumn(table, columns)                          #CALCULAR A COLUNA PIVÔ INICIAL (CHAMANDO A FUNÇÃO FINDPIVOTCOLUMN)
    variables = np.zeros(lines)                                                 #INICIALIZA UM VETOR PARA ARMAZENAR AS VARIÁVEIS DE PIVÔ
    print("\nCONSTRUÇÃO DO QUADRO SIMPLEX (TABELA INICIAL):\n" + str(table))    #IMPRIME A TABELA INICIAL

    iteration = 1
    while pivotColumnIndex != -1:                                                           #O LOOP WHILE É EXECUTADO ENQUANTO HOUVER UMA COLUNA PIVÔ VÁLIDA!
        pivotRowIndex = rowPivotCalculate(table, lines, columns, pivotColumnIndex)          #CALCULA A LINHA PIVÔ (CHAMANDO A FUNÇÃO ROWPIVOTCALCULATE)
        variables[pivotRowIndex] = pivotColumnIndex                                         #ARMAZENA A VARIÁVEL DE PIVÔ PARA A LINHA PIVÔ
        table = createNewTable(table, lines, columns, pivotRowIndex, pivotColumnIndex)      #CRIA UMA NOVA TABELA COM OS VALORES PIVÔ ATUALIZADOS
        print("\nIteração " + str(iteration) + ":\n" + str(table))                          #IMPRIME A NOVA TABELA
        pivotColumnIndex = findPivotColumn(table, columns)                                  #CALCULA A PRÓXIMA COLUNA PIVÔ
        iteration += 1

    #APÓS O TÉRMINO DO LOOP, SÃO EXIBIDOS OS RESULTADOS:
    print("\nVARIÁVEIS DE DECISÃO/SOLUÇÃO ÓTIMA:")
    for i in range(decisions_variables):
        col = [table[j][i] for j in range(lines)]
        if col.count(0) == lines - 1 and col.count(1) == 1:
            rowIndex = col.index(1)
            print("X" + str(i + 1) + " =", table[rowIndex][-1])
        else:
            print("X" + str(i + 1) + " = 0 (FORA DA BASE)")

    print("\nPREÇO SOMBRA:")
    for i in range(0, constraints):
        print("X" + str(i + 1) + " = " + str(table[0][i + decisions_variables]))

    print("\nLUCRO ÓTIMO: " + str(table[0][-1]))



#FUNÇÃO QUE ENCONTRA/RETORNA O ÍNDICE DA COLUNA PIVÔ (COLUNA QUE CONTÉM O MENOR VALOR NEGATIVO DA FUNÇÃO OBJETIVO)
def findPivotColumn(table, columns):
    lowestNegativeValue = 0                         #LOWESTNEGATIVEVALUE É INICIALIZADA COM 0 E REPRESENTA O MENOR VALOR NEGATIVO ENCONTRADO.
    pivotColumnIndex = -1                           #PIVOTCOLUMNINDEX É INICIALIZADA COM -1 E REPRESENTA O ÍNDICE DA COLUNA PIVÔ.

    for i in range(0, columns):                     #O LOOP FOR PERCORRE AS COLUNAS DA TABELA.
        if table[0][i] < lowestNegativeValue:       #SE O VALOR NA POSIÇÃO ATUAL (TABLE[0][i]) FOR MENOR QUE LOWESTNEGATIVEVALUE
            lowestNegativeValue = table[0][i]       #ATUALIZA-SE LOWESTNEGATIVEVALUE E PEGA O ÍNDICE DELE (PIVOTCOLUMNINDEX)
            pivotColumnIndex = i
    return pivotColumnIndex                         #RETORNA O PIVOTCOLUMNINDEX, QUE REPRESENTA O ÍNDICE DA COLUNA PIVÔ.



#FUNÇÃO QUE CALCULA A LINHA PIVÔ, RETORNANDO O ÍNDICE DA LINHA QUE CONTÉM O MENOR VALOR POSITIVO NA DIVISÃO ENTRE O RESULTADO DA LINHA E O VALOR NA COLUNA PIVÔ.
def rowPivotCalculate(table, lines, columns, pivotColumnIndex):
    lowestPositiveValue = math.inf                                      #LOWESTPOSITIVEVALUE É INICIALIZADA COM INFINITO POSITIVO E REPRESENTA O MENOR VALOR POSITIVO ENCONTRADO.
    pivotRowIndex = -1                                                  #PIVOTROWINDEX É INICIALIZADA COM -1 E REPRESENTA O ÍNDICE DA LINHA PIVÔ.

    for i in range(0, lines):                                           #O LOOP FOR PERCORRE AS LINHAS DA TABELA.
        if table[i][pivotColumnIndex] != 0:                             #SE O VALOR NA POSIÇÃO ATUAL (TABLE[I][PIVOTCOLUMNINDEX]) FOR DIFERENTE DE 0,
            division = table[i][columns] / table[i][pivotColumnIndex]   #CALCULA-SE A DIVISÃO ENTRE O VALOR NA COLUNA DE RESULTADOS (TABLE[I][COLUMNS]) E O VALOR NA COLUNA PIVÔ (TABLE[I][PIVOTCOLUMNINDEX]).
        else:
            division = math.inf                                         #CASO CONTRÁRIO, A DIVISÃO É DEFINIDA COMO INFINITO.

        if (division > 0 and division < lowestPositiveValue):           #SE A DIVISÃO FOR MAIOR QUE 0 E MENOR QUE LOWESTPOSITIVEVALUE, ATUALIZA-SE LOWESTPOSITIVEVALUE E PIVOTROWINDEX.
            lowestPositiveValue = division                              #ATUALIZA-SE LOWESTPOSITIVEVALUE E PIVOTROWINDEX.
            pivotRowIndex = i

    return pivotRowIndex                                                #RETORNA O PIVOTROWINDEX, QUE REPRESENTA O ÍNDICE DA LINHA PIVÔ.



#FUNÇÃO QUE CRIA UMA NOVA TABELA COM OS VALORES ATUALIZADOS APÓS A ITERAÇÃO DO MÉTODO SIMPLEX.
def createNewTable(table, lines, columns, pivotRowIndex, pivotColumnIndex):
    pivot = table[pivotRowIndex][pivotColumnIndex]                  #PIVOT RECEBE O VALOR NA POSIÇÃO PIVÔ (TABLE[PIVOTROWINDEX][PIVOTCOLUMNINDEX]).
    newTable = np.zeros((lines, columns + 1))                       #NEWTABLE É CRIADA COMO UMA NOVA TABELA COM UMA COLUNA ADICIONAL.

    for i in range(0, columns + 1):                                                                 #ESTE LOOP PREENCHE A LINHA PIVÔ NA NOVA TABELA
        newTable[pivotRowIndex][i] = np.around(table[pivotRowIndex][i] / pivot, 4)                  #DIVIDINDO CADA VALOR PELO PIVÔ E ARREDONDANDO PARA 4 CASAS DECIMAIS.

    for i in range(0, lines):                                                                         #ESTE LOOP PERCORRE TODAS AS LINHAS E COLUNAS DA NOVA TABELA.
        for j in range(0, columns + 1):
            if i != pivotRowIndex:                                                                    #SE A LINHA NÃO FOR A LINHA PIVÔ (LINHA DE REFERÊNCIA)
                parameter = table[i][pivotColumnIndex] * -1                                           #CALCULA-SE O PARÂMETRO COMO SENDO O VALOR NA COLUNA PIVÔ MULTIPLICADO POR -1
                newTable[i][j] = np.around(table[i][j] + (parameter * newTable[pivotRowIndex][j]), 4) #O VALOR NA POSIÇÃO ATUAL DA NOVA TABELA É ATUALIZADO SOMANDO O VALOR CORRESPONDENTE NA TABELA ORIGINAL (LINHA ANTIGA)
                                                                                                      #COM O PRODUTO DO PARÂMETRO E O VALOR NA MESMA POSIÇÃO DA LINHA PIVÔ NA NOVA TABELA (LINHA DE REFERENCIA)
    return newTable



def main():
    print("MÉTODO SIMPLEX...\n")
    decisions_variables = int(input("Número de variáveis de decisão: "))
    constraints = int(input("Número de restrições (Exceto a restrição de não-negatividade): "))
    #op = int(input("QUAL O OBJETIVO DA FUNÇÃO (1-MÁX / 2-MIN): "))

    columns = decisions_variables + constraints + 1 #É IGUAL A SOMA DAS VARIÁVEIS DE DECISÃO E DAS RESTRIÇÕES MAIS UMA COLUNA ADICIONAL PARA O RESULTADO.
    lines = constraints + 1                         #É IGUAL AO NÚMERO DE RESTRIÇÕES MAIS UMA LINHA ADICIONAL PARA A FUNÇÃO OBJETIVO.

    #SOLICITA AO USUÁRIO QUE ENTRE COM A FUNÇÃO OBJETIVO NA FORMA CANÔNICA, PREENCHENDO O VETOR OBJETIVO Z COM OS COEFICIENTES DAS VARIÁVEIS DE DECISÃO.
    print("\nEntre com a função objetivo (z) (NA FORMA CANÔNICA):")
    z = np.zeros(columns)
    for i in range(0, decisions_variables):
        z[i] = (int(input('X' + str(i + 1) + ': ')))

    #CRIANDO A PRIMEIRA TABELA E PREENCHENDO AS RESTRIÇÕES
    table = np.zeros((lines, columns))

    #PREENCHE A PRIMEIRA LINHA COM OS COEFICIENTES DA FUNÇÃO OBJETIVO, INVERTIDOS E MULTIPLICADOS POR -1.
    for i in range(0, columns):
        if z[i] != 0:
            table[0][i] = z[i] * -1

    #PREENCHE AS RESTRIÇÕES E MONTA A TABELA. PARA CADA RESTRIÇÃO, SOLICITA AO USUÁRIO QUE ENTRE COM OS COEFICIENTES DAS VARIÁVEIS DE DECISÃO E O OPERADOR DE DESIGUALDADE (<= OU >=).
    for i in range(1, lines):
        print("Restrição " + str(i) + " (FORMA CANÔNICA):")
        option = 0

        for j in range(0, columns):
            #SE ESTIVER ENTRANDO COM OS X DA RESTRIÇÃO
            if j < decisions_variables:
                table[i][j] = (input('X' + str(j + 1) + ': '))

            #SE ESTIVER ENTRANDO COM O FINAL DA RESTRIÇÃO
            elif j == columns - 1:
                if option == 1:
                    table[i][j] = (input('<= '))
                else:
                    table[i][j] = (input('>= '))

            #OS COEFICIENTES SÃO ARMAZENADOS NA TABELA, E O VALOR 1 OU -1 É COLOCADO AUTOMATICAMENTE NA COLUNA CORRESPONDENTE AO COEFICIENTE DA VARIÁVEL DA RESTRIÇÃO.
            elif j == i + (decisions_variables) - 1:
                option = int(input("1 - <= / 2 - >= : "))
                if option == 1:
                    table[i][i + (decisions_variables) - 1] = 1
                else:
                    table[i][i + (decisions_variables) - 1] = -1

    #CHAMANDO A FUNÇÃO P/ REALIZAR O MÉTODO SIMPLEX - PASSANDO A TABELA, O NÚMERO DE LINHAS E COLUNAS, O NÚMERO DE VARIÁVEIS DE DECISÃO E O NÚMERO DE RESTRIÇÕES
    simplex(table, lines, columns, decisions_variables, constraints)

if __name__ == "__main__":
    main()
