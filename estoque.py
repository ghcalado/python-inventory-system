#Programa de Controle de Estoque
# ==============================CADASTRO DE PRODUTO==============================
def cadastrar_produto():
    print("Bem-vindo ao Controle de Estoque!")
    prod = input("Digite o nome do produto: ")
    qntd = int(input("Digite a quantidade em estoque: "))
    valor = float(input("Digite o valor do produto: "))
    print(f"Produto '{prod}' cadastrado com sucesso!")
    return prod, qntd, valor 

def valor_total (qntd, valor):
    total = qntd * valor
    return total

def novo_produto(conf):
    conf== "s"
    return cadastrar_produto()
 
#==============================ATUALIZAÇÃO DE ESTOQUE============================
prod, qntd, valor = cadastrar_produto()
print("="*30 + "ATUALIZAÇÃO DE ESTOQUE" + "="*30)
resposta = input("Você deseja visualizar o estoque? (s/n) ")
if resposta == "s":
    print(f"Quantidade em estoque: {qntd}")
    print(f"Valor do produto: R${valor:.2f}")
    print(f"Valor total do estoque: R${valor_total(qntd, valor):.2f}")
    conf = input("Deseja cadastrar um novo produto? (s/n) ")
    if conf == "s":
        novo_produto(conf)
else:
    print("Obrigado por usar o Controle de Estoque!")
    
    




