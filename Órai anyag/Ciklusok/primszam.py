n = int(input("n: "))

for i in range(2, n):
    if n / i >= 1:
        print("nem prímszam")
        exit()
        
print("prímszam")    
    
        