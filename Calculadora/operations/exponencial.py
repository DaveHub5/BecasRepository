def fExpo():
    menuNum1 = "Base: "
    menuNum2 = "Exponente: "


    while(True):
        inputData = input(menuNum1)
        try:
            base = float(inputData)
            while(True):
                inputData = input(menuNum2)
                try:
                    expo = float(inputData)
                    break
                except ValueError:
                    print("Write a correct value")
            break
        except ValueError:
            print("Write a correct value")
    print(base," elevado a ",expo," es: ",pow(base,expo))

