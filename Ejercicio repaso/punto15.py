palabra= input("Ingrese la palabra")
inversa= "".join(reversed(palabra))
if palabra == inversa:
    print("La palabra es palindrome")
else:
    print("La palabra no es palindrome")