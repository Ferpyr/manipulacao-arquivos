def gerar_relatorio():
    vendas = []

    with open("vendas.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            vendedor, produto, valor = linha.strip().split(";")
            venda = {
                "vendedor": vendedor,
                "produto": produto,
                "valor": float(valor)
            }
            vendas.append(venda)
    print("Vendas:")
    valor_total = 0
    qtde_vendas = {}

    for venda in vendas:
        print(f"{venda['vendedor']} - {venda['produto']} - R$ {venda['valor']:.2f}")
        valor_total = valor_total + venda["valor"]
        if venda["vendedor"] in qtde_vendas:
            qtde_vendas[venda["vendedor"]] = qtde_vendas[venda["vendedor"]] + 1
        else:
            qtde_vendas[venda["vendedor"]] = 1

    print(f"Total vendas: R$ {valor_total:.2f}")
    print("Quantidade de vendas:")

    for vendedor in qtde_vendas:
        print(f"{vendedor}: {qtde_vendas[vendedor]}")
    vendedor_maior = max(qtde_vendas, key=qtde_vendas.get)
    maior_quantidade = max(qtde_vendas.values())

    for vendedor in qtde_vendas:
        if qtde_vendas[vendedor] == maior_quantidade:
            print(f"Vendedor com mais vendas: {vendedor}")
            print(f"Quantidade: {maior_quantidade}")

gerar_relatorio()
