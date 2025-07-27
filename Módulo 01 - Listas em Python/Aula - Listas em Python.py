# frutas = ["banana","maçã","uva","kiwi"]
# print(frutas[0])

# lista = []

# lista.append(1)
# lista.append("Python")
# lista.append([40, 30, 20])

# l2 = lista.copy()

# print(lista)

# print(id(l2), id(lista))

# l2[0] = 2

# print(l2)
# print(lista)


"""cores = ["vermelho", "azul", "rosa", "roxo", "azul", "amarelo", "verde", "vermelho", "azul", "rosa", "vermelho", "branca"]

print(f"Há {cores.count("vermelho")} {'vez' if cores.count("vermelho") == 1 else 'vezes'} a cor vermelho")
print(f"Há {cores.count("azul")} {'vez' if cores.count("azul") == 1 else 'vezes'} a cor azul")
print(f"Há {cores.count("rosa")} {'vez' if cores.count("rosa") == 1 else 'vezes'} a cor rosa")
print(f"Há {cores.count("roxo")} {'vez' if cores.count("roxo") == 1 else 'vezes'} a cor roxo")
print(f"Há {cores.count("verde")} {'vez' if cores.count("verde") == 1 else 'vezes'} a cor verde")
print(f"Há {cores.count("branca")} {'vez' if cores.count("branca") == 1 else 'vezes'} a cor branca")
print(f"Há {cores.count("amarelo")} {'vez' if cores.count("amarelo") == 1 else 'vezes'} a cor amarelo")"""

linguagens = ["python", "js", "c"]

linguagens.extend(["java", "php", "ruby", "kotlin"])
print(linguagens)

"""print(f"A linguagem java está na posição {linguagens.index("java")+1}")"""

"""linguagens.pop(1)
print(linguagens)"""

"""linguagens.remove("c")
print(linguagens)"""

"""linguagens.reverse()
print(linguagens)
print(f"A linguagem js está na posição {linguagens.index("js")+1}")"""

"""linguagens.sort()
print(linguagens)"""

"""linguagens.sort(reverse=True)
print(linguagens)"""

"""linguagens.sort(key=lambda x: len(x))
print(linguagens)"""

linguagens.sort(key=lambda x: len(x), reverse=True)
print(linguagens)

print(f"A quantidade de itens na lista é de {len(linguagens)} itens.")