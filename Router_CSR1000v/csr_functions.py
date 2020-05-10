from ncclient import manager
from tabulate import *
from netmiko import ConnectHandler
import xml.dom.minidom
import xmltodict
import json, requests

"""
    Obtener la tabla de routing y crear una tabla con Identificador (0,1,2...),
         Red de destino, e Interfaz de salida.
"""
def obtain_routing_table():
    print("Proccesing...")
    #Definimos conexion
    con = manager.connect(host='192.168.56.101',port=830,username="cisco",password="cisco123!",hostkey_verify=False)

    # Filtro para netconf
    netconf_filter = """
    <filter>
        <routing-state xmlns="urn:ietf:params:xml:ns:yang:ietf-routing" />
    </filter>
    """

    #Recoger información del dispositivo
    netconf_reply = con.get(filter=netconf_filter)
    netconf_reply_dict = xmltodict.parse(netconf_reply.xml)
    routes = netconf_reply_dict["rpc-reply"]["data"]["routing-state"]["routing-instance"]["ribs"]["rib"]["routes"]["route"]

    netRouting = []
    i = 0    
    for route in routes:
        i += 1
        auxRoute = [
            i,
            route["destination-prefix"],
            route["next-hop"]["outgoing-interface"]
        ] 
        netRouting.append(auxRoute)
    
    header_print = [
        "Red de destino",
        "Interfaz de salida"
    ]
    print(tabulate(netRouting, header_print))


"""
    Obtener un listado de las interfaces del router 
        (indicar, en modo tabla, el nombre de la interfaz, su IP y MAC)
"""
def obtain_interfaces():
    print("Proccesing...")
    sshovercli = ConnectHandler(device_type='cisco_ios',host='192.168.56.101',port=22,username="cisco",password='cisco123!')
    output = sshovercli.send_command("show ip interface brief")
    listOfInterfacesAndIps = output.split('\n')

    #Definimos conexion
    con = manager.connect(host='192.168.56.101',port=830,username="cisco",password="cisco123!",hostkey_verify=False)

    # Filtro para netconf
    netconf_filter = """
    <filter>
        <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces" />
    </filter>
    """
    #Recoger información del dispositivo

    netconf_reply = con.get(filter=netconf_filter)

    netconf_reply_dict = xmltodict.parse(netconf_reply.xml)
    netInterfaces = []
    i = 0
    for interface in netconf_reply_dict["rpc-reply"]["data"]["interfaces-state"]["interface"]:
        i += 1
        ip = ""
        for item in listOfInterfacesAndIps:
            listOfInt = item.split()
            if listOfInt[0] == interface["name"]:
                ip = listOfInt[1]
                break

        auxInterf = [
            i,
            interface["name"],
            ip,
            interface["phys-address"]
        ] 
        netInterfaces.append(auxInterf)
    
    header_print = [
        "Name",
        "IP",
        "MAC"
    ]
    print(tabulate(netInterfaces, header_print))











"""
    Crear Interfaces

"""
def createInterface():
    menuNum1 = "Introduzca el Nombre (must be a number): "
    menuNum2 = "Introduzca la IP: "
    menuNum3 = "Introduzca la Máscara de Subred: "

    newName = "41"
    newIp = "41.41.41.41"
    newMasc = "255.255.255.0"

    #Definimos conexion
    con = manager.connect(host='192.168.56.101',port=830,username="cisco",password="cisco123!",hostkey_verify=False)

    while(True):
        newName = input(menuNum1)
        newIp = input(menuNum2)
        newMasc = input(menuNum3)

        # Filtro para netconf
        netconf_data = """
        <config> <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
            <interface>
                <Loopback>
                    <name>{}</name>
                    <description>Interface_Test_Loopback_Overlapped</description>
                    <ip>
                        <address>  
                            <primary>
                                <address>{}</address>
                                <mask>{}</mask>
                            </primary>         
                        </address>    
                    </ip>
                </Loopback>
            </interface>
        </native></config>
        """.format(newName,newIp,newMasc)

        try:
            print("Proccesing...")
            netconf_reply = con.edit_config(target="running", config=netconf_data)
            print("Interface {} has been created.".format(newName))
            break
        except Exception as e:
            print(e)  



"""
    Borrar Interfaces

"""
def deleteInterface():

    sshovercli = ConnectHandler(device_type='cisco_ios',host='192.168.56.101',port=22,username="cisco",password='cisco123!')

    output = sshovercli.send_command("show ip interface brief")
    listOfInterfacesAndIps = output.split('\n')

    menuItems = []
    for item in listOfInterfacesAndIps[1:len(listOfInterfacesAndIps)]:
        listOfInt = item.split()
        menuItems.append(listOfInt[0])

    menu = ""
    dictOptions = {}
    i = 0
    for item in menuItems:
        i+=1
        menu += "{}) {}\n".format(i,item)
        dictOptions[str(i)] = item
    menu += "s) Salir: "
    menu += "\nChoose option: "

    option = ""
    while(True):
        option = input(menu).lower()
        if option == "s":
            break
        try:
            optionInt = int(option)
            if optionInt < 1 or optionInt > len(menuItems):
                print("Choose a correct option")
            else:
                break
        except ValueError:
            print("Choose a correct option")


    #print(dictOptions[option])
    if option != "s":
        print("Proccesing...")
        requests.packages.urllib3.disable_warnings()

        #Conection address
        api_url = "https://192.168.56.101/restconf/data/ietf-interfaces:interfaces/interface={}".format(dictOptions[option])

        #Headers
        headers = {"Accept": "application/yang-data+json", "Content-Type": "application/yang-data+json"}

        #Authentication
        basic_auth = ("cisco", "cisco123!")

        resp = requests.delete(api_url, auth=basic_auth, headers=headers, verify=False)

        
        if(resp.status_code >= 200 and resp.status_code <= 299):
            print("Interface {} has been deleted.".format(dictOptions[option]))
        else:
            print("Error code: {}".format(resp.status_code, resp.json()))


"""
    Implementar una petición a 2 módulos de yang diferentes compatibles con nuestro router
"""
#Los modulos utilizados han sido:
#       urn:ietf:params:xml:ns:yang:ietf-interfaces
#       urn:ietf:params:xml:ns:yang:ietf-routing