#1 Kérj be két számot, és írd ki az összegüket.
szam1 = int(input("Kérek egy egész számot: "))
szam2 = int(input("Kérek még egy egész számot: "))
print(szam1 + szam2)

#2 Kérj be egy számot, és döntsd el, hogy páros-e.
szam = int(input("Adj meg egy számot: "))
if szam % 2 == 0:
    print("A szám páros.")
else:
    print("A szám páratlan.")