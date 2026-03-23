class conta_bancaria:
    def __init__(self,saque = 0, saldo = 0,titular = "sem titular"):
        self.saldo = saldo
        self.deposito = []
        self.saque = saque
        self.titular = titular
        self.historico_deposito = []
        self.historico_saque = []
    def inserir_saque(self,saque):
        self.saque.append(saque)
        print(f"{self.saque} sacado da conta")
    
    def inserir_deposito(self,deposito):
        self.deposito.append(deposito)
        print(f"{deposito} depositado na conta")
    def mostrar_historico_saque(self):
        print("Histórico de saques: ")
        for saque in self.historico_saque:
            print(saque)
    def mostrar_historico_deposito(self):
        print("Histórico de depositos: ")
        for deposito in self.historico_deposito:
            print(deposito)