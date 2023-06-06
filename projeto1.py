menu = """
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [0] Sair
=> """

saldo = 0
extrato = ''
numero_saques = 0
LIMITE_SAQUE = 500
QUANTIDADE_SAQUE_DIARIO = 3

while True: 

    opcao = input(menu)

    if opcao == '1':
        valor = float(input('Informe qual valor será depositado: '))

        if valor > 0: 
            saldo += valor 
            extrato = f'Depósito: R$ {valor:.2f}\n'

        else: 
            print('Operação Falhou! O valor informado é inválido.\n')

    elif opcao == '2':
        valor = float(input('Informe o valor do saque: '))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > LIMITE_SAQUE

        excedeu_saques = numero_saques > QUANTIDADE_SAQUE_DIARIO

        if excedeu_saldo:
            print('Operação Falhou! Você não tem saldo suficiente.\n')
        
        elif excedeu_limite: 
            print('Operação Falhou! O valor do saque excede o limite.\n')

        elif excedeu_saques: 
            print('Operação Falhou! Número máximo de saques excedido.\n')

        elif valor > 0:
            saldo -= valor 
            extrato = f'Saque: R$ {valor:.2f}\n'
            numero_saques += 1
        
        else: 
             print('Operação Falhou! O valor informado é inválido.\n')

    elif opcao == '3':
        print('\n========= EXTRATO =========')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print('=============================')

    elif opcao == '0': 
        break

    else:
        print('Operação inválida! Por favor selecione novemente a operação desejada.\n')