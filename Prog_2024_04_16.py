print()

import Prog_20240416_fg

"""
Hozzunk  létre egy  sorból álló és 8 oszlopból álló, véletlenszerűen 0-ákat és
1-eket tartalmazó mátrixot. Írjunk programot(függvényt használjunk hozzá):
amelyik megmondja, hogy melyik sorban van a legtöbb 1-es
"""

"""
mátrix = Prog_20240416_fg.létrehoz(5, 8, 0, 1)
# print(mátrix)

maxÉrték = Prog_20240416_fg.egyesekSzáma(mátrix[0])
maxHely = 0

i = 1
while i < len(mátrix):
    t = Prog_20240416_fg.egyesekSzáma(mátrix[i])
    if t > maxÉrték:
        maxÉrték = t
        maxHely = i
    i += 1
print(f"\nlegtöbb 1-es: {maxHely + 1}.sor ({maxÉrték} db)")
"""

"""
1.feladat:
írjunk függvényt, amelyik beolvassa a fájl tartalmát egy változóba!
"""

eladások = Prog_20240416_fg.fájlbólBeolvas("Prog_20240416_adat.txt")

""""
2.feladat (HF)
add meg a város sorszámát [1...4]: 7
Hibás adatbevitel! Próbáld újra...
add meg a város sorszámát [1...4]: 2
Kecskemét múlt heti eladásai:
Hétfő: 0db
Kedd: 0db
...
Vasárnap: 13db
"""

while True:
    s = int(input(f"add meg a város sorszámát [1...{len(eladások)}]: "))
    if s >= 1 and s <= len(eladások):
        break
    print("Hibás adatbevitel! Próbáld újra...")

Prog_20240416_fg.kiír(eladások[s - 1])