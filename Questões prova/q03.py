num = int(input("Digite seu número: "))
soma=0
if num>0:
    for i in range (1, num):
        if num%i==0:
            soma+= i
    if soma==num:
        print(f"{num} é perfeito")
    else:
        print(f"{num} não é perfeito")
else:
    print("O número precisa ser positivo")

