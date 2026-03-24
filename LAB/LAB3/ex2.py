def genereaza_factura( **kwargs):
	for key, value in kwargs.items():
		print(key, " ", value)

genereaza_factura(NUME='Pop', OBIECT= 'Mere', BUC='10', PRET='24')