def listar_alunos(alunos):
    print()
    print("Lista de alunos:")
    for aluno in alunos:
        print(f"{aluno['id']} - {aluno['nome']} - {aluno['idade']} anos")

def buscar_aluno(alunos):
    id_busca = int(input("Digite o ID: "))
    for aluno in alunos:
        if aluno["id"] == id_busca:
            print()
            print("Aluno encontrado:")
            print(aluno["nome"])
            print(f"{aluno['idade']} anos")
            print(aluno["curso"])
            return
    print("Aluno não encontrado:C")

def cadastrar_aluno(alunos):
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    curso = input("Curso: ")
    maior_id = 0
    for aluno in alunos:
        if aluno["id"] > maior_id:
            maior_id = aluno["id"]
    novo_id = maior_id + 1
    aluno = {
        "id": novo_id,
        "nome": nome,
        "idade": idade,
        "curso": curso
    }
    alunos.append(aluno)
    with open("alunos2.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{novo_id};{nome};{idade};{curso}\n")
    print("Aluno cadastrado:D")

def remover_aluno(alunos):
    id_remover = int(input("Digite o ID do aluno: "))
    for aluno in alunos:
        if aluno["id"] == id_remover:
            alunos.remove(aluno)
            with open("alunos2.txt", "w", encoding="utf-8") as arquivo:
                for aluno in alunos:
                    arquivo.write(
                        f"{aluno['id']};{aluno['nome']};"
                        f"{aluno['idade']};{aluno['curso']}\n"
                    )
            print("Aluno removido:D")
            return
    print("Aluno não encontrado:C")

def alterar_aluno(alunos):
    id_alterar = int(input("Digite o ID do aluno: "))
    for aluno in alunos:
        if aluno["id"] == id_alterar:
            aluno["nome"] = input("Nome: ")
            aluno["idade"] = int(input("Idade: "))
            aluno["curso"] = input("Curso: ")
            with open("alunos2.txt", "w", encoding="utf-8") as arquivo:
                for aluno in alunos:
                    arquivo.write(
                        f"{aluno['id']};{aluno['nome']};"
                        f"{aluno['idade']};{aluno['curso']}\n"
                    )
            print("Aluno alterado:D")
            return
    print("Aluno não encontrado:C")

def sistema_alunos():
    alunos = []
    with open("alunos2.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            id, nome, idade, curso = linha.strip().split(";")
            aluno = {
                "id": int(id),
                "nome": nome,
                "idade": int(idade),
                "curso": curso
            }
            alunos.append(aluno)

    while True:
        print("    Sistema dos Alunos")
        print("1 - Listar alunos")
        print("2 - Buscar aluno")
        print("3 - Cadastrar aluno")
        print("4 - Remover aluno")
        print("5 - Alterar aluno")
        print("6 - Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            listar_alunos(alunos)
        elif opcao == "2":
            buscar_aluno(alunos)
        elif opcao == "3":
            cadastrar_aluno(alunos)
        elif opcao == "4":
            remover_aluno(alunos)
        elif opcao == "5":
            alterar_aluno(alunos)
        elif opcao == "6":
            print("Encerrado")
            break
        else:
            print("Opção inválida>:C")

sistema_alunos()
