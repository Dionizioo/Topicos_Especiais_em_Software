import sqlite3
from pathlib import Path

# Caminho do banco de dados
data_dir = Path('meu_sistema_livraria') / 'data'
db_path = data_dir / 'livraria.db'


# Função para inicializar o banco de dados
def inicializar_banco():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Criar tabela de livros se não existir
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS livros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL,
            ano_publicacao INTEGER NOT NULL,
            preco REAL NOT NULL
        )
    ''')

    conn.commit()
    conn.close()
    print("Banco de dados inicializado com sucesso.")


# Função para adicionar livros automaticamente
def adicionar_livros_automaticamente():
    livros = [
        # Júlio Verne
        ("Vinte Mil Léguas Submarinas", "Júlio Verne", 1870, 49.90),
        ("A Volta ao Mundo em 80 Dias", "Júlio Verne", 1873, 39.90),
        ("A Ilha Misteriosa", "Júlio Verne", 1874, 44.90),
        ("O Mistério do Castelo de Aá", "Júlio Verne", 1864, 29.90),
        ("Os Filhos do Capitão Grant", "Júlio Verne", 1867, 59.90),
        ("A Jangada", "Júlio Verne", 1881, 39.90),
        ("Dois Anos de Férias", "Júlio Verne", 1888, 49.90),
        ("A Casa dos Catorze Andares", "Júlio Verne", 1881, 44.90),
        ("O Farol do Fim do Mundo", "Júlio Verne", 1905, 29.90),
        ("A Estação de Suez", "Júlio Verne", 1890, 59.90),

        # Stephen King
        ("O Iluminado", "Stephen King", 1977, 49.90),
        ("A Espera de um Milagre", "Stephen King", 1996, 39.90),
        ("IT: A Coisa", "Stephen King", 1986, 59.90),
        ("Misery", "Stephen King", 1987, 44.90),
        ("O Cemitério", "Stephen King", 1983, 29.90),
        ("A Dança da Morte", "Stephen King", 1978, 54.90),
        ("Cemitério Maldito", "Stephen King", 1983, 34.90),
        ("O Apanhador de Sonhos", "Stephen King", 2001, 49.90),
        ("A Torre Negra", "Stephen King", 1982, 39.90),
        ("Sob a Redoma", "Stephen King", 2009, 59.90),
    ]

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    for livro in livros:
        cursor.execute('''
            INSERT INTO livros (titulo, autor, ano_publicacao, preco) 
            VALUES (?, ?, ?, ?)
        ''', livro)

    conn.commit()
    conn.close()
    print("Livros adicionados com sucesso!")


# Inicializar banco de dados e tabela
inicializar_banco()

# Chamar a função para adicionar livros
adicionar_livros_automaticamente()
