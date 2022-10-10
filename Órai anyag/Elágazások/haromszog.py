a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if a + b > c and c + b > a and a + c > b:
    print("Szerkesztheto!")
else:
    print("Nem szerkesztheto!")    