pos = 0
soma = 0
for i in range(6):
    valores = float(input())
    if valores > 0:
        pos +=1
        soma = soma + valores
print(f'{pos} valores positivos')
print(f'{soma/pos}')