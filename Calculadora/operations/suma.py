def fSuma():
    menuNum1 = "Primer Número: "
    menuNum2 = "Segundo Número: "


    while(True):
        inputData = input(menuNum1)
        try:
            sum1 = float(inputData)
            while(True):
                inputData = input(menuNum2)
                try:
                    sum2 = float(inputData)
                    break
                except ValueError:
                    print("Write a correct value")
            break
        except ValueError:
            print("Write a correct value")
    print("La suma de ",sum1," y ",sum2," es: ",sum1+sum2)
