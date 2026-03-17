while True:
    a = int(input("Introdu nota: "))
    if 9 <= a <= 10:
        print("Excelent")
        break
    elif 7 <= a <= 8:
        print("Bine")
        break
    elif 5 <= a <= 6:
        print("Suficient")
        break
    elif 1 <= a < 5:
        print("Reexaminare")
        break
    else:
        print("Introdu o nota valida.")