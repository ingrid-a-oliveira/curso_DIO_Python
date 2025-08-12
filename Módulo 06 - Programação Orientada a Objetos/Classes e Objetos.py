class Ambiente:
    def __init__(self, nome, piso, acabamento, comprimento, largura, esquadria):
        self.nome = nome
        self.piso = piso
        self.acabamento = acabamento
        self.comprimento = comprimento
        self.largura = largura
        self.esquadria = esquadria
        
    def calcular_area(self):
        return self.comprimento * self.largura
        
    def descricao_ambiente(self):
        return (f"\n{self.nome}\nFoi instalado {self.piso} no piso e as paredes possuem {self.acabamento} como revestimento.\nO {self.nome} possui {self.calcular_area()}m².")
        
ambientes = []

def listar_ambientes():
    if not ambientes:
        print("Nenhum ambiente cadastrado.")
        return False
    else:
        print("\nAmbientes cadastrados:")
        for i, amb in enumerate(ambientes, start=1):
            print(f"{i}. {amb.nome}")
        return True
        
while True:
    print("\n==== MENU ====")
    print("1. Adicionar ambiente")
    print("2. Listar ambientes")
    print("3. Calcular área de um ambiente")
    print("4. Ver descrição de um ambiente")
    print("5. Alterar cadastro de um ambiente")
    print("6. Excluir um ambiente")
    print("7. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        
        print("\n---Cadastro de Ambientes---")
        nome = input("Insira o nome do ambiente: ")
        piso = input("Insira o revestimento instalado no piso: ")
        acabamento = input("Insira o revestimento utilizado nas paredes: ")
        comprimento = int(input("Insira o comprimento do ambiente em metros: "))
        largura = int(input("Insira a largura do ambiente em metros: "))
        esquadria = input("Insira o material das esquadrias do ambiente: ")
        
        ambiente = Ambiente(nome, piso, acabamento, comprimento, largura, esquadria)
        ambientes.append(ambiente)
        print(f"O ambienta {nome} foi cadastrado com sucesso!")
        
    elif opcao == "2":
        listar_ambientes()
        
    elif opcao == "3":
        if listar_ambientes():
            escolha = int(input("Escolha o número do ambiente: "))
            if 1 <= escolha <= len(ambientes):
                area = ambientes[escolha - 1].calcular_area()
                print(f"A área do ambiente {ambientes[escolha - 1].nome} é {area}m².")
            else:
                print("Opção inválida.")
                
    elif opcao == "4":
        if listar_ambientes():
            escolha = int(input("Escolha o número do ambiente: "))
            if 1 <= escolha <= len(ambientes):
                print(ambientes[escolha - 1].descricao_ambiente())
            else:
                print("Entrada Inválida!")
                
                
    elif opcao == "5":
        if listar_ambientes():
            escolha = int(input("Escolha o número do ambiente para alterar: "))
            if 1 <= escolha <= len(ambientes):
                amb = ambientes[escolha - 1]
                print(f"Alterando '{amb.nome}' (pressione Enter para manter o valor atual):")

                novo_nome = input(f"Nome [{amb.nome}]: ") or amb.nome
                novo_piso = input(f"Piso [{amb.piso}]: ") or amb.piso
                novo_acabamento = input(f"Acabamento [{amb.acabamento}]: ") or amb.acabamento
                try:
                    novo_comprimento = input(f"Comprimento [{amb.comprimento}]: ")
                    novo_comprimento = float(novo_comprimento) if novo_comprimento else amb.comprimento
                    novo_largura = input(f"Largura [{amb.largura}]: ")
                    novo_largura = float(novo_largura) if novo_largura else amb.largura
                except ValueError:
                    print("Valor inválido para medidas. Alteração cancelada.")
                    continue
                nova_esquadria = input(f"Esquadria [{amb.esquadria}]: ") or amb.esquadria

                amb.nome = novo_nome
                amb.piso = novo_piso
                amb.acabamento = novo_acabamento
                amb.comprimento = novo_comprimento
                amb.largura = novo_largura
                amb.esquadria = nova_esquadria
                
                print("Cadastro atualizado com sucesso!")
            else:
                print("Opção inválida.") 
                
    elif opcao == "6":
        if listar_ambientes():
            escolha = int(input("Escolha o número do ambiente para excluir: "))
            if 1 <= escolha <= len(ambientes):
                removido = ambientes.pop(escolha - 1)
                print(f"Ambiente '{removido.nome}' excluído com sucesso!")
            else:
                print("Opção inválida.")

    elif opcao == "7":
        print("Saindo...")
        break

    else:
        print("Opção inválida, tente novamente.")