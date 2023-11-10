idade = int(input("Digite a idade em dias: "))


anos = idade // 365
meses = (idade % 365) // 30
dias = (idade % 365) % 30

print(anos , meses ,  dias )
