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

    if opcao == "d":
        valor = float(input("Digite o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou. O valor digitado é inválido.")
    elif opcao == "s":
        valor = float(input("Digite o valor do saque: "))

        extrapolou_saldo = valor > saldo

        extrapolou_limite = valor > limite

        extrapolou_num_saques = numero_saques >= LIMITE_SAQUES

        if extrapolou_saldo:
            print("Operação falhou! Você não possui saldo suficiente para realizar a operação.")

        elif extrapolou_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif extrapolou_num_saques:
            print("Operação falhou! Você excedeu o número máximo de saques.")

        elif valor > 0:
            saldo -= valor
            numero_saques += 1
            extrato += f"Saque: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor digitado é inválido.")

    elif opcao == "e":
        print()
        print(" EXTRATO ".center(40,"#"))
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("#"*40)

    elif opcao == "q":
        print("Até mais!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")