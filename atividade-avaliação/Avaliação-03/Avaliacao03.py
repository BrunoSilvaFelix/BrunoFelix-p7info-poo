def primo(p):
    contador = 0
    for i in range(1,p+1):
        if p%i==0:
            contador = contador+1
    if  contador==2:
        return True
    else:
        return False

def somaPrimos(n): #n = 3
    contador = 0
    num = 2
    soma = 0
    primos = []
    while True:
        if primo(num):
            contador = contador + 1
            soma = soma + num
            primos.append(num)
        num = num + 1
        if contador == n:
            break
    return (soma,primos)


print("Informe um número inteiro não negativo:")
num = input()
soma, parcela = somaPrimos(int(num))
if int(num) >= 0:
    print("Para n = {0}, resultado {s} = {p}. ".format(int(num),s = soma,p = parcela))