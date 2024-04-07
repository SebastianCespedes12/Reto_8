import math
x : float = float(input("Numero real x: "))
n : int = int(input("n terminos de la serie: "))
aprox : float = 0

def Factorial (a):
  factorial : int = 1
  while a > 1 :
    factorial *= a	
    a-=1
  return factorial

for i in range (0,n+1):
  a=2*i+1
  aprox += ((-1) ** i) * (x **a) / (Factorial(a))

print(aprox)
print(math.sin(math.radians(x)))