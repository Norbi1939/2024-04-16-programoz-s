# Függvények

def létrehoz(sor, oszlop, alsó, felső):
    import random
    lst = []
    i = 1
    while i <= sor:
        j = 1
        belső = []
        while j <= oszlop:
            belső.append(random.randint(alsó, felső))
            j + 1
        lst.append(belső)
        i += 1
    return lst

def egyesekSzáma(sor):
    db = 0
    for e in sor:
        if e == 1:
            db += 1
    return db 

def fájlbólBeolvas(fájlnév):
    lst = []
    f = open(fájlnév, "r", encoding="UTF-8")
    for sor in f:
        lst.append(sor.replace("\n", "").strip().split())
        f.close()
        i = 0
        while i < len(lst):
            j = 1
            while j < len(lst[i]):
                lst[i][i] = int(lst[i][j])
                j += 1
            i += 1
        return lst
    
def kiír():
    pass