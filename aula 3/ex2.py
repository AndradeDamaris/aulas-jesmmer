valor = int(input())

anos = valor // 365
valor = valor % 365
meses = valor // 30
valor = valor % 30
dias = valor

print(f'{anos} ano(s)')
print(f'{meses} mes(es)')
print(f'{dias} dia(s)')