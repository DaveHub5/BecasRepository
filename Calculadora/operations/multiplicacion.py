def fMul():
    menuNum1 = "Primer Número: "
    menuNum2 = "Segundo Número: "


    while(True):
        inputData = input(menuNum1)
        try:
            mul1 = float(inputData)
            while(True):
                inputData = input(menuNum2)
                try:
                    mul2 = float(inputData)
                    break
                except ValueError:
                    print("Write a correct value")
            break
        except ValueError:
            print("Write a correct value")
    print("La multiplicacion de ",mul1," y ",mul2," es: ",mul1*mul2)

