# Bruno gerencia um pequeno comércio e quer saber qual produto teve o melhor desempenho de vendas no mês passado. Ele registrou a quantidade vendida de dois produtos: maçãs e bananas. Agora, ele precisa escrever um programa que identifique e exiba qual deles teve maior venda.

macas = int(input('Insira a quantidade de maçãs vendidas: '))
bananas = int(input('Insira a quantidade de bananas vendidas: '))

if bananas > macas:
    print('As bananas tiveram mais vendas.')
elif macas > bananas:
    print('As maçãs tiveram mais vendas.')
else:
    print('Ambas tiveram a mesma quantidade vendida.')
