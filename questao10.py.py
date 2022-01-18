num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
contador = 0
for i in range (num1+1,num2):
    if (i %4==0):
        contador += 1
for i in range (num2-1,num1):
    if (i %4==0):
        contador += 1
print("A quantidade de múltiplos de %d e %d é igual a %d múltiplos" %(num1, num2, contador))
