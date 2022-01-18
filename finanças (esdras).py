c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0

y = 1
x = 1
s = 0

x1 = 1
y1 = 1
s1 = 0

while (x != 0):
    c1 = int(input("Digite o saldo {}: " .format(y)))
    s = str(input("Tem mais dinheiro?: "))
    c2 = c2 + c1
    if (s == 'n'):
        x = x - 1
    elif (s == 's'):
        y = y + 1
    else:
        print("Erro")
        x = x - 1
        
        
while (x1 != 0):
    c3 = int(input("Digite a divida {}: " .format(y1)))
    s1 = str(input("Tem mais divida?: "))
    c4 = c4 + c3
    if (s1 == 'n'):
        x1 = x1 - 1
    elif (s1 == 's'):
        y1 = y1 + 1
    else:
        print("Erro")
        x1 = x1 - 1
        
c5 = c2 - c4
print("O valor restante é: ", c5)
encerramento = str(input("Digite qualquer tecla p/ encerrar: "))
        

        
        
    	
