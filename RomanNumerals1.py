

def romannumeral(num):
    RomanNum = ""
    while num != 0:
        if num >= 1000:
            RomanNum += "M"
            num -= 1000
        elif num >= 900:
            RomanNum += "CM"
            num -= 900
        elif num >= 500:
            RomanNum += "D"
            num -= 500
        elif num >= 400:
            RomanNum += "CD"
            num -= 400
        elif num >= 100:
            RomanNum += "C"
            num -= 100
        elif num >= 90:
            RomanNum += "XC"
            num -= 90
        elif num >= 50:
            RomanNum += "L"
            num -= 50
        elif num >= 40:
            RomanNum += "XL"
            num -= 40
        elif num >= 10:
            RomanNum += "X"
            num -= 10
        elif num >= 9:
            RomanNum += "IX"
            num -= 9
        elif num >= 5:
            RomanNum += "V"
            num -= 5
        elif num >= 4:
            RomanNum += "IV"
            num -= 4
        elif num >= 1:
            RomanNum += "I"
            num -= 1
    return RomanNum

while True:
    numb = int(input("Insert number"))
    if numb == 0:
        print("program has been boinked")
        break
    print(romannumeral(numb))