continuar = 1 or 2
soma = 0
contador = 0
somaOp = 0
somaIdOp = 0
maior = 0
while (continuar == 1):
    idade = int(input("digite a sua idade: "))
    opinião = int(input( "\n[1] Ruim \n[2] Regular \n[3] Bom \n[4] Excelente \nDigite o número referente a sua opinião: "))
    continuar = int(input("\n [1] Sim \n [2] Não \n quer continuar? "))
    if (opinião == 3):
        soma += idade
        contador +=1
        media = soma/contador
    if (opinião == 1 or opinião == 2):
        somaOp += 1
    if ( idade > 30 and opinião == 4):
        somaIdOp += 1
    if (idade > maior):
        maior = idade
print("\n Média de idade bom: %d \n Quantidade de respostas Ruim/Regular: %d \n Pessoas acima de 30 Excelente: %d \n Maior idade: %d" %(media, somaOp, somaIdOp, maior))
