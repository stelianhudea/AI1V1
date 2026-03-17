import random
print("Bine ai venit la Loteria Python!")
print("Alege 6 numere între 1 și 49.")
v = []
x=0
while x!=6:
	a = int(input("Introdu un numar intre 1 si 49: "))
	while a<=0 or a>=50: 
		a = int(input("Introdu un numar valit intre 1 si 49: "))
	i = 0
	while i < len(v):
    		if v[i] == a: a = int(input("Numarul este deja introdus, introdu alt numar intre 1 si 49: "))
    		i += 1
	v.append(a)
	x+=1
print("Numerele tale: ", v)
l = []
for i in range(6):
    l.append(random.randint(1, 49))
print("Numere extrase: ", l)
comune = set(v) & set(l)
print("Ai ghicit ", len(comune), " numere: ", comune)
if len(comune) == 3: 
	print("Felicitări! Ai câștigat un premiu mic!")
elif len(comune) == 4: 
	print("Felicitări! Ai câștigat un premiu mediu!")
elif len(comune) == 5: 
	print("Felicitări! Ai câștigat un premiu mediu!")
elif len(comune) == 6: 
	print("Felicitări! Ai câștigat un premiu mare!")

