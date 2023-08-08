def factorial(num):
    factorial= num
    for i in range (num-1,0,-1):
        factorial*= i
    return factorial
print (factorial(8))