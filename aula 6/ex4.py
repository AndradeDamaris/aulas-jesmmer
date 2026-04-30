valores = [0] * 5
def troca():
    for i, v in enumerate(valores):
        valor = int(input())
        valores[4-i] = valor
        return valores
troca = troca(valores)
for i, v in range()