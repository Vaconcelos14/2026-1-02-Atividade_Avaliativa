# Escreva um programa Python que leia um número inteiro positivo e armazene na variável repeticoes;
# e exiba na tela uma sequência de repeticoes números inteiros aleatórios entre 1 e 100.
import random
repetiçoes = int(input(f"Digite a quantidade de números aleatórios: "))
for i in range (repetiçoes+1):
    num_ale = random.randint(1, 100)
    print(f"{i}o número aleatório: {num_ale}")
