biblioteca = []
print("\nBem-vindo à Biblioteca Livrista!")
# Certifique-se de que as variáveis `livros` e `biblioteca` estão definidas
livros = [
    {"Título": "Noites Brancas", "Genero": "literatura_russa", "Autor": "Fiodor Dostoievski", "Ano_de_Publicação": 1848, "Quantidade_Disponível": 10},
    {"Título": "Memórias do Subsolo", "Genero": "literatura_russa", "Autor": "Fiodor Dostoievski", "Ano_de_Publicação": 1864, "Quantidade_Disponível": 20},
    {"Título": "Como Falar em Público e Encantar as Pessoas", "Genero": "auto_ajuda", "Autor": "Dale Carnegie", "Ano_de_Publicação": 2012, "Quantidade_Disponível": 30},
    {"Título": "Diário de uma Paixão", "Genero": "romance", "Autor": "Nicholas Sparks", "Ano_de_Publicação": 1996, "Quantidade_Disponível": 40},
    {"Título": "A Queda", "Genero": "literatura_francesa", "Autor": "Albert Camus", "Ano_de_Publicação": 1956, "Quantidade_Disponível": 30},
    {"Título": "O Estrangeiro", "Genero": "literatura_francesa", "Autor": "Albert Camus", "Ano_de_Publicação": 1942, "Quantidade_Disponível": 20},
    {"Título": "O Mito de Sísifo", "Genero": "literatura_francesa", "Autor": "Albert Camus", "Ano_de_Publicação": 1942, "Quantidade_Disponível": 10},
    {"Título": "A Náusea", "Genero": "literatura_francesa", "Autor": "Jean-Paul Sartre", "Ano_de_Publicação": 1938, "Quantidade_Disponível": 30},
    {"Título": "Política", "Genero": "filosofia_grega", "Autor": "Aristóteles", "Ano_de_Publicação": "Cerca de 350 a.C.", "Quantidade_Disponível": 20},
    {"Título": "Ética a Nicômaco", "Genero": "filosofia_grega", "Autor": "Aristóteles", "Ano_de_Publicação": "Cerca de 340 a.C.", "Quantidade_Disponível": 15},
    {"Título": "Metafísica", "Genero": "filosofia_grega", "Autor": "Aristóteles", "Ano_de_Publicação": "Cerca de 340 a.C.", "Quantidade_Disponível": 15},
    {"Título": "O Banquete", "Genero": "filosofia_grega", "Autor": "Platão", "Ano_de_Publicação": "Cerca de 385-370 a.C.", "Quantidade_Disponível": 10},
    {"Título": "Alegoria da Caverna", "Genero": "filosofia_grega", "Autor": "Platão", "Ano_de_Publicação": "Parte de 'A República', cerca de 380 a.C.", "Quantidade_Disponível": 10},
    {"Título": "A República", "Genero": "filosofia_grega", "Autor": "Platão", "Ano_de_Publicação": "Cerca de 380 a.C.", "Quantidade_Disponível": 10},
    {"Título": "A Riqueza das Nações", "Genero": "economia", "Autor": "Adam Smith", "Ano_de_Publicação": 1776, "Quantidade_Disponível": 5},
    {"Título": "O Capital", "Genero": "economia", "Autor": "Karl Marx", "Ano_de_Publicação": "Volume I: 1867", "Quantidade_Disponível": 5},
    {"Título": "Principles of Economics", "Genero": "economia", "Autor": "Carl Menger", "Ano_de_Publicação": 1871, "Quantidade_Disponível": 5},
    {"Título": "As Seis Lições", "Genero": "economia", "Autor": "Ludwig von Mises", "Ano_de_Publicação": 1959, "Quantidade_Disponível": 5},
    {"Título": "O Liberalismo", "Genero": "economia", "Autor": "Ludwig von Mises", "Ano_de_Publicação": 1927, "Quantidade_Disponível": 5},
    {"Título": "Liberdade & Prosperidade", "Genero": "economia", "Autor": "Ayn Rand", "Ano_de_Publicação": "Publicado em várias obras ao longo dos anos", "Quantidade_Disponível": 5}
]



def exibir_livros():
    print("\nLivros disponíveis para empréstimo:")
    for livro in livros:
        print(f"Título: {livro['Título']}, Genero: {livro['Genero']}, Autor: {livro['Autor']}, "
              f"Ano de Publicação: {livro['Ano_de_Publicação']}, Quantidade Disponível: {livro['Quantidade_Disponível']}")
exibir_livros()



