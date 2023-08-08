def CrearMatriz(M,F,C):
    import random
    for f in range(F):
        for c in range(C):
            M[f][c] = random.randint(1,100)
            print(M[f][c], end="\t")
        print("\n")
    return

def main():
    matriz=[]
    filas = 2
    columnas = 2
    for i in range(filas):
        matriz.append([0]*columnas)
    CrearMatriz(matriz, filas, columnas)
main()
