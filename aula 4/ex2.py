i = 1
positivos = 0
soma = 0
while i<=6:
    valores = float(input())
    if valores > 0:
        positivos+=1
        soma += valores
    i +=1
media = soma/positivos

print(f'{positivos} valores positivos')
print(media)