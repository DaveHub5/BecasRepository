def fDiv():
    menuNum1 = "Dividendo: "
    menuNum2 = "Divisor: "


    while(True):
        inputData = input(menuNum1)
        try:
            div1 = float(inputData)
            while(True):
                inputData = input(menuNum2)
                try:
                    div2 = float(inputData)
                    retorno = div1/div2
                    break
                except ValueError:
                    print("Write a correct value")
                except ZeroDivisionError:
                    retorno = "INFINITO"
                    break
            break
        except ValueError:
            print("Write a correct value")
    print("La división de ",div1," y ",div2," es: ",retorno)

