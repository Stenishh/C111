km = int(input('Quantos kms sera sua viagem ?: '))

if km <= 200:
    passagem = km * 0.50 
    print('Preço final de R$',passagem)
else:
    passagem = km * 0.45 
    print('Preço final de R$',passagem)