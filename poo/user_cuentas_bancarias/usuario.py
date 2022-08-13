import cuentas_bancarias as cb

class Usuario:

    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.cuenta = {
                        "cuenta_corriente" : cb.CuentaBancaria(0.02, 1000),
                        "cuenta_ahorro" : cb.CuentaBancaria(0.02, 2000) 
                        }

    def __repr__(self):
        return f"{self.nombre} - {self.email}"

    def hacer_deposito(self, deposito, account): #toma un argumento deposito, y una account que puede ser "cuenta_corriente" o "cuenta_ahorro"
        self.cuenta[account].deposito(deposito)# se llama a los metodos de instancias de la clase CuentaBancaria
        return self
        

    def hacer_retiro(self, retiro, account): 
        if Usuario.tiene_cash(self.cuenta[account].balance, retiro): # valida con el metodo estatico si tiene cash para retirar dinero.  self.cuenta[account].balance -> accede al atributo balance de CuentaBancaria
            self.cuenta[account].retiro(retiro) # llama a los metodos de CuentaBancaria y retira cash de la cuenta seleccionada
        else:
            print("\n-----Fondos insuficientes para realizar retiro-----\n")
        return self
    
    
    def transferir_dinero(self, monto, usuario):
    
        if Usuario.tiene_cash(self.cuenta["cuenta_corriente"].balance, monto):

            self.cuenta["cuenta_corriente"].retiro(monto)
            usuario.cuenta["cuenta_corriente"].deposito(monto)
        else:
            print("\n-----Saldo insuficiente-----")
        self.mostrar_balance()
    
    def mostrar_balance(self):
        print(f"\nMostrar_balance: {self.nombre}")
        print("------------------") 
        for cuenta, balance in self.cuenta.items(): #itera sobre el diccionario de self.cuentas para mostrar las llaves "cuenta_corriente" y "cuenta_ahorro" y los balance como valores
            print(f"{cuenta}: $ {balance}")
        print("\n########################################")
        return self
        
    
    def interes(self, account):
        self.cuenta[account].generar_interes()
        return self
        
    @staticmethod
    def tiene_cash(balance, monto): # metodo estatico que valida si el retiro o transferencia a realizar tiene fondos suficientes
        if (balance - monto < 0):
            return False
        else:
            return True

jairo = Usuario("jairo", "jfr.elec@gmail.com")
karla = Usuario("Karla", "karla@gmail.com")
lucas = Usuario("Lucas", "lucas@gmail.com")

jairo.mostrar_balance().hacer_deposito(100, "cuenta_corriente").hacer_deposito(100, "cuenta_corriente").hacer_deposito(10000, "cuenta_corriente").hacer_retiro(100, "cuenta_ahorro").mostrar_balance()
karla.mostrar_balance().hacer_deposito(500, "cuenta_corriente").hacer_deposito(9000, "cuenta_corriente").hacer_deposito(100, "cuenta_corriente").hacer_retiro(100, "cuenta_ahorro").mostrar_balance()
lucas.mostrar_balance().hacer_deposito(2000, "cuenta_corriente").hacer_deposito(100, "cuenta_corriente").hacer_deposito(100, "cuenta_corriente").hacer_retiro(100, "cuenta_ahorro").mostrar_balance()
cb.CuentaBancaria.numeros_cuentas()