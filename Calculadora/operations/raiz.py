import math  

def fRaiz():
    menuNum1 = "Raiz: "


    while(True):
        inputData = input(menuNum1)
        try:
            val1 = float(inputData)
            try:
                raiz = math.sqrt(val1)
                break
            except ValueError:
                print("Write a number >= 0")
        except ValueError:
            print("Write a correct value")
    print("La raiz de ",val1," es: ",raiz)

