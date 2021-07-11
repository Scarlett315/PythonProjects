def romannumeral(RomanNum):
    RomanDict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000, "IV":3,
                 "IX":8, "XL":30, "XC":80,"CD":300, "CM":800}
    n = 0
    b = "hi"
    for e in RomanNum:
        if b+e in RomanDict:
            n += RomanDict[b+e]
        else:
            n += RomanDict[e]

        print("e = "+ e)
        print("b = "+ b)
        print("n = "+ str(n))
        b = e

    return n

while True:
    numb = input("Insert Roman Numeral")
    if numb == "Quit":
        print("program has been boinked")
        break
    print(romannumeral(numb))