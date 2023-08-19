'''nome = input('digite o seu cpf: ')

indice = 0
novo_cpf = ''

while indice < len(nome):
   letra = nome[indice]
   novo_cpf += f'{letra}'
   indice += 1

print(novo_cpf)'''

cpf = input('Digite o seu cpf:')

nove_digitos = cpf[:9]
contador_regressivo_1 = 10
resultado_dig_1=0

for digito_1 in nove_digitos:
    resultado_dig_1 += int(digito_1) * contador_regressivo_1
    contador_regressivo_1 -= 1

digito_1 = (resultado_dig_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0


dez_digitos = cpf[:9] + str(digito_1)
contador_regressivo_2 = 11
resultado_dig_2 = 0

for digito_2 in dez_digitos:
    resultado_dig_2 += int(digito_2) * contador_regressivo_2
    contador_regressivo_2 -= 1

digito_2 = (resultado_dig_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

validacao_cpf = f'{nove_digitos}{digito_1}{digito_2}'
if validacao_cpf == cpf:
    print('O CPF é Válido')
else: print('O CPF não confere')

#validadção



'''print (f'{cpf[:9]}{digito_1}{digito_2}')'''