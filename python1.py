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

#4 Kérj be egy N értéket, majd írd ki 1-től N-ig a számokat egy ciklussal.
N = int(input("Kérem az N értékét: "))
for i in range(1, N + 1):
    print(i)

#5 Kérj be egy N számot, majd számold ki a közötti számok összegét.
N = int(input("Kérem az N értékét: "))
osszeg = 0
for i in range(1, N + 1):
    osszeg += i
print("Az 1 és", N, "közötti számok összege:", osszeg)

#6 Kérj be 5 darab számot, tedd őket listába, majd számold ki az átlagukat.
szamok = []
for i in range(5):
    szam = float(input(f"Kérem a(z) {i+1}. számot: "))
    szamok.append(szam)
atlag = sum(szamok) / len(szamok)
print(atlag)

#7 Adj meg egy listát tetszőleges egész számokkal, majd írd ki: a legnagyobb értéket, a legkisebb értéket
szamok = [1, 2, 3, 4, 5] 
print("A lista:", szamok)
print("Legnagyobb szám:", max(szamok))
print("Legkisebb szám:", min(szamok))

#7.1 Adj meg egy listát tetszőleges egész számokkal, majd írd ki: a legnagyobb értéket, a legkisebb értéket
szamok = []
db = int(input("Hány darab számot szeretnél megadni? "))
for i in range(db):
    szam = int(input(f"Kérem a(z) {i+1}. számot: "))
    szamok.append(szam)
print("Legnagyobb szám:", max(szamok))
print("Legkisebb szám:", min(szamok))

#8 Kérj be egy számot és döntsd el, hogy benne van-e az előre adott listában.
szamok = [1, 2, 3, 4, 5]
keresettSzam = int(input("Kérek egy számot: "))
if keresettSzam in szamok:
    print("Ez a szám benne van a listában.")
else:
    print("Ez a szám nincs benne a listában.")