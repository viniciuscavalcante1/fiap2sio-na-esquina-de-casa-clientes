from Cliente import Cliente
from ArvoreAVL import ArvoreAVL

clientes = []
arvore_avl = ArvoreAVL()

print("Seja muito bem-vindo ao programa de cadastramento de clientes de Na Esquina de Casa!")
print("Por favor, selecione uma das seguintes opções: ")


def cadastrar_cliente():
    print("--- Cadastro de cliente ---")
    nome = input("Nome completo: ")
    data_nascimento = input("Data de nascimento: ")
    telefone = input("Contato telefônico: ")
    email = input("E-mail: ")
    endereco = input("Endereço: ")
    cpf = input("CPF: ")

    novo_cliente = Cliente(nome, data_nascimento, telefone, email, endereco, cpf)
    clientes.append(novo_cliente)
    arvore_avl.inserir_cpf(cpf)
    print("O cliente foi cadastrado com sucesso!")


def buscar_cliente_por_cpf_lista():
    cpf_busca = input("Digite o CPF que deseja buscar: ")
    for cliente in clientes:
        if cliente.cpf == cpf_busca:
            print("Cliente encontrado:")
            print(
                f"{'Nome': <20}{'Data de nascimento': <20}{'Contato telefônico': <20}{'E-mail': <20}{'Endereço': <20}{'CPF': <20}")
            print(
                f"{cliente.nome: <20}{cliente.data_nascimento: <20}{cliente.telefone: <20}{cliente.email: <20}{cliente.endereco: <20}{cliente.cpf: <20}")
            return
    print("Cliente não encontrado.")


def buscar_cliente_por_cpf_avl():
    cpf_busca = input("Digite o CPF que deseja buscar: ")
    cpf_encontrado, comparacoes = arvore_avl.contar_comparacoes(cpf_busca)
    if cpf_encontrado:
        print("Cliente encontrado:")
        print(f"{'CPF': <20}{'Comparações realizadas': <30}{'Caminho percorrido na AVL': <20}")
        print(f"{str(cpf_encontrado): <20}{str(comparacoes): <30}{str(arvore_avl.caminho_comparacoes): <20}")
    else:
        print("Cliente não encontrado.")


def listar_clientes_ordenados():
    def quicksort(lista):
        if len(lista) <= 1:
            return lista

        pivot = lista[len(lista) // 2]
        menores = [cliente for cliente in lista if cliente.nome < pivot.nome]
        iguais = [cliente for cliente in lista if cliente.nome == pivot.nome]
        maiores = [cliente for cliente in lista if cliente.nome > pivot.nome]

        return quicksort(menores) + iguais + quicksort(maiores)

    clientes_ordenados = quicksort(clientes)
    print("Lista de clientes em ordem alfabética:")
    print(
        f"{'Nome': <20}{'Data de nascimento': <20}{'Contato telefônico': <20}{'E-mail': <20}{'Endereço': <20}{'CPF': <20}")
    for cliente in clientes_ordenados:
        print(
            f"{cliente.nome: <20}{cliente.data_nascimento: <20}{cliente.telefone: <20}{cliente.email: <20}{cliente.endereco: <20}{cliente.cpf: <20}")


def sair_do_programa():
    print("Saindo do programa. Até logo!")
    exit()


while True:
    print("\nMenu Principal:")
    print("1. Cadastrar cliente")
    print("2. Buscar cliente por CPF (usando uma estrutura de dados simples chamada de Lista)")
    print("3. Buscar cliente por CPF (usando uma estrutura de dados super moderna e veloz chamada de Árvore AVL)")
    print("4. Listar clientes em ordem alfabética (usando um algoritmo super eficiente chamado de Quicksort!)")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_cliente()
    elif opcao == "2":
        buscar_cliente_por_cpf_lista()
    elif opcao == "3":
        buscar_cliente_por_cpf_avl()
    elif opcao == "4":
        listar_clientes_ordenados()
    elif opcao == "5":
        sair_do_programa()
    else:
        print("Opção inválida. Escolha uma opção válida do menu.")
