import math
class Rectangulo:

    def __init__(self, punto1, punto2, punto3, punto4):
            self.esquina1= punto1
            self.esquina2= punto2
            self.esquina3= punto3
            self.esquina4= punto4
    
    def perimetro(self):
          distancia_horizontal= math.sqrt((self.esquina4.coordenada_x-self.esquina1.coordenada_x)**2+(self.esquina4.coordenada_y-self.esquina1.coordenada_y)**2)
          distancia_vertical= math.sqrt((self.esquina3.coordenada_x-self.esquina1.coordenada_x)**2+(self.esquina3.coordenada_y-self.esquina1.coordenada_y)**2)
          perimetro= (distancia_horizontal*2)+(distancia_vertical*2)
          return perimetro
    
    def area(self):
            distancia_horizontal= math.sqrt((self.esquina4.coordenada_x-self.esquina1.coordenada_x)**2+(self.esquina4.coordenada_y-self.esquina1.coordenada_y)**2)
            distancia_vertical= math.sqrt((self.esquina3.coordenada_x-self.esquina1.coordenada_x)**2+(self.esquina3.coordenada_y-self.esquina1.coordenada_y)**2)
            area= distancia_horizontal* distancia_vertical
            return area
    
    def cuadrado(self):
        distancia_horizontal= math.sqrt((self.esquina4.coordenada_x-self.esquina1.coordenada_x)**2+(self.esquina4.coordenada_y-self.esquina1.coordenada_y)**2)
        distancia_vertical= math.sqrt((self.esquina3.coordenada_x-self.esquina1.coordenada_x)**2+(self.esquina3.coordenada_y-self.esquina1.coordenada_y)**2)

        if distancia_vertical== distancia_horizontal:
             print("Es un cuadrado")
        else:
              print("No es un cuadrado")
              
                


class Puntos:
    def __init__(self, coordenada_x, coordenada_y):
          self.coordenada_x= coordenada_x
          self.coordenada_y= coordenada_y
    
punto1= Puntos(4,4)
punto2= Puntos(16,6)
punto3= Puntos(4,6)
punto4= Puntos(16,4)

rectangulo= Rectangulo(punto1, punto2, punto3, punto4)

print("el perimetro equivale a", rectangulo.perimetro())
print("el area vale", rectangulo.area())
print(rectangulo.cuadrado())