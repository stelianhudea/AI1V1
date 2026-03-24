def norma(data):
	a = min(data)
	b = max(data)
	for value in data:
		if value == a:
			value = 0.00
			print(value, " ")
		elif value == b:
			value = 1.00
			print(value, " ")
		else: 
			value = (value - a) / (b - a)
			print(value, " ")

data = [10, 20, 30, 40, 50]
norma(data)