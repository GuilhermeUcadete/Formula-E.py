def forca_opcao(msg, conjunto_opcoes, msg_erro='Inválido'):
    # Solicita ao usuário que escolha uma opção válida de um conjunto
    opcoes = '\n'.join(conjunto_opcoes)  # Formata as opções em uma string
    escolha = input(f"{msg}\n{opcoes}\n-> ")  # Solicita a entrada do usuário
    while escolha not in conjunto_opcoes:  # Verifica se a escolha é válida
        print(msg_erro)  # Mensagem de erro para escolha inválida
        escolha = input(f"{msg}\n{opcoes}\n-> ")  # Solicita novamente a entrada
    return escolha  # Retorna a escolha válida


def checa_numero(msg, msg_erro='Inválido'):
    # Solicita um número ao usuário e verifica se a entrada é válida
    num = input(msg)  # Solicita a entrada do usuário
    while not num.isnumeric():  # Enquanto a entrada não for um número
        print(msg_erro)  # Mensagem de erro para entrada inválida
        num = input(msg)  # Solicita novamente a entrada
    return int(num)  # Retorna o número como inteiro


# Dicionário que contém os produtos, seus preços e estoque disponível
produtos = {
    'Boné': {'preco': 25.00, 'estoque': 10},
    'Chaveiro': {'preco': 10.00, 'estoque': 20},
    'Camisa': {'preco': 50.00, 'estoque': 5},
    'Adesivo': {'preco': 5.00, 'estoque': 50},
    'Carrinho de brinquedo': {'preco': 20.00, 'estoque': 15}
}

carrinho = []  # Inicializa uma lista vazia para o carrinho de compras


def mostrar_produtos():
    # Exibe os produtos disponíveis, seus preços e estoques
    print("Produtos disponíveis:")
    for produto, info in produtos.items():  # Itera sobre os produtos
        print(f"{produto}: R${info['preco']:.2f} (Estoque: {info['estoque']})")  # Exibe produto, preço e estoque


def adicionar_ao_carrinho(produto, quantidade):
    # Adiciona um produto ao carrinho, se a quantidade for válida
    if produto in produtos:  # Verifica se o produto existe
        if quantidade <= produtos[produto]['estoque']:  # Verifica se a quantidade solicitada está disponível
            carrinho.append((produto, quantidade))  # Adiciona o produto e a quantidade ao carrinho
            produtos[produto]['estoque'] -= quantidade  # Reduz o estoque do produto
            print(f"Você comprou {quantidade} {produto}(s) e foram adicionados ao carrinho.")
        else:
            print(f"Quantidade excede o estoque disponível ({produtos[produto]['estoque']}). Tente novamente.")  # Mensagem de erro se o estoque for insuficiente
    else:
        print("Produto não encontrado.")  # Mensagem de erro se o produto não existir


def calcular_total():
    # Calcula o total da compra somando o preço dos produtos no carrinho
    total = sum(produtos[produto]['preco'] * quantidade for produto, quantidade in carrinho)  # Soma os preços
    return total  # Retorna o total


def coletar_endereco():
    # Coleta o endereço do usuário para a entrega
    print("\nPor favor, insira o seu endereço para entrega:")
    rua = input("Rua: ")
    numero = input("Número: ")
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    estado = input("Estado: ")
    cep = input("CEP: ")

    # Formata o endereço completo
    endereco = f"{rua}, {numero} - {bairro}, {cidade} - {estado}, CEP: {cep}"
    return endereco  # Retorna o endereço completo


def finalizar_compra(endereco):
    # Finaliza a compra e exibe os produtos do carrinho e o total a pagar
    total = calcular_total()  # Calcula o total
    print("\nCarrinho de Compras:")
    for produto, quantidade in carrinho:  # Itera sobre os produtos no carrinho
        print(f"{quantidade} x {produto}")  # Exibe cada produto e sua quantidade
    print(f"Total a pagar: R${total:.2f}")  # Exibe o total a pagar
    print(f"Endereço de entrega: {endereco}")  # Exibe o endereço de entrega
    carrinho.clear()  # Limpa o carrinho após a compra


