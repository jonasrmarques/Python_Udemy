def exibir_detalhes_do_pedido(**kwargs):
    """
    Essa função irá receber nosso dicionário de produtos,
    nele o usuário colocará os detalhes do produto que deseja comprar
    """
    pedidos = {
        "item": kwargs.get("item"),
        "preco": kwargs.get("preco", 0.0),
        "qtd": kwargs.get("qtd", 1)
    }
    
    return pedidos



###############################################################################################

def calcular_preco_total(qualquernome):
    """
    Essa função irá fazer o cálculo do pedido do cliente, multiplicando o preço,
    pela quantidade e armazenando esse cálculo em preco total
    """
    teste = input("Digite seu cupom")
    cupom = "nome123"
    preco_total = qualquernome['preco'] * qualquernome['qtd']
    if teste == cupom:
        return preco_total / 2
    else:
        preco_total * 2


#################################################################################################



def enviar_confirmacao(pedidos, preco_total):
    """
    Essa é a nossa função de saída, após rodar as outras duas funções, 
    essa mostrará a quantidade e o produto que foi selecionado, 
    juntamente com o preço que foi calculado na função acima
    """
    
    print(f"Confirmação enviada para {pedidos['qtd']} {pedidos['item']}(s)\n")
    print(f"O valor total a ser pago vai ser: R${preco_total}\n")
    
##################################################################################################

    
    
def processar_pedido(detalhes):
    """
    Essa é a função principal, que irá receber os dados e irá fazer a chamada das outras funções passando todos os valores, essa função tem como parâmetro detalhes, que irá receber os dados da primeira função, dados esses que serão: o ítem, preco e a quantidade.
    
    Após receber esses detalhes, os mesmos serão passados para calcular_preco_total, para os calculos serem realizados e armazenado na variável preco_total.
    
    Após o calculo ser realizado, mais uma vez, é passado os detalhes com o acrescimo do preco_total que foi calculado na função acima e armazenado na variável, nisso, será passado para função enviar_confirmação esses valores e com esses valores teremos a saída que será impressa no terminal com os dois prints que foram colocados na função acima.
    """
    
    preco_total = calcular_preco_total(detalhes)
    enviar_confirmacao(detalhes, preco_total)




##################################################################################################################################################################







#Aqui inicializamos o laço diretamente, ele obrigatoriamente irá ser inicializado pelo fato de já ter passado o True
while True:
    print("Seja bem-vindo(a) ao seu mercado virtual!\n")
    
    #Nós colocamos dentro dessa variável um input, que será responsável por controlar o loop
    comecar = input("Você deseja comprar alguma coisa? [S]im ou [N]ão ").lower()
    #Caso o usuário digite qualquer coisa que contenha "s", ele entrará dentro da condicional, caso não tenha nenhum "s" ele cairá no else e sairá do laço
    if "s" in comecar:
        """
        Aqui nós startamos 3 variáveis que irão receber o item, preço e quantidade, o preço e a quantidade serão convertidos dentro do try.
        """
        item = input("Qual ítem você deseja comprar? \n")
        preco = input("Qual o preço do produto? \n").replace(",", ".")
        qtd = input(f"Digite quantos(as) {item} você deseja levar \n")
        
        try:
            preco_convertido = float(preco)
            qtd_convertida = int(qtd)
        except:
            print("Por favor, digite um preço válido")
            
        """
        Após serem convertidos, será passado como argumento da função processar_pedido, os valores da função exibir_detalhes_do_pedido.
        E isso fará a chamada da função, passando todos os valores que foram sendo inicializados acima
        """
        processar_pedido(exibir_detalhes_do_pedido(item=item, preco=preco_convertido, qtd=qtd_convertida))
        

    else:
        print("Você saiu do programa")
        break

