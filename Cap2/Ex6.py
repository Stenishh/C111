import math

numero = float(input("Digite um número decimal: "))

raiz_quadrada = math.sqrt(numero)
teto = math.ceil(numero)
chao = math.floor(numero)
parte_inteira = int(numero)

print("Raiz quadrada:", raiz_quadrada)
print("Função teto:", teto)
print("Função chão:", chao)
print("Parte inteira:", parte_inteira)
