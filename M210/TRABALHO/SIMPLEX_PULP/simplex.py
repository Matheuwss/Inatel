from pulp import *

#CRIAR O PROBLEMA DE PROGRAMAÇÃO LINEAR
def create_problem_LP(num_variaveis, num_restricoes, coef_objetivo, coef_restricoes, restricoes):
    #CRIAR O PROBLEMA
    problem = LpProblem("PROBLEMA DE PROGRAMAÇÃO LINEAR", LpMaximize)

    #CRIAR AS VARIÁVEIS
    variaveis = [LpVariable(f"x{i+1}", lowBound=0) for i in range(num_variaveis)]

    #DEFINIR A FUNÇÃO OBJETIVO
    problem += lpSum(coef_objetivo[i] * variaveis[i] for i in range(num_variaveis))

    #ADICIONAR AS RESTRIÇÕES
    for i in range(num_restricoes):
        problem += lpSum(coef_restricoes[i][j] * variaveis[j] for j in range(num_variaveis)) <= restricoes[i]

    return problem

#RESOLVER O PROBLEMA UTILIZANDO O MÉTODO SIMPLEX
def solve_problem_LP(problem, coef_objetivo):
    #RESOLVER O PROBLEMA
    problem.solve(PULP_CBC_CMD(msg=False))

    #VERIFICAR O STATUS DA SOLUÇÃO
    status = LpStatus[problem.status]

    #RECUPERAR OS VALORES DAS VARIÁVEIS
    solution = [value(var) for var in problem.variables()]

    #RECUPERAR OS PREÇOS SOMBRA
    shadow_prices = [constraint.pi for constraint in problem.constraints.values()]

    #CALCULAR O LUCRO ÓTIMO
    great_profit = sum(coef_objetivo[i] * solution[i] for i in range(len(solution)))

    #VERIFICAR A VIABILIDADE DAS RESTRIÇÕES
    viabilidade_restricoes = [restricao.slack >= 0 for restricao in problem.constraints.values()]

    return status, solution, shadow_prices, great_profit, viabilidade_restricoes

#FUNÇÃO PRINCIPAL
def main():
    #ENTRADA DE DADOS
    num_variaveis = int(input("Número de variáveis: "))
    num_restricoes = int(input("Número de restrições (Exceto as restrições de não-negatividade): "))

    coef_objetivo = []
    for i in range(num_variaveis):
        coef = float(input(f"Coeficiente da função objetivo para x{i+1}: "))
        coef_objetivo.append(coef)

    coef_restricoes = []
    for i in range(num_restricoes):
        coef_restricao = []
        for j in range(num_variaveis):
            coef = float(input(f"Coeficiente da restrição {i+1} para x{j+1}: "))
            coef_restricao.append(coef)
        coef_restricoes.append(coef_restricao)

    restricoes = []
    for i in range(num_restricoes):
        valor = float(input(f"Valor da restrição {i+1}: "))
        restricoes.append(valor)

    #CRIAR O PROBLEMA DE PROGRAMAÇÃO LINEAR
    problem = create_problem_LP(num_variaveis, num_restricoes, coef_objetivo, coef_restricoes, restricoes)

    #RESOLVER O PROBLEMA
    status, solution, shadow_prices, great_profit, viabilidade_restricoes = solve_problem_LP(problem, coef_objetivo)

    #EXIBIR OS RESULTADOS
    print("\nResultado:")
    print(f"Status: {status}\n")
    print("VARIÁVEIS DE DECISÃO/PRODUÇÃO ÓTIMA:")
    for i in range(num_variaveis):
        print(f"x{i+1} = {solution[i]}")

    print(f"\nLUCRO ÓTIMO/VALOR ÓTIMO DA FUNÇÃO OBJETIVO: {great_profit}\n")
    print("PREÇO SOMBRA:")
    for i in range(num_restricoes):
        print(f"Restrição {i+1}: {shadow_prices[i]}")

    print("\nViabilidade das restrições:")
    for i in range(num_restricoes):
        print(f"Restrição {i+1}: {'Viável' if viabilidade_restricoes[i] else 'Não viável'}")

if __name__ == '__main__':
    main()