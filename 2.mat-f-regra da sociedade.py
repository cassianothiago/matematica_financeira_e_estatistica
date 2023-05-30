import os

print('='*120)
print('Regra da sociedade:.')
print('Modelo matemático de distribuição de resultado:.')
print('='*120)
print('..Menbros da sociedade(M)..')
print('  Participantes da sociedade')
print('..Tempo(t)..')
print('  tempo de participação de cada menbro na sociedade')
print('..Peso(P)..')
print('  Proporção do capital entre os membros')
print('..Capital total(C)..')
print('  Total de capital de cada participante.')
print('='*120)

print('Formulação básica')
print('P = C x T')
print('C = C1 + C2 + ... + Cn = Capital total')

print('Exemplo: Três pessoas formaram uma sociedade, A entrou com 24.000 R$; B com 30.000 R$ e C com 36.000 R$. Depois de três meses tiveram o lucro de 60.000 R$')
print('Calcule o lucro de cada sócio')
print('A / 24000 = B / 30000 = c / 36000 = (A + B + C) / 90000 = 60000 / 90000 = 2 / 3')
print('Logo A = 24000 x 2/3 = 16000')
print('     B = 30000 x 2/3 = 20000')
print('     C = 36000 x 2/3 = 24000')
print('                       =====')
print('         Lucro Total = 60000')

print('.Agora vamos aplicar esse conhecimento.')

socios=int(input('Quantos sócios possuem a sociedade:  '))

for i in range(socios):
    entradas=float(input('Digite quanto o {}º '))
