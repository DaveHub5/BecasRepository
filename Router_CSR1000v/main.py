#!/usr/bin/env python3


import csr_functions as csr

stringMenu = """Menu
a) Print Routing Table
b) Print Interfaces
c) Create Interface
d) Delete Interface
s) Salir
"""



def print_routing_table():
    csr.obtain_routing_table()
 
def print_interfaces():
    csr.obtain_interfaces()
 
def exec_createInterface():
    csr.createInterface()
 
def exec_deleteInterface():
    csr.deleteInterface()

 
def invokeFunction(argument):
    switcher = {
        "a": print_routing_table,
        "b": print_interfaces,
        "c": exec_createInterface,
        "d": exec_deleteInterface      
    }
    func = switcher.get(argument, lambda: "Invalid option")
    if(func() == "Invalid option"):
        print("Invalid option")



while(True):
    print(stringMenu)
    inputData = input("Choose an option (a,b,c,d,s): ").lower()
    if(inputData == "s"):
        break
    invokeFunction(inputData)
    print()