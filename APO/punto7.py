class Cuenta:
    def __init__(self, numero_cuenta, titular, dinero):
        self.numero_cuenta= numero_cuenta
        self.titular= titular
        self.dinero= dinero

    def depositar (self,dinero):
        if dinero>0:
            self.dinero= dinero
            print("Se ha realizado el deposito de ", dinero, "con exito")
        else:
            print("No es posible realizar el deposito")
    
    def retiro (self, retiro):
        if retiro> 0:
            self.dinero -= retiro
            print ("La operacion se ha realizado con exito")
        else:
            print("No se puede realizar el retiro, la cantidad seleccionada no es valida")
    
    def cuota_manejo (self):
        self.dinero -= self.dinero*0.02
        print("La cuota de manejo correspondiente ha sido descontada de su cuenta")

    def detalles (self):
        print("El numero de cuenta es", self.numero_cuenta)
        print ("El titular de la tarjeta es", self.titular )
        print ("El dinero con el que cuenta actualmente la tarjeta es de", self.dinero)

cuenta = Cuenta(27963,["Alberto", "Juan"],0)

print("El monto actual de la cuenta es:", cuenta.dinero)
cuenta.depositar(9000)
print("El monto actual de la cuenta es", cuenta.dinero)

cuenta.retiro(1000)
print("El monto actual de la cuenta es:", cuenta.dinero)

cuenta.cuota_manejo()

cuenta.detalles()
