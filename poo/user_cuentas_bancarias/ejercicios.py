from clases import Usuario, CuentaBancaria

jairo = Usuario("jairo", "jfr.elec@gmail.com")
karla = Usuario("Karla", "karla@gmail.com")
lucas = Usuario("Lucas", "lucas@gmail.com")

jairo.mostrar_balance().hacer_deposito(100, "cuenta_corriente").hacer_deposito(100, "cuenta_corriente").hacer_deposito(10000, "cuenta_corriente").hacer_retiro(100, "cuenta_ahorro").mostrar_balance()
karla.mostrar_balance().hacer_deposito(500, "cuenta_corriente").hacer_deposito(9000, "cuenta_corriente").hacer_deposito(100, "cuenta_corriente").hacer_retiro(100, "cuenta_ahorro"  ).mostrar_balance()
lucas.mostrar_balance().hacer_deposito(2000, "cuenta_corriente").hacer_deposito(100, "cuenta_corriente").hacer_deposito(100, "cuenta_corriente").hacer_retiro(100, "cuenta_ahorro").mostrar_balance()
CuentaBancaria.numeros_cuentas()