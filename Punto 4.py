n : int =int(input("Ingrese numero: "))
factorial : int = 1
for i in range (1,n+1):
    factorial *= i	
    print(f"el factorial de: {i} es {factorial}")