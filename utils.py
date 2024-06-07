usuarios = {}
banco_usuarios = []
contas = []

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):

    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato, numero_saques

def deposito(saldo, extrato):
    valor = float(input("Informe o valor do depósito: "))

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato 

def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def cadastrar_usuario():
    nome = input("Informe seu nome: ")
    cpf = input("Informe seu CPF: ")
    for usuario in banco_usuarios:
        if usuario["cpf"] == cpf:
            print("CPF já cadastrado!")
            return None

    data_nascimento = input("Informe sua data_nascimento: ")
    
    endereco = input("Informe seu endereço (logradouro - número - bairro - sigla/cidade estado): ")
    
    usuarios.update({"nome": nome,"data de nascimento": data_nascimento, "cpf": cpf, "endereço": endereco})
    
    banco_usuarios.append(usuarios)
   
    print(banco_usuarios)
    
    return banco_usuarios 

def criar_conta(contador_de_contas):
    conta_bancaria = {}
    conta_bancaria['agencia'] = '0001'
    conta_bancaria['conta'] = contador_de_contas
    conta_bancaria['user'] = usuarios['nome']
    contas.append(conta_bancaria)
    contador_de_contas += 1
    print(contas)
    
    return contas, contador_de_contas

def listar_contas():
    print("=========== LISTA DE CONTAS ===========")
    for conta in contas:
        print(f"Agência: {conta['agencia']}\nConta: {conta['conta']}\nTitular: {conta['user']}\n")
    print("=======================================")