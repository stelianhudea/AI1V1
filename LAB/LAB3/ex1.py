#1=hartie | 2=foarfeca | 3=piatra
def win(x,y):
	if x==1 and y==1 or x==2 and y==2 or x==3 and y==3:
		print("EGALITATE")
	elif x==1 and y==2: 
		print("WIN: FOARFECA")
	elif x==2 and y==3: 
		print("WIN: PIATRA")
	elif x==1 and y==3: 
		print("WIN: HARTIE")
	else: print("ERR")

print("1=hartie | 2=foarfeca | 3=piatra")
x = int(input("J1: "))
y = int(input("J2: "))
win(x,y)