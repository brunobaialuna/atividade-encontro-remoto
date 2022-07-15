# App de Cálculo de IMC

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / altura ** 2

print(f'Seu imc é {imc:.2f}')

