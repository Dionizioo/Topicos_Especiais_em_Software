# -*- coding: utf-8 -*-
import json
'''import json

dic_contas = {
    'contas': [
        {'numero': 100, 'nome': 'Maria', 'saldo': 24.90},
        {'numero': 101, 'nome': 'Pedro', 'saldo': 30.00},
        {'numero': 102, 'nome': 'João', 'saldo': 40.00},
        {'numero': 103, 'nome': 'Ana', 'saldo': 50.00},
        {'numero': 104, 'nome': 'Jules', 'saldo': 60.00},
        {'numero': 105, 'nome': 'Laura', 'saldo': 70.00},
        {'numero': 106, 'nome': 'Maria', 'saldo': 80.00}
    ]
}

# Salvando o dicionário em um arquivo JSON
with open('contas.json', 'w', encoding='utf-8') as file:
    json.dump(dic_contas, file, ensure_ascii=False, indent=4)
'''

# Lendo o conteúdo do arquivo JSON
with open('contas.json', 'r', encoding='utf-8') as file:
    dic_contas = json.load(file)

    print(dic_contas)
