limite_valor_por_saque= 500
contador_saques = 0
saldo = 0
depositos_list = []
saques_list = []

resposta = input("Digite se deseja realizar um depósito(d), saque(s), visualizar o extrato(e) ou sair(x): ")

while resposta != "x" or resposta != "X":
    if resposta == "d":
        deposito = float(input("Digite quanto quer depositar: "))
        saldo += deposito
        depositos_list.append(f"Depósito - R${deposito:.2f}")
        
        resposta = input("Digite se deseja realizar um depósito(d), saque(s), visualizar o extrato(e) ou sair(x): ")
        
    elif resposta == "s" or resposta == "S":
        if contador_saques < 3: 
            saque = float(input("Digite quanto quer sacar: "))
            
            if saque <= saldo and contador_saques < 3 and saque <= 500:
                saldo -= saque
                saques_list.append(f"Saque - R${saque:.2f}")
                contador_saques += 1
                
        else:
            print("Reveja se o saque não é maior que o saldo, se não está realizando mais de 3 saques ou se o saque não é maior que 500!")
        
        resposta = input("Digite se deseja realizar um depósito(d), saque(s), visualizar o extrato(e) ou sair(x): ")

    elif resposta == "e" or resposta == "E":
        print("------------- EXTRATO DA CONTA -----------------")
        if len(depositos_list) > 0 or len(saques_list) > 0:
            if len(depositos_list) > 0:
                for depositos in depositos_list:
                    print(depositos)
            
            if len(saques_list) > 0:
                for saques in saques_list:
                    print(saques)

            print(f"Saldo Atual: R${saldo:.2f}")
        else:
            print("Não foram realizadas transações")
        
        resposta = input("Digite se deseja realizar um depósito(d), saque(s), visualizar o extrato(e) ou sair(x): ")