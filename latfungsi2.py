def nilai(nuts, nuas):
    total=((nuts + nuas)/2)
    print("Nilai UTS: ", nuts)
    print("Nilai UAS: ", nuas)
    print("Nilai Total:", total)
    return total

nuts =int(input("Inputkan nilai UTS:"))
nuas =int(input("Inputkan nilai UAS:"))
nilai(nuts, nuas)
