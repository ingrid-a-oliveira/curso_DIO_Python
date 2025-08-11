def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    
    if funcao.__name__ == "somar":
        print(f"O resultado da operação {a} + {b} = {resultado}")
        
    elif funcao.__name__ == "subtrair":
        print(f"O resultado da operação {a} - {b} = {resultado}")
    
exibir_resultado(10, 10, somar)
exibir_resultado(10, 10, subtrair)

op = somar
print(op(1,58))