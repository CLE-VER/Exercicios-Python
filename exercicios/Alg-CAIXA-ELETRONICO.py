class CaixaEletronico:
    def __init__(self):
        self.saldo = 0.0
        self.depositos = []
        self.saques = []
        self.saques_diarios = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.depositos.append(valor)
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido. Tente novamente.")

    def sacar(self, valor):
        if self.saques_diarios >= 3:
            print("Limite diário de saques atingido.")
        elif valor > 500:
            print("O valor máximo para saque é de R$500.00.")
        elif valor > self.saldo:
            print("Saldo insuficiente para realizar o saque.")
        else:
            self.saldo -= valor
            self.saques.append(valor)
            self.saques_diarios += 1
            print(f"Saque de R${valor:.2f} realizado com sucesso.")

    def extrato(self):
        if not self.depositos and not self.saques:
            print("Movimentações não foram realizadas até o momento.")
        else:
            print("Extrato:")
            for deposito in self.depositos:
                print(f"Depósito: R${deposito:.2f}")
            for saque in self.saques:
                print(f"Saque: R${saque:.2f}")
            print(f"Saldo atual: R${self.saldo:.2f}")

    def menu(self):
        while True:
            print("\nMenu:")
            print("1. Depositar")
            print("2. Sacar")
            print("3. Extrato")
            print("4. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                valor = float(input("Digite o valor para depósito: R$"))
                self.depositar(valor)
            elif opcao == '2':
                valor = float(input("Digite o valor para saque: R$"))
                self.sacar(valor)
            elif opcao == '3':
                self.extrato()
            elif opcao == '4':
                print("Obrigado por usar o caixa eletrônico!")
                break
            else:
                print("Opção inválida. Tente novamente.")
caixa = CaixaEletronico()
caixa.menu()
