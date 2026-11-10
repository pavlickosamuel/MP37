with open("hlasovanie_1.txt", "r") as fr:
    sms = [r.strip() for r in fr if r.strip()]

print("Celkový počet SMS:", len(sms))

poradia = {str(c): [] for c in range(5220, 5230)}

for poradie, cislo in enumerate(sms, start=1):
    if cislo in poradia:
        poradia[cislo].append(poradie)

for cislo, zoznam in poradia.items():
    with open(f"{cislo}.txt", "w") as fw:
        for p in zoznam:
            fw.write(f"{p}\n")