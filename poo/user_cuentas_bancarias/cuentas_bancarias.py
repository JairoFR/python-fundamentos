class CuentaBancaria:
    total_cuentas = 0

    def __init__(self, tasa_interes, balance = 0):
        self.tasa_interes = tasa_interes
        self.balance = balance
        CuentaBancaria.total_cuentas += 1

    def __str__(self):
        return f"{self.balance}"

    def deposito(self, deposito):
        self.balance += deposito
        print("\n-----Deposito realizado con exito------\n")

    def retiro(self, retiro):
        self.balance -= retiro
        print("------Giro realizado con exito---------")
    
    def generar_interes(self):
        if (self.balance > 0):
            self.balance = self.balance + (self.balance * self.tasa_interes)
            return self
    
    @classmethod
    def numeros_cuentas(cls):
        print(f"{cls.total_cuentas} cuentas creadas")







