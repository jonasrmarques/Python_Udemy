def banco():
    
    def criar_conta(**kwargs):
        informacoes = {
            "nome": kwargs.get("nome"),
            "saldo": kwargs.get("saldo"),
        }
        
        return informacoes
    info = criar_conta(nome="Jonas", saldo=1000)
    

    def saudacao(infos):
        print(f"Olá {infos["nome"]}, seja bem-vindo(a) ao seu banco nem um pouco seguro!")
        
    def selecao_de_operacao(infos):
        
        while True:
            selecao = input(f"Você deseja fazer qual operação?\n 1-|Criar Conta \n2-|SACAR| \n 3-|DEPOSITAR| \n 4-|VERIFICAR SALDO| \n 5-|SAIR DO BANCO| \n Digite aqui: ").lower()
            
            if "1" in selecao or "criar" in selecao or "criar conta" in selecao:
                nome = input("Qual o seu nome para criarmos sua conta? ")
                deposito = float(input("Quanto você deseja depositar?"))
                return criar_conta(nome = nome, saldo = deposito)
            
            elif "2" in selecao or "sacar" in selecao:
                saque = float(input("Quanto você deseja sacar? "))
                if saque > infos["saldo"]:
                    print("Saldo insuficiente")
                elif saque <= infos["saldo"]:
                    print("Saque realizado")
                    
            elif "3" in selecao or "deposito" in selecao or "depositar" in selecao:
                depositar = float(input("Quanto você deseja depositar? "))
                infos["saldo"] += depositar
                print(infos["saldo"])
            
            elif "4" in selecao or "ver" in selecao or "verificar" in selecao or "verificar saldo" in selecao:
                print("Seu saldo atual é:")
                print(infos["saldo"])
            elif "5" in selecao or "sair" in selecao:
                print("Saindo do banco, você pode voltar sempre", infos["nome"])
                break



    
    
    def chamada_das_funcoes():
        saudacao(info)
        selecao_de_operacao(info)
    chamada_das_funcoes()

banco()