def realizar_operacoes(saldo, limite, extrato, numero_saques, LIMITE_SAQUES, banco):
    while True:
        menu2 = """
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """
        opcao = input(menu2)

        if opcao == "1":
            print("\nDepósito Selecionado")
            valor = float(input("\nInforme o valor do depósito: "))

            if valor > 0:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"
            else:
                print("\nOperação falhou! O valor informado é inválido.")

        elif opcao == "2":
            print("\nSaque Selecionado")
            valor = float(input("Informe o valor do saque: "))
            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite
            excedeu_saques = numero_saques >= LIMITE_SAQUES

            if excedeu_saldo:
                print("\nOperação falhou! Você não tem saldo suficiente.")
            elif excedeu_limite:
                print("\nOperação falhou! O valor do saque excede o limite.")
            elif excedeu_saques:
                print("\nOperação falhou! Número máximo de saques excedido.")
            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
            else:
                print("\nOperação falhou! O valor informado é inválido!")

        elif opcao == "3":
            print(f"\nExtrato do {banco}")
            print("\n========= EXTRATO BANCÁRIO ============")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("=======================================")

        elif opcao == "0":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

print("\n*** BEM VINDOS AO SISTEMA BANCÁRIO JK-DIO ***")
nome = input("\nQual o Seu nome? ")
print(f"\nBem vindo {nome}! Escolha o seu banco")

menu1 = """
[1] Banco do Brasil
[2] Santander
[3] Itaú
[4] Nubank
[0] Sair

=> """

while True:
    opcao = input(menu1)
    if opcao in ["1", "2", "3", "4"]:
        banco = ['Banco do Brasil', 'Santander', 'Itaú', 'Nubank'][int(opcao) - 1]
        print(f"\nBanco {banco} Selecionado")
        
        
        saldo = 0
        limite = 500
        extrato = ""
        numero_saques = 0
        LIMITE_SAQUES = 3
        
        
        realizar_operacoes(saldo, limite, extrato, numero_saques, LIMITE_SAQUES, banco)
        
    elif opcao == "0":
        print("Saindo do sistema. Até logo!")
        break  
    else:
        print("\nOperação inválida, por favor selecione novamente um dos bancos da lista.")
