import math
class Circulo:
    def __init__(self,centro,radio):
        self.centro = centro
        self.radio = radio
        print (centro)
        print (radio)
    
    def area(self):
        return math.pi * (self.radio**2)
    
    def perimetro (self):
        diametro= self.radio*2
        perimetro= diametro * math.pi
        return perimetro 
    
    def punto_circulo (self):
        distancia= math.sqrt((Puntos.coordenada_x- self.centro.coordenada_x)**2+(Puntos.coordenada_y-self.centro.coordenada_y)**2)
        if distancia <= self.radio:
            print("El punto pertenece a la circunferencia")
        else:
            print("El punto no pertenece a la circunferencia")

class Puntos:
    def __init__(self, coordenada_x, coordenada_y):
        self.coordenada_x = coordenada_x
        self.coordenada_y = coordenada_y

centro= Puntos(0,0)
radio = 4
circunferencia= Circulo(centro, radio)
punto1= Puntos(4,6)
punto2= Puntos(2,4)
print("El area del circulo es", circunferencia.area())
print("El perimetro del circulo es", circunferencia.perimetro())