# Opções disponíveis para o usuário
opcoes_info = ['Sobre a Tech Mahindra', 'Sobre a Formula-E', 'Sobre os pilotos', 'Mercadinho', 'Sair']
pilotos = ['Pedro Alcantra', 'Henrique Burguer', 'Mateus Kovith', 'Guilherme Olaku', 'Voltar']

usuario = input('Bem-vindo à Tech Mahindra! Qual o seu nome?\n-> ')  # Solicita o nome do usuário
while True:
    opcao = forca_opcao('Digite a opção que você deseja saber mais:', opcoes_info, 'Digite uma opção válida')  # Solicita a opção ao usuário

    if opcao == opcoes_info[0]:
        # Informação sobre a Tech Mahindra
        print(
            'A Tech Mahindra é uma empresa indiana de tecnologia da informação e consultoria...')
        print('Voltando para as opções...')
        continue  # Retorna ao menu principal

    elif opcao == opcoes_info[1]:
        # Informação sobre a Fórmula E
        print(
            'A Fórmula E é uma categoria de automobilismo de monolugares elétricos...')
        print('Voltando para as opções...')
        continue  # Retorna ao menu principal

    elif opcao == opcoes_info[2]:
        while True:  # Loop para selecionar pilotos
            biografia = forca_opcao('Qual dos nossos pilotos você deseja conhecer?', pilotos, 'Digite um piloto válido')  # Solicita o piloto
            if biografia == pilotos[0]:
                # Informação sobre Pedro Alcântara
                print('Pedro Alcântara é um piloto brasileiro de Fórmula E...')
                print('Voltando para as opções...')

            elif biografia == pilotos[1]:
                # Informação sobre Henrique Burguer
                print('Henrique Burguer é um piloto brasileiro de automobilismo...')
                print('Voltando para as opções...')

            elif biografia == pilotos[2]:
                # Informação sobre Mateus Kovith
                print('Mateus Kovith, nascido em 1996 em Belo Horizonte...')
                print('Voltando para as opções...')

            elif biografia == pilotos[3]:
                # Informação sobre Guilherme Olaku
                print('Guilherme Olaku, nascido em 1998 em Minas Gerais...')
                print('Voltando para as opções...')

            elif biografia == pilotos[4]:
                print('Voltando para as opções...')  # Voltar para as opções de pilotos
                break  # Sai do loop de seleção de pilotos

    elif opcao == opcoes_info[3]:
        print('Bem-vindo ao Mercadinho da Fórmula E!')  # Início do mercadinho
        while True:
            mostrar_produtos()  # Mostra os produtos disponíveis
            escolha = input("\nDigite o nome do produto para adicionar ao carrinho (ou 'sair' para finalizar): ")  # Solicita o produto
            if escolha.lower() == 'sair':
                break  # Sai do loop se o usuário digitar 'sair'
            if escolha in produtos:  # Verifica se o produto existe
                quantidade = checa_numero("Digite a quantidade que deseja adicionar: ", "Quantidade inválida")  # Solicita a quantidade
                adicionar_ao_carrinho(escolha, quantidade)  # Adiciona o produto ao carrinho
            else:
                print("Produto não encontrado.")  # Mensagem de erro se o produto não existir

        # Coleta o endereço antes de finalizar a compra
        endereco = coletar_endereco()  # Coleta o endereço
        finalizar_compra(endereco)  # Finaliza a compra
        print(f'Obrigado por comprar em nossa loja! Volte sempre {usuario}')  # Mensagem de agradecimento
        break  # Sai do loop principal

    elif opcao == opcoes_info[4]:
        print(f'Obrigado por visitar nosso site! Volte sempre {usuario}')  # Mensagem de despedida
        break  # Sai do loop principal
