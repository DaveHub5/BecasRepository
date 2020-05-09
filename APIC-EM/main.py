#!/usr/bin/env python3


import apic_em_functions as apic

stringMenu = """Menu
a) Print Hosts
b) Print Network Devices
c) Print Network Vlans
d) Print Netwrok License
s) Salir
"""



def print_hosts():
    apic.print_networkDevices()
 
def print_networkDevices():
    apic.print_networkDevices()
 
def print_networkVlans():
    apic.print_networkVlans()
 
def print_networkLicense():
    apic.print_networkLicense()

 
def invokeFunction(argument):
    switcher = {
        "a": print_hosts,
        "b": print_networkDevices,
        "c": print_networkVlans,
        "d": print_networkLicense      
    }
    func = switcher.get(argument, lambda: "Invalid option")
    if(func() == "Invalid option"):
        print("Invalid option")



while(True):
    print(stringMenu)
    inputData = input("Choose an option (a,b,c,d,s): ")
    if(inputData == "s"):
        break
    invokeFunction(inputData)
    print()

