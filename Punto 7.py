n : int = 1
mult : int 
while n>=1 and n<=9 :
  for i in range (1,11):
    mult = i*n
    print(f"{n}x{i} = {mult}")
  n+=1
  if n == 10 :break
  print(f"Tabla del {n}: ")