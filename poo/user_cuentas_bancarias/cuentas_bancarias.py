class CuentaBancaria:
    
    def __init__(self, tasa_interes, balance = 0):
        self.tasa_interes = tasa_interes
        self.balance = balance

    def __str__(self):
        return f"{self.balance}"

    def deposito(self, deposito):
        self.balance += deposito
        
    def retiro(self, retiro):
        self.balance -= retiro
    
    def mostrar_info(self):
        print("\nMostrar_balance:")
        print("------------------") 
        for k,v in self.cuenta.items():
            print(f"{k}: {v}")
    
    def generar_interes(self):
        if (self.balance > 0):
            self.balance = self.balance + (self.balance * self.tasa_interes)
            return self
    

