def calcular_total(numeros):
    return sum(numeros)

def retorna_ant_suc(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    
    return antecessor, sucessor

print(calcular_total([10,20,30,40]))
print(retorna_ant_suc(8))