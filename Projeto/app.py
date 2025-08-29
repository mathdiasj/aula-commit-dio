import random

# Este dicionário irá armazenar as contas.
# A chave será o número da conta e o valor será outro dicionário com 'nome' e 'saldo'.
contas = {}

def gerar_numero_conta():
    """Gera um número de conta de 6 dígitos único."""
    while True:
        numero = random.randint(100000, 999999)
        if numero not in contas:
            return numero

def criar_nova_conta():
    """Cria uma nova conta para o cliente."""
    nome = input("Insira seu nome: ")
    while True:
        try:
            valor_inicial = float(input("Insira o valor inicial da conta: "))
            if valor_inicial >= 0:
                break
            else:
                print("O valor inicial não pode ser negativo. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")
            
    numero_conta = gerar_numero_conta()
    contas[numero_conta] = {'nome': nome, 'saldo': valor_inicial}
    print(f"\nConta criada com sucesso!")
    print(f"Nome do Titular: {nome}")
    print(f"Número da Conta: {numero_conta}")
    print(f"Saldo Inicial: R${valor_inicial:.2f}")

def menu():
    """Exibe o menu de opções."""
    print("\n--- Menu do Banco ---")
    print("1. Ver Saldo")
    print("2. Depositar")
    print("3. Sacar")
    print("4. Sair")
    return input("Escolha uma opção: ")

def encontrar_conta():
    """Solicita o número da conta e verifica se ela existe."""
    try:
        num_conta = int(input("Insira o número da sua conta: "))
        if num_conta in contas:
            return num_conta
        else:
            print("Número de conta não encontrado.")
            return None
    except ValueError:
        print("Entrada inválida. Por favor, insira um número.")
        return None

def ver_saldo():
    """Mostra o saldo da conta."""
    num_conta = encontrar_conta()
    if num_conta:
        saldo_atual = contas[num_conta]['saldo']
        print(f"O saldo da conta {num_conta} é de R${saldo_atual:.2f}")

def depositar():
    """Adiciona um valor à conta."""
    num_conta = encontrar_conta()
    if num_conta:
        try:
            valor = float(input("Insira o valor para depositar: "))
            if valor > 0:
                contas[num_conta]['saldo'] += valor
                print(f"Depósito de R${valor:.2f} realizado com sucesso.")
                print(f"Novo saldo: R${contas[num_conta]['saldo']:.2f}")
            else:
                print("O valor do depósito deve ser positivo.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

def sacar():
    """Retira um valor da conta."""
    num_conta = encontrar_conta()
    if num_conta:
        try:
            valor = float(input("Insira o valor para sacar: "))
            saldo_atual = contas[num_conta]['saldo']
            if valor > 0:
                if valor <= saldo_atual:
                    contas[num_conta]['saldo'] -= valor
                    print(f"Saque de R${valor:.2f} realizado com sucesso.")
                    print(f"Novo saldo: R${contas[num_conta]['saldo']:.2f}")
                else:
                    print("Saldo insuficiente.")
            else:
                print("O valor do saque deve ser positivo.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

# --- Código Principal ---

# Cria uma conta inicial para começar
print("Bem-vindo ao sistema de banco. Vamos criar sua primeira conta!")
criar_nova_conta()

# Loop principal do menu
while True:
    opcao = menu()
    if opcao == '1':
        ver_saldo()
    elif opcao == '2':
        depositar()
    elif opcao == '3':
        sacar()
    elif opcao == '4':
        print("Obrigado por usar nosso banco. Até logo!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção de 1 a 4.")