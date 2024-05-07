



   
   



[new_func1]=  "Depositar"
[new_func2]=  "Sacar"
[new_func3] = "Extrato"
[new_func4] = "Sair"



new_func1 =  "Depositar"
new_func2 =  "Sacar"
new_func3 = "Extrato"
new_func4 = "Sair"

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    menu = f"1 - {new_func1}\n2 - {new_func2}\n3 - {new_func3}\n4 - {new_func4}\n"
    opcao = input(menu)

    if opcao == '1':
        valor = float(input("Digite o valor a ser depositado: "))
        saldo += valor
        extrato.append(('Deposito', valor))
        print("Deposito realizado com sucesso!")

    elif opcao == '2':
        if numero_saques < LIMITE_SAQUES:
            valor = float(input("Digite o valor a ser sacado: "))
            if valor <= (saldo + limite):
                saldo -= valor
                numero_saques += 1
                extrato.append(('Saque', valor))
                print("Saque efetuado com sucesso!")
            else:
                print("Saldo insuficiente.")
        else:
            print("Limite de saques atingido.")

    elif opcao == '3':
        print("Extrato da sua conta bancária:")
        for operacao, valor in extrato:
            print(f"{operacao}: {valor}")
        