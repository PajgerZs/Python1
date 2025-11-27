#1 Kérj be két számot, és írd ki az összegüket.
szam1 = float(input("Kérek egy számot: "))
szam2 = float(input("Kérek még egy számot: "))
print(szam1 + szam2)

#2 Kérj be egy számot, és döntsd el, hogy páros-e.
szam = int(input("Adj meg egy számot: "))
if szam % 2 == 0:
    print("A szám páros.")
else:
    print("A szám páratlan.")

#3 Kérj be három számot, és írd ki melyik a legnagyobb.
szam1 = int(input("Kérem az első számot: "))
szam2 = int(input("Kérem a második számot: "))
szam3 = int(input("Kérem a harmadik számot: "))
legnagyobb = szam1
if szam2 > legnagyobb:
    legnagyobb = szam2
if szam3 > legnagyobb:
    legnagyobb = szam3

print("A legnagyobb szám: ", legnagyobb)