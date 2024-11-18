# Carlos quer monitorar seu orçamento mensal para evitar gastos excessivos. Ele estabeleceu um limite de R$ 3.000,00 para seus gastos e precisa de um programa que ajude a controlar suas despesas. O programa deve receber o total de despesas realizadas e informar se ele ultrapassou o limite ou ainda está dentro do orçamento.

total_despesas = float(input('Insira o total de despesas no mês: '))
limite = 3000

if total_despesas <= limite:
    print('Você está dentro do orçamento. Parabéns!')
else:
    print('Você estourou seu orcamento. Para não ter complicações futuras se atente aos gastos.')
