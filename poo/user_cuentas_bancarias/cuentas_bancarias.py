class CuentasBancarias:
    
    def __init__(self, tasa_interes, balance = 0):
        self.tasa_interes = tasa_interes
        self.balance = balance
    

    def __str__(self):
        return f"{self.balance}"
    def deposito(self, deposito):
        self.balance += deposito
        return self
    
    def retiro(self, retiro):
        if self.tiene_cash(self.balance, retiro):
            self.balance -= retiro
        else:
            print("Fondos insuicientes")
        return self
    
    def mostrar_info(self):
        print(f"Balance: {self.balance}")   
        return self
    
    def generar_interes(self):
        if (self.balance > 0):
            self.balance = self.balance + (self.balance * self.tasa_interes)
            return self
    
    @staticmethod
    def tiene_cash(balance, monto):
        if (balance - monto <= 0):
            return False
        else:
            return True

cuenta1 = CuentasBancarias(0.01, 100)
cuenta2 = CuentasBancarias(0.01, 200)

cuenta1.deposito(100).deposito(100).deposito(100).retiro(50).generar_interes().mostrar_info()
cuenta2.deposito(100).deposito(500).retiro(50).retiro(10).retiro(10).retiro(10).generar_interes().mostrar_info()
