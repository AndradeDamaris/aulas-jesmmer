def val(quant):
    pos = 0
    soma = 0
    for i in range(quant):
        valores= float(input())
        if valores > 0:
            pos += 1
            soma = soma + valores
    media = soma/pos
    return pos, media
quant = 6
pos, media = val(quant)
print(f"{pos} valores positivos")
print(f"{media:.1f}")