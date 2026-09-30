def menu_arquivo():
    while True:
        print("\n1 - Ler arquivo")
        print("2 - Adicionar texto")
        print("3 - Sobrescrever arquivo")
        print("4 - Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            with open("notas.txt", "r", encoding="utf-8") as arquivo:
                conteudo = arquivo.read()
            print(conteudo)

        elif opcao == "2":
            texto = input("Digite o texto: ")
            with open("notas.txt", "a", encoding="utf-8") as arquivo:
                arquivo.write(texto + "\n")

        elif opcao == "3":
            texto = input("Digite o novo texto: ")
            with open("notas.txt", "w", encoding="utf-8") as arquivo:
                arquivo.write(texto + "\n")

        elif opcao == "4":
            print("Encerrado")
            break

        else:
            print("Opção invalida")
menu_arquivo()