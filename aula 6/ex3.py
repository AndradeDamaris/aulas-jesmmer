x = [0] *5
for i,v in enumerate(x):
    valores = int(input())
    x[i] = valores

def ler(x):
    for i,v in enumerate(x):
        if v <= 0:
            x[i] = 1
    return x
nova = ler(x)

for i, v in enumerate(nova):
    print(f'X[{i}] = {v}')