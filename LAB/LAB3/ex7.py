preturi = [100, 50, None, 200, None, 80]
preturi_fara_none = filter(lambda x: x is not None, preturi)
preturi_reduse = map(lambda x: x * 0.9, preturi_fara_none)
rezultat = list(preturi_reduse)
print(rezultat)