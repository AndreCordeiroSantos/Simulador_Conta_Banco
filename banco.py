# Modelo de Conta de banco.
# Criado por Andre Santos


# Saldo inicial, junto com o número da conta pré definidos.
saldo = 100
conta = '123456'

while True:
    # Mostragem de opções da conta de banco.
    print('ABRIR CONTA [1]')
    print('DEPÓSITO [2]')
    print('SAQUE [3]')
    print('CONSULTAR SALDO [4]')
    print('TRANSFERIR [5]')
    print('SAIR [6]')
    
    # Valor a ser recebido do usuário.
    opcao = input('Escolha uma opção: ')
    
    # Opções escolhidas em andamento
    if opcao == '1':
        print(f'Conta aberta com sucesso!, esse é o número da sua conta {conta}')
     
    # Opção do depósito   
    elif opcao == '2':
        valor = float(input('Digite o valor a ser depositado: '))
        saldo += valor
        print(f'Deposito de R${valor} realizado com sucesso.')
    
    # Opção do saque     
    elif opcao == '3':
        valor = float(input('Digite o valor a ser sacado: ')) 
        if saldo >= valor:
            saldo -= valor
            print(f'Saque de R${valor} realizado com sucesso.')
        else:
            print('Saldo insuficiente para realizar o saque.')
            
    # Opção de consultar saldo       
    elif opcao == '4':
        print(f'Saldo disponível: R${saldo}')
        
    #opção de transferencia de valor
    elif opcao == '5':
        valor = float(input('Digite o valor a ser transferido:'))
        
        if saldo >= valor:
            conta_destino = input('Digite o número da conta de destino: ')
            print(f'Transferencia de R${valor} para a conta {conta_destino}')
            saldo -= valor
        else:
            print('Saldo insuficiente para realizar a transferencia.')
    
    #opção para sair do programa
    elif opcao == '6':
        print('Saindo')
        break
    else:
        print('Opção inválida. Porfavor, escolha uma opção válida.')
        
# Mostragem de encerramento do programa
print("Encerramento do programa.")