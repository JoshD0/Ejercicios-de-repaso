import random
for i in range (0,100):
    numero=random.randint(0,100)
    for n in range (i):
        if numero%2==0:
            print(numero)