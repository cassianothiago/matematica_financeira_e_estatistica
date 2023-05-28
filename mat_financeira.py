import os

print('='*120)
print('Noções basicas de  matemática financeira:.')

print('='*120)
print('..Capital ou Valor Presente(VP ou C)..')
print('  Capital inicial(Principal)\n')
print('..Juros (J)..')
print('  Remunerção do capital\n')
print('..Taxas de juros(i) sua representação costuma ser em %..')
print('  valor da taxa de juros em um determinado tempo\n')
print('..Prazo ou Período(n)..')
print('  Unidade de tempo\n')
print('..Montante ou valor futuro(VF ou M)')
print('  Valor final da operação')
print('='*120)

print('formulação básica:.')

print('='*120)
print('M = C + J')
print('J=C x i')
print('i = J/C')
print('')
print('Exemplo: um capital de 1000 aplicado a uma taxa de 12% ao mês. qual é o montante ao final do mês\n')
print('J = C x i : J = 1000 x 0,12 = 120')
print('M=C + J : M=1000 + 120 = 1120')
print('='*120)
print('.Agora vamos aplicar esse conhecimento.')
print('Nessa primeira lição vamos estabeler o tempo n = 1 unidade \n')
lembrete=(input('Lembre-se faça o exercício sozinho depois volte aqui e confira o resultado!. Tecle enter para continuar'))
print('qual variável vc quer descobrir?')
while True:
    variável=(input('Digite M para montante; C para capital; J para juros; i para taxa de juros ou X para sair e mostrar o resultado: '))
    if variável=='X' or variável=='x':
        break
    elif variável=='M' or variável=='m':
        capital_inicial=float(input('Qual é o valor do Capital inicial: '))
        juros=float(input('Qual é o valor do Juro: '))
        montante=capital_inicial+juros
    elif variável=='C' or variável=='c':
        montante=float(input('Digite o valor do montante: '))
        juros=float(input('Digite o valor do juro: '))
        capital_inicial=montante-juros
    elif variável=='J' or variável=='j':
        montante=float(input('Digite o valor do montante: '))
        capital_inicial=float(input('Digite o valor do capital inicial: '))
        i=int(input('Digite a taxa de juros(i): '))
        juros=capital_inicial*i
    elif variável=='i' or variável=='I':
        montante=float(input('Digite o valor do montante:  '))
        capital_inicial=float(input('Digite o valor do capital inicial: '))
        juros=float(input('Digite o valor dos juros: '))
        i=juros/capital_inicial
    else:
        print('Variável inválida. Favor digitar novamente!')
        variável=(input('Digite M para montante; C para capital; J para juros; i para taxa de juros ou X para sair e mostrar o resultado: '))
print('='*120)
print('Montante = ',montante)
print('Capital inicial = ',capital_inicial)
print('Os juros = ',juros)
print('Taxa de juros(i) = {:.2f} ou {:.2f}%'.format(i,i*100))

print('='*120)
os.system('pause')
