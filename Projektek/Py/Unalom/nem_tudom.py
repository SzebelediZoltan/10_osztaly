lista = []

while True:
    x = float(input())
    if x > 0:
        lista.append(x)
    else:
        break
    

print(lista[::-1])

        