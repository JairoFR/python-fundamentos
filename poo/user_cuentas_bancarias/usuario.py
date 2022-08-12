class Usuario:

    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.balance_cuenta = 0

    def __str__(self):
        return f"{self.nombre} - {self.email}"

    def hacer_deposito(self, deposito): #toma un arguemento deposito, que es el deposito a realizar
        self.balance_cuenta += deposito # el balance_cuenta aumenta de acuerdo al deposito recibido
        return self

    def hacer_retiro(self, retiro): #toma un argumento
        self.balance_cuenta -= retiro
        return self
    
    def mostrar_balance(self):
        print(f"Balance: {self.nombre}\n{self.balance_cuenta}")
    

jairo = Usuario("jairo", "jfr.elec@gmail.com")
karla = Usuario("Karla", "karla@gmail.com")
lucas = Usuario("Lucas", "lucas@gmail.com")

jairo.hacer_deposito(100).hacer_deposito(200).hacer_deposito(500).hacer_retiro(400).mostrar_balance()
karla.hacer_deposito(100).hacer_deposito(200).hacer_retiro(100).hacer_retiro(100).mostrar_balance()
lucas.hacer_deposito(100).hacer_retiro(20).hacer_retiro(10).hacer_retiro(40).mostrar_balance()
print(jairo)
print(karla)