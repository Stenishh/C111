numero = int(input("Escolha um número: "))  # Converte a entrada para inteiro

print('Tabuada:')
for i in range(1, 10 + 1):
    print(f"{numero} x {i} = {numero * i}")  # f-string corrigida
