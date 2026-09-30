def listar_aprovados():
    aprovados = []
    with open("alunos.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            nome, nota = linha.strip().split(";")
            nota = float(nota)
            if nota >= 6.0:
                aprovados.append(f"{nome} - {nota}")
    print("Alunos aprovados:")
    for aluno in aprovados:
        print(aluno)
listar_aprovados()
