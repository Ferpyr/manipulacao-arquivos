def buscar_nome():
    nomes = []
    with open("nomes.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            nomes.append(linha.strip())
    nome = input("Digite o nome: ")
    if nome in nomes:
        print("Nome encontrado :D")
    else:
        print("Nome não encontrado :C")
buscar_nome()
