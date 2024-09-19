"""while True:
    try:
        filemane = input("Digite o nome do arquivo: ")

        if not filemane:
            raise FileExistsError('Arquivo não encontrado')


    except FileExistsError:
        print('Arquivo não encontrado')

    else:
        file = open(filemane, 'r')
        print(file.read())
        file.close()
"""

'''with open('contas.txt', 'w') as file:
    file.write("100 Jules 24,90\n")
    file.write("101 Maria 30,00\n")
    file.write("102 Pedro 40,00\n")
    file.write("103 João 50,00\n")
    file.write("104 Ana 60,00\n")

    print('500 laura 70,00', file=file)
print("-"*30)

with open('contas.txt', 'r') as file:
    print( f'{"Contas":<10}{"Nome":<10}{"Valor":>10}')

    for linha in file:
       # print(linha.slit())
        co , no , sal = linha.split()
        print(f'{co:<10}{no:.<10}{sal:.>10}')

print("-"*30)

contas = open('contas.txt', 'r')
temp = open('contas_temp.txt', 'w')

with contas, temp:
    for linha in contas:
        co , no , sal = linha.split()
        if co !='104':
            temp.write(linha)
        else:
            nova_linha = ' '.join([co, 'Jules', sal])
            temp.write(nova_linha)

import os
os.remove('contas.txt')
os.rename('contas_temp.txt', 'contas.txt') '''


'''Desafio 1: Leitor de Arquivos com Contagem de Palavras
Objetivo: Crie um programa que leia o conteúdo de um arquivo de texto,
conte a ocorrência de cada palavra no arquivo e exiba o resultado em ordem decrescente de frequência.

Requisitos:
Solicite ao usuário o nome de um arquivo de texto.
Abra e leia o arquivo (use exceções para lidar com a ausência do arquivo).
Conte quantas vezes cada palavra aparece no arquivo.
Exiba o resultado de forma que as palavras mais frequentes apareçam primeiro, seguidas da contagem.
Desafio Extra:
Ignore maiúsculas/minúsculas (ex: "Python" e "python" contam como a mesma palavra).
Remova pontuações (ex: "palavra," e "palavra" devem ser contadas como a mesma).'''

import string
from collections import Counter

def contarpalavras(arquivo):
    try:
        with open(arquivo, 'r', encoding='utf-8') as file:
            texto = file.read()

            #conveter para minisculas e remover pontuação
            texto = texto.lower()
            texo = texto.translate(str.maketrans('','', string.punctuation))

            #separa as palavaras e contar a frequencia
            palavras = texto.split()
            contador= Counter(palavras)

            for palavras , frequencia in contador.most_common():
                print(f'{palavras}:{frequencia}')
    except FileNotFoundError:
        print('Arquivo não encontrado')


#solicitar o nome do arquivo
nome_arquivo = input('Digite o nome do arquivo: ')
contarpalavras(nome_arquivo)