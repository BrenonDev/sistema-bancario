menu = """
╔═══════════════════════════════╗
║                               ║
║    Sistema Bancário - Menu    ║
║   ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯   ║
║  [1] Depositar                ║
║  [2] Sacar                    ║
║  [3] Extrato                  ║
║  [0] Sair                     ║
║                               ║
╚═══════════════════════════════╝

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1": # DEPOSITAR
        valor = float(input("Digite o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"\n   Depósito: R$ {valor:.2f}\n"
            print("\n Valor depositado!")
            print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
        else:
            print("\n Operação falhou! O valor informado é inválido.")
            print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")


    elif opcao == "2": # SACAR
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("\n Operação falhou! Você não tem saldo suficiente.")
            print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")

        elif excedeu_limite:
            print("\n Operação falhou! Você não tem limite suficiente.")
            print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")

        elif excedeu_saques:
            print("\n Operação falhou! Número de saques excedido.")
            print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")

        elif valor > 0:
            saldo -= valor
            extrato += f"\n   Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("\n Valor sacado!")
            print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")

        else:
            print("\n Operação falhou! O valor informado  é inválido.")
            print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")



    elif opcao == "3": # EXTRATO
        print("\n╔═══════════════ EXTRATO ════════════════╗")
        print("╨                                        ╨")
        print("\n   Não foram realizadas movimentações." if not extrato else extrato)
        print("  --------------------------------------  ")
        print(f"   Saldo: R$ {saldo:.2f}")
        print("  --------------------------------------  ")
        print("\n╥                                        ╥")
        print("╚═══════════════ EXTRATO ════════════════╝")

    elif opcao == "0": # SAIR
        break

    else:
        print("\n Operação inválida, por favor selecione novamente a operação desejada.")
        print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
