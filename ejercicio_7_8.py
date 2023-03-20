class Cuenta:
   
    def __init__(self, titular, cantidad):
        self.titular = titular
        self.cantidad = cantidad

    def setTitular(self, titular):
        self.titular = titular
    
    def setCantidad(self, cantidad):
        self.cantidad = cantidad
    
    def getTitular(self):
        return self.titular
    
    def getCantidad(self):
        return self.cantidad

    def mostrar(self):
        print('El titular de la cuenta es: ' + self.titular)
        print(self.cantidad)

    
    def ingresar(self, ingresar):
        if ingresar > 0 :
            print(ingresar)
        else:
            return 0

    def retirar(self):
        saldoNegativo = 67
        print(self.cantidad - saldoNegativo)
        

cantidadFloat = 4000.0
cantidadFloat1 = float(cantidadFloat)

cantidadIngresar = 150
cantidadIngresar1 = float(cantidadIngresar)

cuenta1 = Cuenta('Ana',cantidadFloat1)
cuenta1.mostrar()
cuenta1.ingresar(cantidadIngresar1)
cuenta1.retirar()


class CuentaJoven(Cuenta):
    def __init__(self,edad, bonificacion):
        self.edad = edad
        self.bonificacion = bonificacion
        

    def setEdad(self,edad):
        self.edad = edad
    
    def getEdad(self):
        return self.edad
    
    def setBonificacion(self,bonificacion):
        self.bonificacion = bonificacion
    
    def getBonificacion(self):
        return self.bonificacion
    
    def es_titular_valido(self):
        if self.edad > 25 and self.edad > 18:
            return True
        else:
            return False
    
    def retirada_dinero(self):       
        if self.edad < 25 and self.edad > 18:
            print(self.bonificacion - 15)            
    
    def mostrar(self):
        print('Cuenta joven')
        print(self.bonificacion)


edadCliente = 23
edadCliente1 = int(edadCliente)

bonificacionCliente = 300
bonificacionCliente1 = float(bonificacionCliente)

cuenta2 = CuentaJoven(edadCliente1,bonificacionCliente1)
cuenta2.es_titular_valido()
cuenta2.retirada_dinero()
cuenta2.mostrar()

    
 