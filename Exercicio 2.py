# Como descobrir o ano Bissexto

# Apresentação
print('\n\t\t\t -- Descobrir o ano Bissexto -- \n')

# Entrada
ano = int(input('Ano: '))

# Processamento
if (ano% 4==0 and ano% 100!=0) or (ano% 400==0):
    print('Bissexto')

else:
    print('Não é bissexto')


