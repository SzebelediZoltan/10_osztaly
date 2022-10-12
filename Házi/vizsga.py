#Irasbeli
irasbeli1= int(input("Az első írásbeli pontok: "))
irasbeli2 = int(input("A második írásbeli pontok: "))
irasbeli3 = int(input("A harmadik írásbeli pontok: "))

#Szobeli
szobeli = int(input("Az első szóbeli pontok: "))

#Számolás/Kiírás

if irasbeli1 > irasbeli2:
    maxi = irasbeli1
elif irasbeli3 > irasbeli2:
    maxi = irasbeli3
else:
    maxi = irasbeli2 

egybe = szobeli + maxi

if maxi / 50 * 100 > 80:
    if egybe / 100 * 100 > 60:
        print("Átment")
    else:
        print("Bukott")
else:
    print("Bukott")