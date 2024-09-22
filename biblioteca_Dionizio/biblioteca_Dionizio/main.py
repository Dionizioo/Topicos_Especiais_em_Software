import os
import shutil
import sqlite3
import csv
from pathlib import Path
from datetime import datetime

# Diretórios principais
base_dir = Path('meu_sistema_livraria')
backup_dir = base_dir / 'backups'
data_dir = base_dir / 'data'
export_dir = base_dir / 'exports'


# Criando a estrutura de diretórios se não existir
def criar_diretorios():
    for directory in [backup_dir, data_dir, export_dir]:
        os.makedirs(directory, exist_ok=True)
    print("Estrutura de diretórios criada com sucesso.")


criar_diretorios()

# Caminho do banco de dados
db_path = data_dir / 'livraria.db'


# Função para inicializar o banco de dados
def init_db():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

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


init_db()


# Funções CRUD

# Adicionar um novo livro
def adicionar_livro(titulo, autor, ano_publicacao, preco):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO livros (titulo, autor, ano_publicacao, preco) 
        VALUES (?, ?, ?, ?)
    ''', (titulo, autor, ano_publicacao, preco))

    conn.commit()
    conn.close()
    print("Livro adicionado com sucesso.")


# Exibir todos os livros
def exibir_livros():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM livros')
    livros = cursor.fetchall()

    print("Livros cadastrados:")
    for livro in livros:
        print(livro)

    conn.close()


# Atualizar preço de um livro
def atualizar_preco(id_livro, novo_preco):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE livros
        SET preco = ?
        WHERE id = ?
    ''', (novo_preco, id_livro))

    conn.commit()
    conn.close()
    print(f"Preço do livro {id_livro} atualizado para {novo_preco}.")


# Remover um livro
def remover_livro(id_livro):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('DELETE FROM livros WHERE id = ?', (id_livro,))

    conn.commit()
    conn.close()
    print(f"Livro {id_livro} removido com sucesso.")


# Buscar livros por autor
def buscar_livros_por_autor(autor):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM livros WHERE autor = ?', (autor,))
    livros = cursor.fetchall()

    print(f"Livros do autor {autor}:")
    for livro in livros:
        print(livro)

    conn.close()


# Backup do banco de dados
def fazer_backup():
    backup_file = backup_dir / f"backup_livraria_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.db"
    shutil.copy(db_path, backup_file)
    print(f"Backup criado: {backup_file}")


# Exportar dados para CSV e também corrigir os utf-8
def exportar_para_csv():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM livros')
    livros = cursor.fetchall()

    csv_file = export_dir / 'livros_exportados.csv'
    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'Titulo', 'Autor', 'Ano de Publicação', 'Preço'])
        writer.writerows(livros)

    print(f"Dados exportados para {csv_file}")
    conn.close()


# Importar dados de CSV
def importar_de_csv(csv_file):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    with open(csv_file, newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            cursor.execute('''
                INSERT INTO livros (titulo, autor, ano_publicacao, preco)
                VALUES (?, ?, ?, ?)
            ''', (row[1], row[2], row[3], row[4]))

    conn.commit()
    conn.close()
    print(f"Dados importados de {csv_file}")


# Limpeza de backups antigos
def limpar_backups_antigos():
    backups = sorted(backup_dir.glob('*.db'), key=os.path.getmtime)

    while len(backups) > 5:
        backup_antigo = backups.pop(0)
        os.remove(backup_antigo)
        print(f"Backup removido: {backup_antigo}")


# Menu interativo
def menu():
    while True:
        print("""
        1. Adicionar novo livro
        2. Exibir todos os livros
        3. Atualizar preço de um livro
        4. Remover um livro
        5. Buscar livros por autor
        6. Exportar dados para CSV
        7. Importar dados de CSV
        8. Fazer backup do banco de dados
        9. Sair
        """)

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            titulo = input("Título: ")
            autor = input("Autor: ")
            ano = int(input("Ano de Publicação: "))
            preco = float(input("Preço: ").replace(',', '.'))
            fazer_backup()
            adicionar_livro(titulo, autor, ano, preco)

        elif opcao == '2':
            exibir_livros()

        elif opcao == '3':
            id_livro = int(input("ID do Livro: "))
            novo_preco = float(input("Novo Preço: ").replace(',', '.'))
            fazer_backup()
            atualizar_preco(id_livro, novo_preco)

        elif opcao == '4':
            id_livro = int(input("ID do Livro: "))
            fazer_backup()
            remover_livro(id_livro)

        elif opcao == '5':
            autor = input("Autor: ")
            buscar_livros_por_autor(autor)

        elif opcao == '6':
            exportar_para_csv()

        elif opcao == '7':
            csv_file = input("Caminho do arquivo CSV: ")
            fazer_backup()
            importar_de_csv(csv_file)

        elif opcao == '8':
            fazer_backup()

        elif opcao == '9':
            limpar_backups_antigos()
            print("Saindo...")
            break

        else:
            print("Opção inválida! Por favor, escolha uma opção válida.")


menu()
