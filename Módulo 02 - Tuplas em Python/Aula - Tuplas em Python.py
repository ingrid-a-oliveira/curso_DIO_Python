"""frutas = ("Laranja", "Maçã", "Melancia",)"""
"""print(frutas[0])"""

#frutas[0] = "uva"
#print(frutas)      #tuplas não permitem alterações nos dados inseridos, diferente da lista que é possível acrescentar ou remover itens.

"""letras = tuple("python")"""
"""print(letras)"""    #('p', 'y', 't', 'h', 'o', 'n')

"""numeros = tuple([1, 2, 3, 4])
print(numeros)"""   #(1, 2, 3, 4)

"""pais = ("Brasil",)  
print(pais)"""      #É utilizado parênteses e vírgula para se formar uma tupla, caso não tenha vírgula será uma string


#Para acessar um elemento de uma tupla, utiliza-se a variável que armazena a tupla seguida do índice entre colchetes, e o comando print para exibir o resultado no terminal.
"""print(frutas[2])
print(frutas[-2])"""

#tuplas podem armazenar outras tuplas, formando tabelas (elementos bidimensionais)
"""matriz = (
    (1, "a", 2),
    ("b", 3, 9),
    (6, 8, "i")
)

print(matriz[0])
print(matriz[0][0]) #seleciona resultado presente na linha 0 e coluna 0 (1)
print(matriz[-1][-1])"""

#fatiamento
"""tupla = letras
print(tupla)
print(tupla[2:])
print(tupla[:2])
print(tupla[1:3])
print(tupla[0:3:2])
print(tupla[:: ])
print(tupla[::-1])"""

"""carros = ("opala", "chevette", "fusca",)
for indice, carro in enumerate(carros):
    print(f"{indice+1}: {carro}")

print(carros.count("opala"))
print(carros.index("opala"))
print(len(carros))"""