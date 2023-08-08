import math

class Ejes:
    def __init__(self, eje_x,eje_y):
        self.eje_x= eje_x
        self.eje_y= eje_y

    def mover(self, cambio_x,cambio_y):
        self.eje_x= cambio_x
        self.eje_y= cambio_y
    
    def calcular_distancia(punto1, punto2):
        distancia= math.sqrt((punto2.eje_x-punto1.eje_x)**2+(punto2.eje_y-punto1.eje_y)**2)
        return distancia
   
punto1= Ejes(5,7)
punto2= Ejes(10,15)
coordenada_x= punto1.eje_x
coordenada_y= punto1.eje_y
print("Estas son las coordenadas iniciales", "(", coordenada_x,",", coordenada_y ,")")

punto2.mover(10,15)
coordenada_x= punto2.eje_x 
coordenada_y= punto2.eje_y

print("Estas son las nuevas coordenadas", "(", coordenada_x,"," ,coordenada_y ,")" )


print(Ejes.calcular_distancia(punto1,punto2))

