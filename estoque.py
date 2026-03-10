# ======================== CONTROLE DE ESTOQUE ========================
# Lista para armazenar todos os produtos cadastrados no sistema
meu_estoque = []

def calcular_valor(qntd, valor):
    return qntd * valor

def cadastrar_produto():
    print("\n" + "="*20 + " CADASTRO DE PRODUTO " + "="*20)
    
    nome = input("Nome do produto: ").strip().capitalize()
    
    try:
        qntd = int(input(f"Quantidade de {nome}: "))
        valor = float(input(f"Preço unitário: "))
        
        # Criando o dicionário do produto
        produto = {
            "nome": nome, 
            "qntd": qntd, 
            "valor": valor,
            "total_item": calcular_valor(qntd, valor)
        }
        return produto
    except ValueError:
        print("Erro nos valores! Tente cadastrar este item de novo.")
        return None

def exibir_resumo():
    print("\n" + "="*25 + " RESUMO GERAL " + "="*25)
    valor_geral = 0
    
    for item in meu_estoque:
        print(f"-> {item['nome']}: {item['qntd']} un | R$ {item['valor']:.2f} (Total: R$ {item['total_item']:.2f})")
        valor_geral += item['total_item']
    
    print("-" * 64)
    print(f"VALOR TOTAL DO ESTOQUE: R$ {valor_geral:.2f}")
    print("=" * 64)

# ======================== FLUXO PRINCIPAL ========================
print("Bem-vindo ao Controle de Estoque!")

while True:
    novo_item = cadastrar_produto()
    
    if novo_item:
        meu_estoque.append(novo_item)
        print(f"Sucesso: {novo_item['nome']} adicionado ao sistema.")

    resp = input("\nDeseja cadastrar mais algum produto? (s/n): ").lower()
    
    if resp != 's':
        break

# Verifica se a lista tem itens antes de mostrar o resumo
if len(meu_estoque) > 0:
    exibir_resumo()
else:
    print("\nNenhum produto cadastrado. Encerrando o programa.")

print("\nObrigado por usar o sistema!")
    
    




