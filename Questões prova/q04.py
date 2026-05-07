num = int(input("Digite seu número: "))
caracteres = 0
while num>0:
    num=num//10
    caracteres+=1
print(caracteres)