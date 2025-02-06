sexo = input('Qual seu sexo? F -> para Mulher e M -> para Homem: ')

while sexo != 'M' and sexo != 'F':
    print("Entrada inválida. Digite 'M' para homem ou 'F' para mulher.")
    sexo = input('Qual seu sexo? F -> para Mulher e M -> para Homem: ')
print('Agora esta certo!')