import textwrap


def menu():
    menu = """
    ╔═════════════════════════════════════╗
    ║                                     ║
    ║       Sistema Bancário - Menu       ║
    ║      ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯      ║
    ║  [1] Depositar   [4] Novo Usuário   ║
    ║  [2] Sacar       [5] Nova Conta     ║
    ║  [3] Extrato     [6] Lista Contas   ║
    ║                                     ║
    ║  [0] Sair                           ║
    ║                                     ║
    ╚═════════════════════════════════════╝
    
    => """
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):
    
    if valor > 0:
        saldo += valor
        extrato += f"\n   Depósito:\tR$ {valor:.2f}\n"
        print("\n\n Valor depositado!")
        print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")

    else:
        print("\n\n Operação falhou! O valor informado é inválido.")
        print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n\n Operação falhou! Você não tem saldo suficiente.")
        print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")

    elif excedeu_limite:
        print("\n\n Operação falhou! Você não tem limite suficiente.")
        print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")

    elif excedeu_saques:
        print("\n\n Operação falhou! Número de saques excedido.")
        print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")

    elif valor > 0:
        saldo -= valor
        extrato += f"\n   Saque:\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n\n Valor sacado!")
        print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")

    else:
        print("\n\n Operação falhou! O valor informado  é inválido.")
        print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")

    return saldo, extrato, numero_saques


def exibir_extrato(saldo, /, *, extrato):
    
    print("\n╔═══════════════ EXTRATO ════════════════╗")
    print("╨                                        ╨")
    print("\n   Não foram realizadas movimentações." if not extrato else extrato)
    print("  --------------------------------------  ")
    print(f"   Saldo:\tR$ {saldo:.2f}")
    print("  --------------------------------------  ")
    print("\n╥                                        ╥")
    print("╚═══════════════ EXTRATO ════════════════╝")


def criar_usuario(usuarios):
    
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n\n Já existe usuário com esse CPF!")
        print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, número - bairro - cidade/sigla estado): ")
    
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("\n\n Usuário criado com sucesso!")
    print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n\n Conta criada com sucesso!")
        print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print(" Usuário não encontrado, fluxo de criação de conta encerrado!")
    print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")


def listar_contas(contas):
    for conta in contas:
        linha = f"""
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("==================================================")
        print(textwrap.dedent(linha))

def main():

    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:

        opcao = menu()

        if opcao == "1": # DEPOSITAR
            
            valor = float(input("Digite o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)


        elif opcao == "2": # SACAR
            
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )


        elif opcao == "3": # EXTRATO

            exibir_extrato(saldo, extrato=extrato)


        elif opcao == "4": # NOVO USUÁRIO
            criar_usuario(usuarios)


        elif opcao == "5": # NOVA CONTA
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)


        elif opcao == "6": # LISTAR CONTAS
            listar_contas(contas)


        elif opcao == "0": # SAIR
            break


        else:
            print("\n\n Operação inválida, por favor selecione novamente a operação desejada.")
            print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")


main()