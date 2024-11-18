# Anna Júlia está criando um sistema para calcular o Índice de Massa Corporal (IMC) e fornecer recomendações básicas. O programa deve receber o peso e a altura de uma pessoa e exibir o valor do IMC, além de indicar se está abaixo do peso, com peso normal ou acima do peso. Crie um programa que receba o peso (em kg) e a altura (em metros) e calcule o IMC usando a fórmula: IMC = peso / (altura ** 2) Depois, exiba o valor do IMC e uma mensagem indicando se está abaixo do peso (IMC < 18.5), peso normal (18.5 <= IMC < 25) ou acima do peso (IMC >= 25).

peso = float(input('Insira o peso em Kg: '))
altura = float(input('Insira a altura em metros: '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print(f'Seu imc é {imc}.\nVocê está abaixo do peso.')
elif imc < 25:
    print(f'Seu imc é {imc}.\nVocê está com o peso esperado para sua altura.')
else:
    print(f'Seu imc é {imc}.\nVocê está acima do peso.')
