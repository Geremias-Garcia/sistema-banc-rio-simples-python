menu = """
    
    Selecione a opção desejada:
    [1]Depositar
    [2]Sacar
    [3]Extrato
    [0]Sair

"""

saldo = 0
valor_limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3


def depositar(deposito):
    global saldo
    if deposito > 0:
        saldo += deposito
        extrato.append(f"+{deposito:.2f}")
        print("Deposito realizado.")
    else:
        print("Valor inválido.")


def sacar(saque):
    global saldo
    global numero_saques
    global extrato

    if numero_saques < LIMITE_SAQUES:
        if 0 < saque <= 500 and saque <= saldo:
            saldo -= saque
            numero_saques += 1
            extrato.append(f"-{saque:.2f}")
            print("Saque realizado.")
        elif saque > 500:
            print("Valor excede o limite permitido por saque.")
        elif saque > saldo:
            print("Valor de saque solicitado é maior que o saldo disponível")
        else:
            print("Valor inválido")

    else:
        print("Limite de saques diários esgotado.")


def mostrar_extrato():
    print("\n########### Extrato ###########")
    print("-------------------------------\n")
    if not extrato:
        print("Nenhuma transação efetuada")
    else:
        for transacao in extrato:
            print(transacao)
    print("\n-------------------------------")
    print(f"Saldo atual: {saldo:.2f}")
    print(f"Número de saques realizados: {numero_saques}")
    print("###############################")


while True:
    opcao = input(menu)

    if opcao == "1":
        deposito = float(input("insira o valor do depósito: "))
        depositar(deposito)

    elif opcao == "2":
        saque = float(input("Informe o valor do saque: "))
        sacar(saque)

    elif opcao == "3":
        mostrar_extrato()

    if opcao == "0":
        break
