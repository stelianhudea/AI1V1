import random
n = random.randint(1, 50)
print("Random: " + str(n))
a = int(input("Introdu un numar intre 1 si 50: "))
while a<=0 or a>=51: 
	a = int(input("Introdu un numar valit intre 1 si 50: "))
k=0
i=0
while k==0:
	if n>a:
		print("Numărul este mai mare!")
	elif n<a:
        	print("Numărul este mai mic!")
	else:
       		print("Felicitări! Ai ghicit numărul în " + str(i) + " încercări.")
        	k=1
	if k==0: 
		a = int(input("Noul numar: "))
		i += 1
