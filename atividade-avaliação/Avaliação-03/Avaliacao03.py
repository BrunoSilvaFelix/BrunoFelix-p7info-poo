def primo(p):
    contador = 0
    for i in range(1,p+1):
        if p%i==0:
            contador = contador+1
    if  contador==2:
        return True
    else:
        return False
  
def somaPrimo(n):
    soma = 0 
    contador = 0
    for i in range(1,n+1):
        if primo(i) == True:
            soma = soma + i
            contador = contador+1
        if contador == n:
            break
    return soma    

num = input()

print(somaPrimo(num))            