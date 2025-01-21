def criar_conta(**kwargs):
    dados = {
        "nome": kwargs.get("nome"),
        "saldo": kwargs.get("saldo")
    }
    return dados

conta = None

def sacar(infos, saque):
    if infos["saldo"] < saque:
        print("Valor insuficiente")
    else:
        print("Saque realizado com sucesso")
        infos["saldo"] -= saque
        
def depositar(infos, deposito):
    print("Deposito realizado com sucesso")
    infos["saldo"] += deposito

def exibir_saldo_total(infos):
    print(f"O seu saldo é: {infos["saldo"]}")
         
def banco():  
    while True:        
        selecao = input(f"Você deseja fazer qual operação?\n 1-|Criar Conta \n2-|SACAR| \n 3-|DEPOSITAR| \n 4-|VERIFICAR SALDO| \n 5-|SAIR DO BANCO| \n Digite aqui: ").lower()
        if "1" in selecao or "criar" in selecao or "criar conta" in selecao:
            print("Seja bem vindo(a) a criação de conta!")
            nome = input("Por favor, digite o seu nome: ")
            saldo = float(input("Por favor, digite o quão você deseja colocar como depósito"))
            conta = criar_conta(nome = nome, saldo = saldo)
        elif "2" in selecao or "sacar" in selecao:
            saque = float(input("Quanto você deseja sacar? "))
            sacar(conta, saque)
        elif "3" in selecao or "depositar" in selecao:
            deposito = float(input("Quanto você deseja depositar? "))
            depositar(conta, deposito)
        elif "4" in selecao or "exibir" in selecao:
            exibir_saldo_total(conta)
        
        elif "5" in selecao or "sair" in selecao:
            print("Saindo do banco, não volte nunca mais")
            break
banco()