#Conjunto (set) é uma relação de itens não ordenada, imutável (em relação aos componentes e não ao conjunto) e desconsidera valores duplicados.

numero = set([1, 2, 3, 4, 4, 5, 8, 7, 9, 10, 11, 15, 12, 12, 12, 14, 16])
print(numero)

letras = set("abacate")
print(letras)

carros = set(["opala", "chevette", "fusca", "brasilia", "opala"])
print(carros)

personagens = {"Luffy", "Zoro", "Dabi", "Natsu", "Killua", "Nezuko", "Sukuna", "Nezuko", "Luffy"}
print(personagens)

#Pelo set não é possível acessar o índice dos elementos, para isso seria necessário converter o conjunto em lista.

personagens = list(personagens)
print(personagens[4])

for carro in carros:
    print(carro)
    
for indice, carro in enumerate(carros):
    print(f"{indice+1}: {carro}")

#união    
personagens_01 = {"Luffy", "Zoro"}
personagens_02 = {"Chopper", "Robin"}

mugiwaras = personagens_01.union(personagens_02)
print(mugiwaras)

#intersecção
melhores_sombras = {"Beru", "Igris", "Iron", "Bellion"}
sombras_fortes = {"Bellion", "Beru", "Igris"}

top_sombras = melhores_sombras.intersection(sombras_fortes)
print(top_sombras)

#diferença
fora_top = melhores_sombras.difference(sombras_fortes)
print(fora_top)

#diferença simétrica
conjunto_a = {0, 1, 2, 4}
conjunto_b = {1, 2, 3, 4}
diferenca_simetrica = conjunto_a.symmetric_difference(conjunto_b)
print(diferenca_simetrica)

#verificação de subconjunto
conjunto_c = {1, 2, 3}
conjunto_d = {5, 6, 8, 9, 1, 3, 2}
print(conjunto_c.issubset(conjunto_d)) #conjunto c é subconjunto do conjunto d
print(conjunto_d.issubset(conjunto_c)) #conjunto d não é subconjunto do conjunto c"""

#verificação de conjunto
print(conjunto_c.issuperset(conjunto_d)) #conjunto c não abrange todos os itens do conjunto d
print(conjunto_d.issuperset(conjunto_c)) #conjunto d abrange todos os itens do conjunto c

#isdisjoint
conjunto_e = {1, 2, 3, 4, 5}
conjunto_f = {6, 7, 8, 9}
conjunto_g = {1, 0}
verif_05 = conjunto_e.isdisjoint(conjunto_f)
verif_06 = conjunto_e.isdisjoint(conjunto_g)
print(verif_05) #os conjuntos "e" e "f" não possuem elementos em comum
print(verif_06) #os conjuntos compartilham elementos em comum

#adicionar elementos
viloes = {"big mom", "barba negra", "inveja", "elfo de gelo", "shigaraki"}
print(viloes)
viloes.add("Dabi")
viloes.add("Doflamingo")
viloes.add("Muzan")
print(viloes)

"""#limpar set
viloes.clear()
print(viloes)"""

#copiar set
viloes.copy()
print(viloes)

#excluir elemento (se for inserido um elemento que não existe no conjunto, ele ignora e executa sem erro)
viloes.discard("inveja")
print(viloes)

#remover elemento
viloes.pop()
print(viloes)
viloes.pop()
print(viloes)

#remove - semelhante ao "discard", mas se o elemento não existir no conjunto apresentará erro ao executar
numeros = {0, 1, 2, 3, 4, 5, 1, 5, 8, 1, 9, 6}

numeros.remove(3)
print(numeros)

"""numeros.remove(51)
print(numeros)"""

#verificar quantidade de elementos no conjunto (não conta elementos repetidos)
print(len(numeros))

#verificar se o elemento está no conjunto
print(1 in numeros)
print(55 in numeros)