def fResta():
    menuNum1 = "Primer Número: "
    menuNum2 = "Segundo Número: "


    while(True):
        inputData = input(menuNum1)
        try:
            res1 = float(inputData)
            while(True):
                inputData = input(menuNum2)
                try:
                    res2 = float(inputData)
                    break
                except ValueError:
                    print("Write a correct value")
            break
        except ValueError:
            print("Write a correct value")
    print("La resta de ",res1," y ",res2," es: ",res1-res2)

