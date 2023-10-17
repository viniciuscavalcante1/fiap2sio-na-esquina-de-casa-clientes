from Cliente import Cliente
from NoAVL import NoAVL
from ArvoreAVL import ArvoreAVL
clientes = []  # Uma lista para armazenar os clientes

while True:
    print("Cadastro de Cliente")
    nome = input("Nome completo: ")
    data_nascimento = input("Data de Nascimento: ")
    telefone = input("Contato telefônico: ")
    email = input("E-mail: ")
    endereco = input("Endereço: ")
    cpf = input("CPF: ")

    # Cria um objeto Cliente com os dados informados
    novo_cliente = Cliente(nome, data_nascimento, telefone, email, endereco, cpf)
    clientes.append(novo_cliente)  # Adiciona o cliente à lista

    continuar = input("Deseja cadastrar outro cliente? (S/N): ")
    if continuar.lower() != 's':
        break

def buscar_cliente_por_cpf(cpf):
    for cliente in clientes:
        if cliente.cpf == cpf:
            return cliente
    return None  # Retorna None se o cliente não for encontrado

cpf_busca = input("Digite o CPF que deseja buscar: ")
cliente_encontrado = buscar_cliente_por_cpf(cpf_busca)

if cliente_encontrado:
    print("Cliente encontrado:")
    print(f"Nome: {cliente_encontrado.nome}")
    print(f"Data de Nascimento: {cliente_encontrado.data_nascimento}")
    # Adicione outros campos aqui
else:
    print("Cliente não encontrado.")
arvore_avl = ArvoreAVL()

# Inserir CPFs
cpfs = ["1", "2", "3", "4", "5", "6"]

for cpf in cpfs:
    arvore_avl.inserir_cpf(cpf)

# Buscar um CPF e contar comparações
cpf_busca = "6"
cpf_encontrado, comparacoes = arvore_avl.contar_comparacoes(cpf_busca)

if cpf_encontrado:
    print("CPF encontrado:", cpf_encontrado)
    print("Comparações:", comparacoes)
    print("Caminho percorrido:", arvore_avl.caminho_comparacoes)
else:
    print("CPF não encontrado.")

# Função para ordenar uma lista de nomes usando o algoritmo QuickSort
def quicksort(lista):
    if len(lista) <= 1:
        return lista

    # Escolhe o pivô (neste caso, o nome do cliente no meio da lista)
    pivot = lista[len(lista) // 2]

    # Divide a lista em três partes: menores, iguais e maiores que o pivô
    menores = [nome for nome in lista if nome < pivot]
    iguais = [nome for nome in lista if nome == pivot]
    maiores = [nome for nome in lista if nome > pivot]

    # Recursivamente ordena as partes menores e maiores
    return quicksort(menores) + iguais + quicksort(maiores)

# Suponha que nomes_clientes seja a lista de nomes de clientes
nomes_clientes = ["Alice", "Carlos", "Zapdos", "Eva", "David", "Bia", "Yuri"]

# Chama a função de ordenação
nomes_clientes_ordenados = quicksort(nomes_clientes)

# Exibe a lista de nomes ordenados
print("Nomes de clientes ordenados:", nomes_clientes_ordenados)