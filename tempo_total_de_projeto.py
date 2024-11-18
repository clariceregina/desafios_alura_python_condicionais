# Camila está organizando um projeto e precisa calcular o tempo total necessário para concluir três atividades: A, B e C. No entanto, se alguma atividade tiver um número de dias negativo, o código deve avisar que os valores inseridos são inválidos e não calcular o total.

a = int(input('Insira a quantidade de dias necessários para concluir a Atividade A'))
b = int(input('Insira a quantidade de dias necessários para concluir a Atividade B'))
c = int(input('Insira a quantidade de dias necessários para concluir a Atividade C'))

if a < 0 or b < 0 or c < 0:
    print('Erro: os números devem ser positivos.')
else:
    tempo_total = a + b + c
    print(f'O tempo total do projeto é de {tempo_total} dias.')
