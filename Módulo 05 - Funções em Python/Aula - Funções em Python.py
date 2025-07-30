#Para criar uma função em Python utiliza-se o "def"
#Caso seja definido um argumento para a função, ficará entre parênteses, como "(nome)".
def exibir_mensagem():
    print("Hello World!!!")
    
exibir_mensagem()


def exibir_mensagem2(nome):
    print(f"Seja bem vindo(a), {nome}!")
    
exibir_mensagem2(nome="Ingrid")


def exibir_mensagem3(nome="Anônimo"):
    print(f"Seja bem vindo(a), {nome}!!!")
    
exibir_mensagem3()
exibir_mensagem3(nome="Jake")

def boas_vindas(nome = "anonimo"):
    print(f"Bem-vindo(a), {nome}! Você sobreviveu até aqui... por enquanto.")
    
boas_vindas(nome="Ingrid")

def boas_vindas(nome = "anonimo"):
    return(f"Bem-vindo(a), {nome}! Você sobreviveu até aqui... por enquanto.")
mensagem=boas_vindas("Ingrid")
print(mensagem)