import os

print('='*120)
print('Noções basicas de  matemática financeira:.')

print('='*120)
print('..Capital ou Valor Presente(C ou VP)..')
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
print('J = C x i')
print('i = J / C')
print('')
print('Exemplo: um capital de 1000 aplicado a uma taxa de 12% ao mês. qual é o montante ao final do mês\n')
print('J = C x i : J = 1000 x 0,12 = 120')
print('M=C + J : M=1000 + 120 = 1120')
print('='*120)
print('.Agora vamos aplicar esse conhecimento.')
print('Nessa primeira lição vamos estabeler o tempo n = 1 unidade \n')
lista=[]
lembrete=(input('Lembre-se faça o exercício sozinho depois volte aqui e confira o resultado!. Tecle enter para continuar'))
print('Qual variável vc quer descobrir?')
print('Obs: se for pedido uma variável que não consta no exercício ou não afete o resultado digite zero ou se tiver o valor digite-o\n')
while True:
    variável=(input('\nDigite M para montante; C para capital; J para juros; i para taxa de juros ou X para sair e mostrar o resultado: '))
    if variável=='X' or variável=='x':
        break
    elif variável=='M' or variável=='m':
        capital_inicial=float(input('Qual é o valor do Capital inicial: '))
        juros=float(input('Qual é o valor dos Juros: '))
        i=float(input('Qual é o valor da taxa de juros: '))
        montante=capital_inicial+juros
        lista.append(variável)
        
    elif variável=='C' or variável=='c':
        montante=float(input('Qual o valor do montante: '))
        juros=float(input('Qual o valor dos juros: '))
        i=float(input('Qual é o valor da taxa de juros: '))
        capital_inicial=montante-juros
        lista.append(variável)

    elif variável=='J' or variável=='j':
        capital_inicial=float(input('Qual o valor do capital inicial: '))
        i=float(input('Qual é o valor da taxa de juros: '))
        montante=float(input('Qual é o valor do montante: '))
        juros=capital_inicial*i
        lista.append(variável)

    elif variável=='i' or variável=='I':
        montante=float(input('Qual o valor do montante:  '))
        capital_inicial=float(input('Qual o valor do capital inicial: '))
        juros=float(input('Qual o valor dos juros: '))
        i=juros/capital_inicial
        lista.append(variável)

    else:
        print('Variável inválida. Favor digitar novamente!')
        variável=(input('Digite M para montante; C para capital; J para juros; i para taxa de juros ou X para sair e mostrar o resultado: '))
passo_a_passo=(input('Ver apenas o resultado tecle enter ou P para ver o passo a passo do exercício: '))
print('='*120)
if 'm' in lista or 'M' in lista:
    print('Montante = C + J')
    print('Montante = {} + {} = {}'.format(capital_inicial,juros,montante))
    print('='*120)
if 'c' in lista or 'C' in lista:
    print('capital inicial = M - J')
    print('Capital inicial = {} - {} = {}'.format(montante,juros,capital_inicial))
    print('='*120)
if 'j' in lista or 'J' in lista:
    print('Juros = C x i')
    print('Juros = {} x {} = {}'.format(capital_inicial,i,juros))
    print('='*120)
if 'i' in lista or 'I' in lista:
    print('Taxa de juros = J / C')
    print('Taxa de juros = {} / {} = {} ou {}%'.format(juros,capital_inicial,i,i*100))
print('='*120)
print('RESULTADO')
print('')
print('Montante = ',montante)
print('Capital inicial = ',capital_inicial)
print('Juro = ',juros)
print('Taxa de juros = ',i,' ou ',i*100,'%')

print('='*120)
os.system('pause')

