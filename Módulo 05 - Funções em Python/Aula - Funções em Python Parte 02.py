#Parâmetros Posicionais
#def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
#      ..........     ..........     ..........
#           |              |              |
#           |    Positional or heyword    |
#           |                             - Keyword only
#           ..Positional only

def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)
    
#Os parâmetros antes do / (modelo, ano, placa) só podem ser passados por posição, nunca usando nome=valor
#Os parâmetros depois da / (marca, motor, combustivel) podem ser passados por posição ou por nome.

#Valores passados por nome para os parâmetros "marca, motor, combustivel"
criar_carro("Palio", 1999, "AAA-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") #válido

#Valores passados por posição para todos os parâmetros
criar_carro("Palio", 1999, "AAA-1234", "Fiat", "1.0", "Gasolina") #válido

"""criar_carro(modelo="Palio", ano=1999, placa="AAA-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")""" #inválido

#Apenas por nome
def criar_carro_nome(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)
    
criar_carro_nome(modelo="Impala", ano=1967, placa="IMP-1967", marca="Chevrolet", motor="V8", combustivel="Gasolina")

#"Híbrido"
def criar_carro_hibrido(modelo, ano, placa, /, marca, *, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)
criar_carro_hibrido("Impala", 1967, "IMP-1967", marca="Chevrolet", motor="V8", combustivel="Gasolina") #Válido
criar_carro_hibrido("Impala", 1967, "IMP-1967", "Chevrolet", motor="V8", combustivel="Gasolina") #Válido
"""criar_carro_hibrido("Impala", 1967, "IMP-1967", "Chevrolet", "V8", "Gasolina")""" #inválido