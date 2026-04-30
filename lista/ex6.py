# raio = float(input())
# n = 3.14159
# area = n*(raio**2)
# print(f'A = {area:.4f}')
raio = int(input())
n = 3.14159
for i in range(raio):
    area = n*(raio**2)
    print(f'A de {raio} = {area:.4f}')
    raio = raio - 1