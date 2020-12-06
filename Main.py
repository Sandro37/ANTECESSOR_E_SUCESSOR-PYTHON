var = int(input("Entre com um numero: "))
vet = []

print(type(vet))

vet.append(var - 1)
vet.append(var + 1)

for i in vet:
    print(i)

print("Considerando o {0} seu antecessor é {1} e seu sucessor é {2}".format(var,vet[0], vet[1]))