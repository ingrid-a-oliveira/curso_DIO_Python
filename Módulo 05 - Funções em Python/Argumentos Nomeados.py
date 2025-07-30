# Versão 1: função que sempre pede os dados via input do usuário
"""def salvar_carros():
    marca = input("Digite a marca do carro: ")
    modelo = input("Digite o modelo do carro: ")
    ano = input("Digite o ano do modelo do carro: ")
    placa =  input("Digite a placa do carro: ")
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")
    
salvar_carros()"""

# Versão 2: A função recebe os dados como parâmetros e exibe a mensagem no terminal   
"""def salvar_carros(marca, modelo, ano, placa):
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")
    
salvar_carros(marca="Chevrolet", modelo="Opala", ano="1978", placa="AAA-1234")"""

#Versão 3: A função aceita parâmetros opcionais e, se não forem informados, solicita ao usuário
def salvar_carros(marca=None, modelo=None, ano=None, placa=None):
    if marca is None:
        marca = input("Digite a marca do carro: ")
    if modelo is None:
        modelo = input("Digite o modelo do carro: ")
    if ano is None:
        ano = input("Digite o ano do modelo do carro: ")
    if placa is None:
        placa =  input("Digite a placa do carro: ")
        
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")
    
# Passa todos os dados diretamente, não pede input
"""salvar_carros(marca="Chevrolet", modelo="Opala", ano="1978", placa="AAA-1234")"""

#Passa só uma das informações, o resto pede para o usuário
"""salvar_carros(marca="Chevrolet")"""

#Nenhum dado é informado diretamente, todos os dados são pedidos via input
salvar_carros()