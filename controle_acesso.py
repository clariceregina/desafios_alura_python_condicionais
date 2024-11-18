# Mariana é responsável por liberar o acesso ao escritório e precisa de um programa que verifique se os funcionários podem entrar. Para isso, ela usará o horário atual. O escritório só permite acesso entre 8h e 18h. Crie um programa que receba a hora atual como entrada (em formato de 24 horas) e exiba uma mensagem informando se o acesso é permitido ou negado.

hora_atual = int(input('Insira a hora atual (formato 24h): '))

if 8 < hora_atual > 18:
    print('Acesso negado. Tente entre 8h e 18h.')
else:
    print('Acesso autorizado. Boas-vindas!')
