import random
e_lupte = [
    {"Mobs": "Lup +1", "Atac": 10, "Aparare": 120},
    {"Mobs": "Lup +3", "Atac": 18, "Aparare": 200},
    {"Mobs": "Lup +5", "Atac": 25, "Aparare": 300},
    {"Mobs": "Urs +0", "Atac": 15, "Aparare": 250},
    {"Mobs": "Urs +3", "Atac": 35, "Aparare": 450},
    {"Mobs": "Urs +7", "Atac": 60, "Aparare": 700},
    {"Mobs": "Slime +1", "Atac": 5, "Aparare": 80},
    {"Mobs": "Slime +5", "Atac": 20, "Aparare": 150},
    {"Mobs": "Slime +9", "Atac": 30, "Aparare": 200},
    {"Mobs": "Goblin +1", "Atac": 22, "Aparare": 210},
    {"Mobs": "Goblin +4", "Atac": 40, "Aparare": 350},
    {"Mobs": "Goblin +8", "Atac": 65, "Aparare": 600},
    {"Mobs": "Schelet +0", "Atac": 28, "Aparare": 220},
    {"Mobs": "Schelet +5", "Atac": 55, "Aparare": 500},
    {"Mobs": "Schelet +9", "Atac": 90, "Aparare": 900},
    {"Mobs": "Orc +2", "Atac": 70, "Aparare": 850},
    {"Mobs": "Orc +6", "Atac": 120, "Aparare": 1300},
    {"Mobs": "Orc +10", "Atac": 180, "Aparare": 2000},
    {"Mobs": "Trol +1", "Atac": 150, "Aparare": 1800},
    {"Mobs": "Trol +5", "Atac": 220, "Aparare": 2500},
    {"Mobs": "Trol +9", "Atac": 300, "Aparare": 3500},
    {"Mobs": "Dragon mic", "Atac": 350, "Aparare": 4000},
    {"Mobs": "Dragon rosu", "Atac": 500, "Aparare": 6000},
    {"Mobs": "Dragon antic", "Atac": 750, "Aparare": 9000},
    {"Mobs": "Fenrir +1", "Atac": 200, "Aparare": 5000},
    {"Mobs": "Fenrir +5", "Atac": 350, "Aparare": 7500},
    {"Mobs": "Fenrir +9", "Atac": 500, "Aparare": 10000},
    {"Mobs": "Demon +1", "Atac": 420, "Aparare": 5200},
    {"Mobs": "Demon +6", "Atac": 650, "Aparare": 7800},
    {"Mobs": "Lord Demon", "Atac": 900, "Aparare": 12000}
]
e_inv = [
    {"Obiect": "Sabie +1", "Valoare atac": 5, "Valoare aparare": 1, "clasa": 1, "Tip_obiect": 1},
    {"Obiect": "Sabie +5", "Valoare atac": 10, "Valoare aparare": 3, "clasa": 1, "Tip_obiect": 1},
    {"Obiect": "Sabie +9", "Valoare atac": 20, "Valoare aparare": 5, "clasa": 1, "Tip_obiect": 1},
    {"Obiect": "Sabie legendara", "Valoare atac": 40, "Valoare aparare": 10, "clasa": 1, "Tip_obiect": 1},
    {"Obiect": "Pumnal +1", "Valoare atac": 7, "Valoare aparare": 1, "clasa": 2, "Tip_obiect": 1},
    {"Obiect": "Pumnal +5", "Valoare atac": 15, "Valoare aparare": 3, "clasa": 2, "Tip_obiect": 1},
    {"Obiect": "Pumnal +9", "Valoare atac": 25, "Valoare aparare": 5, "clasa": 2, "Tip_obiect": 1},
    {"Obiect": "Pumnal Umbra", "Valoare atac": 35, "Valoare aparare": 6, "clasa": 2, "Tip_obiect": 1},
    {"Obiect": "Arc +1", "Valoare atac": 8, "Valoare aparare": 1, "clasa": 2, "Tip_obiect": 1},
    {"Obiect": "Arc +5", "Valoare atac": 18, "Valoare aparare": 2, "clasa": 2, "Tip_obiect": 1},
    {"Obiect": "Arc +9", "Valoare atac": 30, "Valoare aparare": 4, "clasa": 2, "Tip_obiect": 1},
    {"Obiect": "Arc Dragon", "Valoare atac": 45, "Valoare aparare": 6, "clasa": 2, "Tip_obiect": 1},
    {"Obiect": "Armura +0", "Valoare atac": 0, "Valoare aparare": 10, "clasa": 1, "Tip_obiect": 2},
    {"Obiect": "Armura +5", "Valoare atac": 0, "Valoare aparare": 25, "clasa": 1, "Tip_obiect": 2},
    {"Obiect": "Armura +9", "Valoare atac": 0, "Valoare aparare": 40, "clasa": 1, "Tip_obiect": 2},
    {"Obiect": "Armura Dragon", "Valoare atac": 5, "Valoare aparare": 60, "clasa": 1, "Tip_obiect": 2},
    {"Obiect": "Roba +1", "Valoare atac": 5, "Valoare aparare": 8, "clasa": 3, "Tip_obiect": 2},
    {"Obiect": "Roba +5", "Valoare atac": 10, "Valoare aparare": 15, "clasa": 3, "Tip_obiect": 2},
    {"Obiect": "Roba +9", "Valoare atac": 15, "Valoare aparare": 25, "clasa": 3, "Tip_obiect": 2},
    {"Obiect": "Roba Arhimag", "Valoare atac": 25, "Valoare aparare": 35, "clasa": 3, "Tip_obiect": 2},
    {"Obiect": "Elixir +0", "Valoare atac": 0, "Valoare aparare": 15, "clasa": 0, "Tip_obiect": 3},
    {"Obiect": "Elixir +1", "Valoare atac": 0, "Valoare aparare": 25, "clasa": 0, "Tip_obiect": 3},
    {"Obiect": "Elixir mare", "Valoare atac": 0, "Valoare aparare": 40, "clasa": 0, "Tip_obiect": 3},
    {"Obiect": "Inel putere", "Valoare atac": 10, "Valoare aparare": 3, "clasa": 0, "Tip_obiect": 4},
    {"Obiect": "Inel titan", "Valoare atac": 20, "Valoare aparare": 5, "clasa": 0, "Tip_obiect": 4},
    {"Obiect": "Amuleta foc", "Valoare atac": 15, "Valoare aparare": 2, "clasa": 0, "Tip_obiect": 4},
    {"Obiect": "Amuleta gheata", "Valoare atac": 15, "Valoare aparare": 5, "clasa": 0, "Tip_obiect": 4},
    {"Obiect": "Colier dragon", "Valoare atac": 30, "Valoare aparare": 10, "clasa": 0, "Tip_obiect": 4},
    {"Obiect": "Talisman antic", "Valoare atac": 35, "Valoare aparare": 12, "clasa": 0, "Tip_obiect": 4},
    {"Obiect": "Piatra magica", "Valoare atac": 20, "Valoare aparare": 20, "clasa": 0, "Tip_obiect": 4}
]
inv = []
pov = 0
print("Clase: Razboinic, Mag, Rogue")
c = random.randint(1, 3)
if c == 1: print("Esti razboinic!")
elif c == 2: print("Esti asasin!")
elif c == 3: print("Esti mag!")
hp = random.randint(100, 12000)
atk = random.randint(10, 900)
print("HP: ", hp," ATAC: ", atk)
print("1 = STANGA | 2 = DREAPTA | 3 = INVENTAR | 4 - EXIT")
while hp > 0:
	a = int(input("Sarcina: "))
	if a == 1:
		ev = random.randint(0, 29)
		r = random.randint(1, 2)
		if r == 2:
			print("Ai primit un / o: ", e_inv[ev])
			if  c == e_inv[ev]["clasa"] or e_inv[ev]["clasa"] == 0:
				inv.append(e_inv[ev])
				hp += e_inv[ev]["Valoare aparare"]
				atk += e_inv[ev]["Valoare atac"]
			else: print("Itm sa spar, incompatibil cu tine")
		elif r == 1: 
			if  e_lupte[ev]["Aparare"] / atk <= hp / e_lupte[ev]["Atac"]:
				print(e_lupte[ev])
				print("Win! ", "HP: ", hp," ATAC: ", atk)
			else: 
				hp = 0
				print("Game over ", "HP: ", hp," ATAC: ", atk)
	elif a == 2:
		ev = random.randint(0, 29)
		r = random.randint(1, 2)
		if r == 2:
			print("Ai primit un / o: ", e_inv[ev])
			if  c == e_inv[ev]["clasa"] or e_inv[ev]["clasa"] == 0:
				inv.append(e_inv[ev])
				hp += e_inv[ev]["Valoare aparare"]
				atk += e_inv[ev]["Valoare atac"]
			else: print("Itm sa spar, incompatibil cu tine")
		elif r == 1: 
			if  e_lupte[ev]["Aparare"] / atk <= hp / e_lupte[ev]["Atac"]:
				print(e_lupte[ev])
				print("Win! ", "HP: ", hp," ATAC: ", atk)
			else: 
				hp = 0
				print("Game over ", "HP: ", hp," ATAC: ", atk)
	elif a == 3:
		print("Inventar: ", inv)
	elif a == 4: 
		hp = 0
		print("Povestea sa terminat!")
