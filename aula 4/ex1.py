i = 1
positivos = 0
while i <= 6:
    valor = float(input())
    if valor > 0:
        positivos+=1
    i+=1
print(f'{positivos} valores positivos')