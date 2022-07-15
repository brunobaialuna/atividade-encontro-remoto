# App de Cálculo de IMC

nome = input("Digite seu nome: ")
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / altura ** 2

print(f'{nome}, seu imc é {imc:.2f}')

