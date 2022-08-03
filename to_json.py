import json

ar = []

with open('Запрет.txt', encoding='utf-8') as r:
    for i in r:
        n = i.lower().split('\n')[0]
        if n != '':
            ar.append(n)

with open('Запрет.json', 'w', encoding='utf-8') as e:
    json.dump(ar, e)
