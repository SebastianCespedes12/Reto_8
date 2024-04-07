import math
x : float = float(input("Numero real x: "))
n : int = int(input("n terminos de la serie: "))
aprox : float = 0


for i in range (0,n+1):
  a=2*i+1
  aprox += ((-1) ** i) * ((x **a) / a)

print(aprox)
print(math.sin(math.radians(x)))