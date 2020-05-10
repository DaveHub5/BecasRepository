#!/usr/bin/env python3


from operations.suma import fSuma
from operations.resta import fResta
from operations.multiplicacion import fMul
from operations.division import fDiv
from operations.exponencial import fExpo
from operations.raiz import fRaiz



stringMenu = """Menu
a) Suma
b) Resta
c) Multiplicación
d) División
e) Exponente
f) Raiz
s) Salir
"""



def opcionSuma():
    fSuma()
 
def opcionResta():
    fResta()
 
def opcionMultiplicacion():
    fMul()
 
def opcionDivision():
    fDiv()

def opcionExponencial():
    fExpo()
 
def opcionRaiz():
    fRaiz()
 
def invokeFunction(argument):
    switcher = {
        "a": opcionSuma,
        "b": opcionResta,
        "c": opcionMultiplicacion,
        "d": opcionDivision,
        "e": opcionExponencial,
        "f": opcionRaiz,        
    }
    func = switcher.get(argument, lambda: "Invalid option")
    if(func() == "Invalid option"):
        print("Invalid option")



while(True):
    print(stringMenu)
    inputData = input("Choose an option (a,b,c,d,e,f,s): ").lower()
    if(inputData == "s"):
        break
    invokeFunction(inputData)

