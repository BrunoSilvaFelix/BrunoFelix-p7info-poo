
x = 0
car = "-"
while True:
    print("Frase:")
    frase = input().split()
    tamanho = []
    if frase == ['0']:
        break
    for i in frase:
        tamanho.append(str(len(i)))
        if len(i) >= x:
            x = len(i)
            maiorPalavra = i
    print(car.join(tamanho))

print()
print("A maior palavra é: %s" % maiorPalavra)

