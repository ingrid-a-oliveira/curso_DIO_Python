#Evitar utilizar variáveis globais, conforme exemplo abaixo. Por uma questão de boas práticas e visando evitar falhas durante a manutenção do código.
salario = 2000

def salario_bonus(bonus):
    global salario #se não informar que a variável está no escopo global, dará erro na execução do código
    salario += bonus
    return salario

print(salario_bonus(500))