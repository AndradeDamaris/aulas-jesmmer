# valor = int(input())
# horas = valor // 3600
# valor = valor % 3600
# minutos = valor//60
# segundos = valor %60

# print(f'{horas}:{minutos}:{segundos}')

valor = int(input())
valor2 = valor 
for i in range(valor):
    if valor == valor2:
        horas = valor // 3600
        valor = valor % 3600
        minutos = valor//60
        segundos = valor %60
        print(f'{horas}: {minutos}:{segundos}')
    else:
        horas = valor2 // 3600
        valor = valor2 % 3600
        minutos = valor2//60
        segundos = valor2 %60
        
        print(f'{horas}: {minutos}:{segundos}')
    valor2 = valor *2
