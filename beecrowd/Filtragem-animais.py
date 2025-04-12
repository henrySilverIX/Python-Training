animais = {"aguia": ["vertebrado", "ave", "carnivoro"],
           "pomba": ["vertebrado", "ave", "onivoro"],
           "homem": ["vertebrado", "mamifero", "onivoro"],
           "vaca": ["vertebrado", "mamifero", "herbivoro"],
           "pulga": ["invertebrado", "inseto", "hematofago"],
           "lagarta": ["invertebrado", "inseto", "herbivoro"],
           "sanguessuga": ["invertebrado", "anelideo", "hematofago"],
           "minhoca": ["invertebrado", "anelideo", "onivoro"]
           }

filo = input()
classe = input()
ordem = input()

caracteristicas_desejadas = [filo, classe, ordem]


'''
A parte (k for k, v in dicionario.items() if v == valor_desejado) é um gerador que percorre o dicionário,
e o k representa a chave de cada par (chave, valor).

if v == valor_desejado
Filtramos apenas os pares onde o valor (v) seja igual ao valor que estamos procurando.

k no início do gerador:

Significa que o gerador vai produzir somente as chaves (k) dos pares que passaram na filtragem.

'''

animal = next((k for k,v in animais.items() if v == caracteristicas_desejadas), None)

print(animal)


