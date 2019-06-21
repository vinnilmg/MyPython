import random

#random.seed(1)
numero = random.randint(0, 10)

print(numero)

try:
	print(2/0)
except:
	print ("BUG")