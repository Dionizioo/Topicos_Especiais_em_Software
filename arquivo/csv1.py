import csv

with open('filmes.csv',mode='r', encoding='utf-8') as file:
    csv_file = csv.reader(file)
    header=next(csv_file)

    #print(header)
    print('|', f' | '.join(header), '|')

    for linhas in csv_file:
        print('|', f' | '.join(linhas), '|')
