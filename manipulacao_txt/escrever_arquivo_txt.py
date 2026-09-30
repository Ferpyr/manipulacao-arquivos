# Modo "r - Abre o arquivo para leitura
# Modo "w" - Abre para escrita e apaga o conteúdo existente
# Modo "a" - Adiciona novo conteúdo no final do arquivo
# Modo "x" - Cria um arquivo novo e gera erro se ele ja existir

def criar_arquivo():
    # O "with" fecha o arquivo
    # O "open()" função para leitura ou escrita de arquivos
    with open("alunos.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("Renan\n")
        arquivo.write("Carlos\n")
        arquivo.write("Moises\n")

#criar_arquivo()

def adicionar_aluno(nome):
    with open("alunos.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(nome + "\n")
#adicionar_aluno("Neymar")
#adicionar_aluno("Pelé")
#adicionar_aluno("Maradona")


def listar_alunos():
    with open("alunos.txt", "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
    print(f"O conteúdo arquivo alunos é: {conteudo}")

#listar_alunos()

def listar_alunos_individual():
    # lista_alunos = []
    with open("alunos.txt", "r", encoding="utf-8") as arquivo:
        nomes_alunos = [nome.strip() for nome in arquivo]
        # for linha in arquivo:
        #    lista_alunos.append(linha.strip())

    print(f"Lista de alunos: {nomes_alunos}")
#listar_alunos_individual()


def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))

    with open("alunos_cadastro.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{nome};{idade}\n")

    print(f"O aluno {nome} cadastrado com sucesso!")

#cadastrar_aluno()

def listar_cadastro():
    itens_cadastro = []
    with open("cadastro.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            nome, idade = linha.strip().split(";")

            obj = {
                "nome": nome,
                "idade": idade
            }

            itens_cadastro.append(obj)
    print(f"itens cadastrados: {itens_cadastro}")

listar_cadastro()