import math

# Solicita um número decimal ao usuário
numero = float(input("Digite um número decimal: "))

# Calcula os valores solicitados
raiz_quadrada = math.sqrt(numero)
teto = math.ceil(numero)
chao = math.floor(numero)
parte_inteira = int(numero)

# Exibe os resultados
print("Raiz quadrada:", raiz_quadrada)
print("Função teto:", teto)
print("Função chão:", chao)
print("Parte inteira:", parte_inteira)
