# Programa Teste Para Calculo de IMC
from dev import calculo_imc, classificacao

nome = input("Digite seu nome: ")
altura = float(input("\nDigite sua altura: "))
peso = float(input("\nDigite seu peso: "))

imc = calculo_imc(peso, altura)


print(f'{nome}, seu IMC é {imc:.2f}.', classificacao(imc))