def buscar_titulo(livros, titulo):
    for livro in livros:
        if livro["Título"].lower() == titulo.lower():
            return livro
    return None

def realizar_emprestimo(livros, biblioteca):
    while True:
        livro_titulo = input("\nDigite o nome do livro que você deseja emprestar (ou 0 para finalizar): ")
        if livro_titulo == '0':
            print("Finalizando empréstimo.")
            break

        livro_existente = buscar_titulo(livros, livro_titulo)

        if livro_existente:
            try:
                quantidade_emprestada = int(input("Digite a quantidade desejada: "))
                if quantidade_emprestada <= 0:
                    print("Quantidade inválida! Tente novamente.")
                    continue
                if livro_existente["Quantidade_Disponível"] >= quantidade_emprestada:
                    livro_existente["Quantidade_Disponível"] -= quantidade_emprestada
                    biblioteca.append({
                        "Título": livro_titulo,
                        "Quantidade_Emprestada": quantidade_emprestada
                    })
                    print(f"Empréstimo de {quantidade_emprestada} cópias do livro '{livro_titulo}' realizado com sucesso!")
                else:
                    print("Quantidade insuficiente disponível.")
            except ValueError:
                print("Entrada inválida! Tente novamente.")
        else:
            print("Livro não encontrado na biblioteca.")
realizar_emprestimo(livros,biblioteca)

def devolver_livros(livro, quantidade_devolvida, livros, biblioteca):
    for item in biblioteca:

        if item['Título'].lower() == livro.lower():
            if item["Quantidade_Emprestada"] >= quantidade_devolvida:
                for acervo in livros:
                    if acervo["Título"].lower() == livro.lower():
                        acervo["Quantidade_Disponível"] += quantidade_devolvida
                        item["Quantidade_Emprestada"] -= quantidade_devolvida
                        if item["Quantidade_Emprestada"] == 0:
                            biblioteca.remove(item)
                        print(f"{quantidade_devolvida} x '{livro}' devolvido à biblioteca")
                        break
                else:
                    print("Livro não encontrado no catálogo.")
                break
            else:
                print("Quantidade devolvida maior do que a emprestada")
                return
    else:
        print("Livro não encontrado no registro de empréstimos.")
# Exemplo de uso com inputs
livro = input("Qual livro você deseja devolver? ")
quantidade_devolvida = int(input("Quantos exemplares você deseja devolver? "))
devolver_livros(livro, quantidade_devolvida, livros, biblioteca)

def adicionar_novo_livro(livro_titulo, genero, autor, ano_de_publicacao, quantidade_disponivel, livros):
    novo_livro = {
        'Título': livro_titulo,
        'Genero': genero,
        'Autor': autor,
        'Ano_de_Publicacao': ano_de_publicacao,
        'Quantidade_Disponível': quantidade_disponivel
    }
    livros.append(novo_livro)
    print(f"Livro '{livro_titulo}' adicionado com sucesso!")  # Mensagem de feedback ao usuário

    return livros

livro_titulo = input("Qual novo livro voce deseja adicionar : ")
genero = input("Gênero: ")
autor = input("Autor: ")
ano_de_publicacao = input("Ano de Publicação: ")
quantidade_disponivel = int(input("Quantidade Disponível: "))

# Inicializando a lista de livros vazia
livros = []

# Chamando a função com os dados coletados
adicionar_novo_livro(livro_titulo, genero, autor, ano_de_publicacao, quantidade_disponivel, livros)
print(livros)

def adicionar_livro(livros):
    while True:
        livro_titulo = input("\nDigite o nome do livro que você deseja adicionar à biblioteca (ou 0 para finalizar): ")
        if livro_titulo == '0':
            print("Finalizando adição de livros.")
            break

        livro_existente = buscar_titulo(livros, livro_titulo)
        if livro_existente:
            print("Livro já existe na biblioteca.")
        else:
            genero = input("Digite o gênero do livro: ")
            autor = input("Digite o autor do livro: ")
            ano_de_publicacao = input("Digite o ano de publicação do livro: ")
            quantidade_disponivel = int(input("Digite a quantidade disponível: "))
            if quantidade_disponivel <= 0:
                print("Quantidade inválida! Tente novamente.")
                continue
            adicionar_novo_livro(livro_titulo, genero, autor, ano_de_publicacao, quantidade_disponivel, livros)






# Lista de livros na biblioteca
livro = []
biblioteca=[]

print("\nObrigado por utilizar Biblioteca Livrista!")
print("\nÓtima leitura!")




