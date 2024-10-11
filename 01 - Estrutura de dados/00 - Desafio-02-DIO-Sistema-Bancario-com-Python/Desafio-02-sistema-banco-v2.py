from datetime import datetime

LIMITE_TRANSACOES = 10  # Limite total de operações
AGENCIA = "0001"         # Agência fixa

# Funções para operações bancárias

def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        extrato += f"Depósito:\tR$ {valor:.2f} em {data_hora}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite):
    if valor > saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
    elif valor > limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
    elif valor > 0:
        saldo -= valor
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        extrato += f"Saque:\t\tR$ {valor:.2f} em {data_hora}\n"
        print("\n=== Saque realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato

def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")

# Funções para gerenciamento de usuários e contas

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    if any(usuario['cpf'] == cpf for usuario in usuarios):
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("=== Usuário criado com sucesso! ===")

def criar_conta(usuarios, contas):
    cpf = input("Informe o CPF do usuário: ")
    usuario = next((u for u in usuarios if u['cpf'] == cpf), None)
    
    if usuario:
        numero_conta = len(contas) + 1
        conta = {"agencia": AGENCIA, "numero_conta": numero_conta, "usuario": usuario}
        contas.append(conta)
        print("\n=== Conta criada com sucesso! ===")
    else:
        print("\n@@@ Usuário não encontrado, verifique o CPF digitado ou crie um usuário primeiro! @@@")

def listar_contas(contas):
    if not contas:
        print("\n@@@ Não há contas criadas ainda! @@@")
        return
    
    for conta in contas:
        print(f"\nAgência:\t{conta['agencia']}")
        print(f"C/C:\t\t{conta['numero_conta']}")
        print(f"Titular:\t{conta['usuario']['nome']}")
        print("=" * 50)

# Função principal

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_transacoes = 0  # Contador total de transações
    usuarios = []
    contas = []

    while True:
        menu = """
        BEM VINDO AO SISTEMA BANCARIO JK-DIO
        
        ================ MENU ================
        [1] Depositar
        [2] Sacar
        [3] Extrato
        [4] Criar Usuário
        [5] Criar Conta
        [6] Listar Contas
        [0] Sair
        => """
        
        opcao = input(menu)

        # Verifica se atingiu o limite antes de realizar a operação
        if numero_transacoes >= LIMITE_TRANSACOES:
            print("\n@@@ Você atingiu o limite de transações permitidas. Não é possível realizar mais operações. @@@")
            if opcao in ["1", "2"]:  # Impede depósitos ou saques
                continue  # Retorna ao menu sem executar operações

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)
            numero_transacoes += 1  # Incrementa o contador
        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite)
            numero_transacoes += 1  # Incrementa o contador
        elif opcao == "3":
            exibir_extrato(saldo, extrato)
        elif opcao == "4":
            criar_usuario(usuarios)
        elif opcao == "5":
            criar_conta(usuarios, contas)
        elif opcao == "6":
            listar_contas(contas)
        elif opcao == "0":
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()
