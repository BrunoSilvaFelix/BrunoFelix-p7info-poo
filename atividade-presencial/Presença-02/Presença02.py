def printDecimal(num):
    return num

def printOctal(num):
    return oct(num)

def printHexadecimal(num):
    return hex(num)

def printBinario(num):
    return bin(num)

def imprimirTabela():
    print("{:^14}{:^14}{:^30}{:^13}".format("Decimal","Octal","Hexadecimal","Binario"))
    print("-------------\t---------\t---------------------\t-----------------")
    for cont in range(0, 255+1):
        print("{:^14}{:^14}{:^30}{:^13}".format(printDecimal(cont),printOctal(cont),printHexadecimal(cont),printBinario(cont)))
        
print(imprimirTabela())



