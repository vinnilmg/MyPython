import math
 
a = 5
b = 8
c = 1
 
delta = b * b - 4 * a * c
 
if delta < 0:
    print ("A equação não possui raizes reais")
elif delta == 0:
    raiz = (-1 * b + math.sqrt(delta)) / (2 * a)
    print ("A raiz da equação é: ",raiz)
else:
    raiz1 = (-1 * b + math.sqrt(delta)) / (2 * a)
    raiz2 = (-1 * b - math.sqrt(delta)) / (2 * a)  
    print(raiz1, raiz2) 