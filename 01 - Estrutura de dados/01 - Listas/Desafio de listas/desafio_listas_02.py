import sys

def produto_mais_vendido(produtos):
    contagem = {}
    
    # Contagem da frequência de cada produto
    for produto in produtos:
        if produto in contagem:
            contagem[produto] += 1
        else:
            contagem[produto] = 1
    
    max_produto = None
    max_count = 0
    
    # Encontrar o produto com a maior contagem
    for produto, count in contagem.items():
        if count > max_count:
            max_count = count
            max_produto = produto
    
    return max_produto

def obter_entrada_produtos():
    print("Digite a lista de produtos vendidos, separados por vírgula:")
    entrada = sys.stdin.readline().strip()
    produtos = [produto.strip() for produto in entrada.split(',')]
    return produtos
produtos = obter_entrada_produtos()
print(produto_mais_vendido(produtos))