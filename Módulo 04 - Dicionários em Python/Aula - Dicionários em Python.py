#O dicionário em python serve para armazenar pares de informações, em resumo seria como um conjunto de perguntas e respostas.

pessoa = {
    "nome": "Toya",
    "Apelido": "Dabi",
    "Individualidade": "Cremação",
    "Problemas": "Daddy Issues"    
}

#Acrescentar item ao dicionário
pessoa["Pai"] = "Endeavor"
print(pessoa["nome"])
print(pessoa["Pai"])

print(pessoa)

#Existe a possibilidade de criar um dicionário por dict.
"""pessoa = dict(nome="Toya", 
              Apelido="Dabi",
              Individualidade="Cremação",
              Problemas="Daddy Issues")

print(pessoa["Individualidade"])"""

#Dicionário aninhado possui uma estrutura similar a um banco de dados.
contatos = {
    "ana@gmail.com": {"Nome": "Ana", "Telefone": "2222-2222"},
    "ingrid@gmail.com": {"Nome": "Ingrid", "Telefone": "1111-1111"},
    "maria@gmail.com": {"Nome": "Maria", "Telefone": "3333-3333", "info_extra": {"Celular": "6363-6363"}}
}
print(contatos["ingrid@gmail.com"])
print(contatos["maria@gmail.com"]["Nome"])

info_extra = contatos["maria@gmail.com"]["info_extra"]["Celular"]
print(info_extra)

"""for chave, valor in contatos.items():
    print(chave, contatos[chave])"""

for chave in contatos:
    print(chave, contatos[chave])
    
    
#O dicionário não permite a repetição de chaves, caso seja atribuído um valor diferente para uma chave existente, ele fará a substituição do valor. 
pessoa["nome"] = "Shoto"
pessoa["Apelido"] = "meio a meio"
pessoa["Individualidade"] = "Fogo/Gelo"
print(pessoa)