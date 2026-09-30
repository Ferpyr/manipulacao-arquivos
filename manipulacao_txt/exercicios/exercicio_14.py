def gerenciar_tarefas():
    tarefas = []
    with open("tarefas.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            tarefas.append(linha.strip())
    while True:
        print("\n1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Remover tarefa")
        print("4 - Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            tarefa = input("Digite a tarefa: ")
            tarefas.append(tarefa)
            with open("tarefas.txt", "w", encoding="utf-8") as arquivo:
                for tarefa in tarefas:
                    arquivo.write(tarefa + "\n")

            print("Tarefa adicionada")

        elif opcao == "2":
            print("\nTarefas:")
            for tarefa in tarefas:
                print(tarefa)

        elif opcao == "3":
            tarefa = input("Qual tarefa quer remover: ")
            if tarefa in tarefas:
                tarefas.remove(tarefa)
                with open("tarefas.txt", "w", encoding="utf-8") as arquivo:
                    for tarefa in tarefas:
                        arquivo.write(tarefa + "\n")
                print("Tarefa removida")

            else:
                print("Tarefa não encontrada")
        elif opcao == "4":
            print("Encerrado")
            break
        else:
            print("Opção invalida")
gerenciar_tarefas()
