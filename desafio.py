import utils as u 

print('===== Bem-vindo ao Banco do Fabricio! =====')

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[c] Cadastrar usuário
[f] Criar conta
[l] Listas contas   
[q] Sair

=> """

def main():
    saldo = 0
    extrato = ""
    numero_saques = 0
    limite = 500
    LIMITE_SAQUES =  3
    contador_de_contas = 1
    
    while True:

        opcao = input(menu)

        if opcao == "d":
            saldo, extrato = u.deposito(saldo, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = u.sacar(saldo= saldo, valor= valor, extrato = extrato, limite = limite, numero_saques = numero_saques, limite_saques = LIMITE_SAQUES)
            
        elif opcao == "e":
            u.exibir_extrato(saldo, extrato= extrato)
        
        elif opcao == "c":
            u.cadastrar_usuario()

        elif opcao == "f":
            contas, contador_de_contas= u.criar_conta(contador_de_contas) 
        
        elif opcao == "l":
            u.listar_contas()
        
        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()