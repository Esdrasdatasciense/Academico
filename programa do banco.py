
    

depositar = 1
x = 0
sacar = 2
saldo = 3
sair = 4
caixa = 400
print('=' * 15)
print("""depositar = 1
sacar     = 2
saldo     = 3
sair      = 4
saldo     = 400""")
print('=' * 15)
z = 0

while z != 4:
    x = int(input('Qual operação deseja? '))
    if x == 2:
        y = int(input('Quanto deseja sacar?: '))
        if (y > caixa):
            print ('Saldo insuficiente')
            a = str(input('Quer continuar? '))
            if a == 'sim':
                z = 2
            elif a == 'nao':
                z = 4
                print('Saldo final: ',caixa)

        else:
            print ('Saque concluído')
            caixa = (caixa - y)
            print('Saldo final: ',caixa)
            a = str(input('Quer continuar? '))
            if a == 'sim':
                z = 2
            elif a == 'nao':
                z = 4
                
    elif x == 3:
        print('o saldo é: ',caixa)
        a = str(input('Quer continuar? '))
        if a == 'sim':
            z = 2
        elif a == 'nao':
            z = 4
    elif x == 1:
        l = int(input('Quanto deseja depositar? '))
        caixa += l
        print('Saldo final: ',caixa)
        a = str(input('Quer continuar? '))
        if a == 'sim':
            z = 2
        elif a == 'nao':
            z = 4
    elif x == 4:
        z = 4
print('Obrigado por usar o banco')

        
