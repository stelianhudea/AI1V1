bun = ["bine", "frumos", "super", "excelent", "minunat"]
b = "Comentariu pozitiv!"
rau = ["urât", "prost", "groaznic", "dezamăgitor"]
r = "Comentariu negativ!"
v = "Ambele"
a = input("Prop: ").lower().split()
com1 = set(a) & set(bun);
com2 = set(a) & set(rau);
if com1:
	print(b)
elif com2:
	print(r)
else:  
	print(v, "sau nici una")
