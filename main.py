import random
val = ["äpple", "banan", "cykel", "dator", "elefant", "fönster", "gitarr", "hundvalp", "isbjörn", "jordgubbe", "kaktus", "lampa", "morgon", "nyckel", "osthyvel", "papegoja", "ryggsäck", "sköldpadda", "telefon", "utomjording", "vattenfall", "xylofon", "yoghurt", "zebra", "åkattraktion", "överraskning", "blåbär", "choklad", "drake", "ekorre", "fjäril", "glassbåt", "hammare", "igelkott", "jacka", "kudde", "lejon", "måne", "nätverk", "ormbunke", "penguin", "regnbåge", "snögubbe", "tandborste", "uggla", "vinter", "äventyr", "öken", "ambulans", "bibliotek", "cirkus", "delfin", "eldstad", "fotboll", "gräsklippare", "helikopter", "ishockey", "järnväg", "kanelbulle", "lastbil", "mikrovågsugn", "nyckelpiga", "orkester", "pannkaka", "raket", "simhall", "tågstation", "universum", "vulkan", "åskväder", "ögonbryn", "apelsin", "blomma", "citron", "diamant", "ficklampa", "groda", "jordklot", "kamera", "lustgård", "madrass", "pussel", "sjukhus", "trädgård", "verktyg", "älgko", "fängelse", "guldmynt", "hjärta", "kaffekopp", "lägenhet", "människa", "paraply", "skattkista", "teater", "vetenskap", "ansikte", "bergstopp", "födelsedag", "sommarlov"]
spelarval = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j" "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "å", "ä", "ö"]
datorval = random.choice(val)
print(f"Du ska gissa ett ord, bokstav för bokstav, på {len(datorval)} bokstäver.")
felkvar = 10
felgisningar = []
while True:
    while True:
        spelarensval = input("Ange en gisning ->").lower()
        
        if spelarensval in spelarval:
            break  
        print("ogiltig gisning")
    felgisningar.append(spelarensval)
    print(f"Du har nu {felkvar} st. felgisningar kvar")
    print(f"Du har gissat på: {felgisningar}")


