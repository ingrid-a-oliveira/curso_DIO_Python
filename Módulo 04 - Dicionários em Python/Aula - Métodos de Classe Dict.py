contatos = {
    "ana@gmail.com": {"Nome": "Ana", "Telefone": "2222-2222"},
    "ingrid@gmail.com": {"Nome": "Ingrid", "Telefone": "1111-1111"},
    "maria@gmail.com": {"Nome": "Maria", "Telefone": "3333-3333"}
}

#Limpa o conteúdo do dicionário
"""contatos.clear()
print(contatos)"""

#Faz uma cópia do dicionário, mas no caso de novas atribuições o dicionário copiado é alterado e o original se mantem sem alterações.
"""copia = contatos.copy()
print(copia)
copia["ingrid@gmail.com"] = {"Nome": "Gui"}"""

"""print(contatos["ingrid@gmail.com"])
print(copia["ingrid@gmail.com"])"""

#Adiciona várias chaves de uma vez, na segunda opção adiciona também um valor padrão para as chaves. Ele cria um dicionário novo, não altera o existente.
"""dict.fromkeys(["Nome", "Telefone"])"""

"""print(dict.fromkeys(["Melhor Sombra", "Sombra mais forte", "Formiga"], 
                    "Beru"))"""

#Busca uma chave no dicionário, caso a chave não exista, ele retornará "none", evitando o erro e encerramento do programa.
"""print(contatos.get("chave"))
print(contatos.get("ingrid@gmail.com"))
print(contatos.get("chave", {})) #Nesse caso, a chave não existe no dicionário e o elemento após a vírgula retornará como resultado.
print(contatos.get("maria@gmail.com", {})) #Nesse caso não retorna {} como resultado pois a chave existe no dicionário"""

#Retorna uma lista de tuplas, sendo útil para o comando "for", por exemplo.
"""print(contatos.items())
"""
#Retorna as chaves do dicionário
"""print(contatos.keys())
"""
"""for chave in contatos.keys():
    print(chave)"""
    
#Remove uma chave do dicionário
"""contatos.pop("ana@gmail.com")
print(contatos)"""

#Caso não encontre a chave solicitada para exclusão, retornará o valor definido.
"""remove = contatos.pop("none@gmail.com", {})
print(remove)"""

#Não informa a chave, ele remove os itens na sequência existente no dicionário
"""remover = contatos.popitem()
print(remover)
print(contatos)"""

#Se a chave informada existir, mantem o valor original. Se não existir a chave no dicionário, incluirá a chave com o valor informado.
pessoa = {"Nome": "Killua", "Sobrenome": "Zoldyck"}
pessoa.setdefault("Nome", "Natsu")
print(pessoa)

pessoa.setdefault("Idade", "14")
print(pessoa)

# Substitui os dados da chave se ela já existir.
# Se a chave não existir, cria uma nova.
contatos.update({"ana@gmail.com": {"Nome": "Lara"}})
print(contatos)

contatos.update({"samuel@gmail.com": {"Nome": "Samuel", "Telefone": "4444-4444"}})
print(contatos)

#Retorna todos os valores
print(contatos.values())

#Verifica se os dados informados são chaves no dicionário
resultado = "samuel@gmail.com" in contatos
print(resultado)

resultado = "none@gmail.com" in contatos
print(resultado)

resultado = "idade" in contatos["ana@gmail.com"]
print(resultado)

#Remover valor do dicionário
del contatos["ana@gmail.com"]
print(contatos)

del contatos["ingrid@gmail.com"]["Telefone"]
print(contatos)

del contatos #deleta "contatos" inteiro