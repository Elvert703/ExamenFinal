





class Automovil(object):
    """Abstraccion de los objetos automovil."""
    def __init__(self, gasolina):
        self.gasolina = gasolina
        print "Tenemos", self.gasolina, "litros"
        
    def arrancar(self):
        if self.gasolina > 0:
            print "Arranca"
        else:
            print "No arranca"
            
    def conducir(self):
        if self.gasolina > 0:
            self.gasolina -= 1
            print "Quedan", self.gasolina, "litros"
        else:
            print "No se mueve, se termino gasolina"


#
#
#

miCarro = Automovil(2) #con 10 galones iniciales
carrodeArmando = Automovil(5)
carrodePaola = Automovil(4)

miCarro.arrancar()
carrodeArmando.arrancar()
carrodePaola.arrancar()

for i in range(3):
    miCarro.conducir()  #conducir el carro
    carrodeArmando.conducir()
    carrodePaola.conducir()


