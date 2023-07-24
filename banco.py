menu = """

  [d] Depositar
  [s] Sacar
  [e] Extrato
  [q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == 'd':
        
        valor = float(input('Valor do depósito:'))
        
        if valor > 0:
            saldo += valor
            extrato += f"\nDepósito: {str(valor)}"
        else:
            print('Operação falhou! O valor informado é inválido.')

    elif opcao == 's':

        valor = float(input('Valor do depósito:'))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print('Operação falhou! Sem saldo suficiente.')
        elif excedeu_limite:
            print('Operação falhou! O valor do saque excedeu o limite.')
        elif excedeu_saques:
            print('Operação falhou! Você excedeu o limite de saques.')
        elif valor > 0:
            saldo -= valor
            extrato += f"\nSaque: {str(valor)}"
            numero_saques += 1
        else:
            print('Operação falhou! O valor informado é inválido.')


    elif opcao == 'e':
        print("\n---------------------------------- EXTRATO ----------------------------------")
        print("\nNão foram realizadas movimentações. " if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n-----------------------------------------------------------------------------")

    elif opcao == 'q':
        break

    else:
        print('Operação inválida!')
