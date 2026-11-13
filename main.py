import random
while True:    
    val = ["äpple", "banan", "cykel", "dator", "elefant", "fönster", "gitarr", "hundvalp", "isbjörn", "jordgubbe", "kaktus", "lampa", "morgon", "nyckel", "osthyvel", "papegoja", "ryggsäck", "sköldpadda", "telefon", "utomjording", "vattenfall", "xylofon", "yoghurt", "zebra", "åkattraktion", "överraskning", "blåbär", "choklad", "drake", "ekorre", "fjäril", "glassbåt", "hammare", "igelkott", "jacka", "kudde", "lejon", "måne", "nätverk", "ormbunke", "penguin", "regnbåge", "snögubbe", "tandborste", "uggla", "vinter", "äventyr", "öken", "ambulans", "bibliotek", "cirkus", "delfin", "eldstad", "fotboll", "gräsklippare", "helikopter", "ishockey", "järnväg", "kanelbulle", "lastbil", "mikrovågsugn", "nyckelpiga", "orkester", "pannkaka", "raket", "simhall", "tågstation", "universum", "vulkan", "åskväder", "ögonbryn", "apelsin", "blomma", "citron", "diamant", "ficklampa", "groda", "jordklot", "kamera", "lustgård", "madrass", "pussel", "sjukhus", "trädgård", "verktyg", "älgko", "fängelse", "guldmynt", "hjärta", "kaffekopp", "lägenhet", "människa", "paraply", "skattkista", "teater", "vetenskap", "ansikte", "bergstopp", "födelsedag", "sommarlov"]
    spelarval = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "å", "ä", "ö"]
    spelarval_ny = spelarval.copy()

    datorval = random.choice(val)
    datorval_bokstav = list(datorval)
    ord_fyllt = ["*"] * len(datorval)

    felkvar = 10
    felgisningar = []

    print(f"Du ska gissa ett ord, bokstav för bokstav, på {len(datorval)} bokstäver.")

    while felkvar != 0:
        while True:
            spelarensval = input("\nAnge en gisning ->").lower()
        
            if spelarensval in spelarval:
                break  
            elif spelarensval in spelarval_ny:
                print("Du har redan gissat på den bokstaven, välj en annan.")
            else:
                print("ogiltig gisning")
        spelarval.remove(spelarensval)
        if spelarensval in datorval:
            print(f"\nDu gissade rätt på bokstaven {spelarensval}")
            for i in range(len(datorval)):
                if datorval[i] == spelarensval:
                    ord_fyllt[i] = spelarensval
        

        else:
            print(f"\nDu gissade fel på bokstaven {spelarensval}")
            felgisningar.append(spelarensval)
            felkvar -= 1
        print(f"Du har nu {felkvar} st. felgisningar kvar")
        print(f"Felgissningar: {' '.join(felgisningar)}")
        print(f"Rätt gissade bokstäver: {' '.join(ord_fyllt)}")
        if ord_fyllt == datorval_bokstav:
            print(f"Grattis! Du gissade rätt på ordet {datorval}")
            break
        elif felkvar == 0:
            print(f"Tyvärr, du har inga gissningar kvar. Ordet var {datorval}")
    igen = input("\nVill du spela en gång till? j/n ->").lower()
    if igen == "n":
        break
    elif igen == "j":
        continue

print("program avslutas")
