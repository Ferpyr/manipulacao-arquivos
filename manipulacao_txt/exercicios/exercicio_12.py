def classificar_alunos():
    with open("alunos.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            nome, nota = linha.strip().split(";")
            nota = float(nota)
            if nota >= 6:
                condicao = "Aprovado"
            elif nota >= 4:
                condicao = "Recuperação"
            else:
                condicao = "Reprovado"
            print(f"{nome} - {nota} - {condicao}")
classificar_alunos()
