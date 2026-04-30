def inOut(N, menor, maior):
    dentro = 0
    fora = 0
    for i in range(N):
        valores = int(input())
        if valores >= menor and valores <= maior:
            dentro +=1
        else:
            fora +=1
    return dentro, fora
N = int(input())
dentro, fora = inOut(N, 10, 20)
print(f"{dentro} in")
print(f'{fora} out')