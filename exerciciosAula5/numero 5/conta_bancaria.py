class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, deposito):
        self.saldo += deposito
        print(f'Depósito realizado com sucesso!')

    def sacar(self, saque):
        if saque > self.saldo:
            print(f'saldo insuficiente!')
        else:
            self.saldo -= saque
            return print(f'Saque realizado com sucesso!')

    def info(self):
        print(f'Nome: {self.titular} \nSaldo: {self.saldo}\n')
