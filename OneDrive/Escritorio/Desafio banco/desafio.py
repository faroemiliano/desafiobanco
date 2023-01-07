menu = '''

[d] Deposito
[s] Saque
[e] Extrato 
[q] Sair

==>'''
saldo = 0
limite = 500
extrato = ''
numero_saque = 0
SAQUE_LIMITE = 3


while True:

    opcao = input (menu)
    
    if opcao == 'd':
        valor = float (input('informe o valor do deposito'))
        
        if valor > 0:
            saldo += valor
            extrato += f'Deposito: R$ {valor:.2f}\n'

        else:
            print ('o valor informado não e correto')  

    elif opcao == 's':
        valor = float (input ('coloque um valor para saque: '))

        excedeu_saldo = valor > limite

        excedeu_limite = valor > saldo

        excedeu_saque = numero_saque >= SAQUE_LIMITE

        if excedeu_saldo:
            print ('operação falhou, so pode fazer saques ate R$ 500')

        elif excedeu_limite:
            print ('operação falhou, o valor do saque excede o limite')

        elif excedeu_saque:
            print ('operação falhou, numero de saques excedido')

        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saque += 1

        else:
            print ('operação falhou, numero informado e invalido')            

    elif opcao == 'e':
        print ('*********EXTRATO*********')

        print ('não foram realizadas movimentações' if not extrato else extrato)

        print (f'saldo: R$ {saldo:.2f}')
        
        print ('*-*-*-*-*-*-*-*-*-*-*-*-*-*')

    elif opcao == 'q':
        break

    else:
        print ('erro ao definir sua opcao')
