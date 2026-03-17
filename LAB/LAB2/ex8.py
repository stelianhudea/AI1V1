lista = [
	{"Tara": "Ro", "Valoare max": 5000},
	{"Tara": "Coreea N", "Valoare max": 0},
	{"Tara": "IT", "Valoare max": 15000},
	{"Tara": "D", "Valoare max": 20000},
]
a = input("Tara: ")
b = int(input("Suma: "))
gasit = False
for tara in lista:
    if tara["Tara"] == a:
        gasit = True
        if b <= tara["Valoare max"]:
            print("Sigură")
        else:
            print("Suspicioasa sau frauduloase")

if not gasit:
    print("Tara nu exista")