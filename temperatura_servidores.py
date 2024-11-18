# Lucas trabalha em TI e precisa garantir que a temperatura de uma sala de servidores não ultrapasse 25°C. Ele quer um programa que receba a temperatura atual como entrada e, se necessário, exiba uma mensagem de alerta.

temperatura_atual = float(input('Insira a temperatura atual: '))

if temperatura_atual <= 20:
    print('A temperatura do servidor está ideal.')
elif temperatura_atual > 20 and temperatura_atual < 25:
    print('Atenção: temperatura perto de 25°C.')
else:
    print('A temperatura é igual a 25°C ou ultrapassou este limite.')
