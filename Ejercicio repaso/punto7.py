numeros=[60,3,5,8,78,6,1,700,10]
menor=10000
mayor=0
for i in range (len(numeros)):
    if menor>numeros[i]:
        menor=numeros[i]
print("El número menor es",menor)
for n in range (len(numeros)):
    if mayor<numeros[n]:
        mayor=numeros[n]
print("El número mayor es", mayor)