repeticoes = int(input("Digite a qunatidade de números: "))
valores=[]
if repeticoes>0:
    for i in range (repeticoes):
        n =int(input(f"O valor {i+1}: "))
        valores.append(n)
        soma = sum(valores)
        media = soma/repeticoes
        maior = max(valores)
        menor = min(valores)
        cont = 0

    for v in valores:
        if v > media:
            cont+=1
print(f"A soma é: {soma}")
print(f"A média é: {media}")
print(f"O maior valor é: {maior}")
print(f"O menor valor é: {menor}")
print(f"a quantidade de números maior que a média: {cont} ")

