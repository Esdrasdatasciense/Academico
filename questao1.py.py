
num = int(input("Digite um valor (-1 para sair): ") )
soma = 0
maior = 0
menor = 0
while (num != -1):
    soma = soma + num
    num = int( input("Digite um valor (-1 para sair): ") )
    if (num > maior):
        maior = num
    if (num < menor):
        menor = num and menor != -1
print("\n*** acabou o programa *** \n O maior número digitado foi: %d \n O menor valor digitado foi: %d \n Soma dos números digitados: %d" %(maior, menor, soma))
