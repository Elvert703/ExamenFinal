# -*- coding: cp1252 -*-
#
#   la clase automovil version mas inteligente
#
#   atributos:
#     self.gasolina: cantidad de gasolina en el tanque
#     self.prendido: indica si se le dio starter
#     self.odometro: indica la distancia recorrida por el automovil
#
#   metodos:
#      arrancar(self): arranca el vehículo
#           precondiciones: debe tener gasolina para arrancarse
#
#      conducir (self,distancia): se mueve la distancia indicada
#           precondiciones: debe estar prendido
#           postcondiciones: se mueve la distancia solicitada, si
#                     tiene suficiente gasolina. Si no, solo se
#                     mueve la distancia que alcance con la gasolina
#


class Automovil(object):
    """Abstraccion de los objetos automovil."""
    def __init__(self, gasolina):
        self.gasolina = gasolina #la cantidad de gasolina inicial
        self.prendido = False  #se inicia con el carro apagado
        self.odometro = 0  #no ha recorrido ninguna distancia
        print "Tenemos", self.gasolina, "litros"
        
    def arrancar(self):
        if self.gasolina > 0:
            self.prendido = True #se arranca el carro
            print "Arranca"
        else:
            print "No arranca"
            
    def conducir(self,distancia):
        if not self.prendido:
            print "No se mueve, esta apagado"
            return
        
        if distancia <= self.gasolina:     #hay gasolina suficiente
            self.gasolina = self.gasolina - distancia #se consume la gasolina
            self.odometro += distancia #se recorre la distancia
        else:
            self.odometro += self.gasolina #se mueve solo lo que permite
                                               #la gasolina que tenemos
            self.gasolina = 0               #y se termina la gasolina
            
        if self.gasolina == 0:          #si ya no hay gasolina
            self.prendido = False       #se apaga el carro
        
       
#
#
#

miCarro = Automovil(10) #con 10 galones iniciales

miCarro.arrancar()
distancia = 6  #distancia a recorrer

for i in range(3):
    miCarro.conducir(distancia)  #conducir el carro
    print "nos quedan ", miCarro.gasolina, "litros"

#se falsean los datos
miCarro.odometro = 2
print "se recorrio: ",miCarro.odometro, " kilometros"
