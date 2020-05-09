#!/usr/bin/env python3

#Required pip install tabulate

import requests
import json
import urllib3
from pprint import pprint
from tabulate import *

requests.packages.urllib3.disable_warnings()

def get_ticket():
    url = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/ticket"
    headers = {
        'Content-Type': 'application/json'
    }
    body_json = {
    "password": "Xj3BDqbU",
    "username": "devnetuser"
    }
    resp = requests.post(url,json.dumps(body_json),headers=headers,verify=False)
    statusCode = resp.status_code
    response_json = resp.json()
    serviceTicket = response_json['response']['serviceTicket']
    print("El ticket de servicio asignado es: ",serviceTicket)
    return serviceTicket


def print_hosts():
    url = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/host"
    ticket = get_ticket()
    headers = {
        'Content-Type': 'application/json',
        'X-Auth-Token': ticket
    }   
    resp = requests.get(url,headers=headers,verify=False)
    response_json = resp.json()
    hosts = []
    i = 0
    for host in response_json["response"]:
        i += 1
        auxHost = [
            i,
            host["hostType"],
            host["hostIp"],
            host["hostMac"]
        ] 
        hosts.append(auxHost)
    
    header_print = [
        "Number",
        "Type",
        "IP",
        "MAC"
    ]

    print(tabulate(hosts, header_print))
    #pprint(response_json)


def print_networkDevices():
    url = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/network-device"
    ticket = get_ticket()
    headers = {
        'Content-Type': 'application/json',
        'X-Auth-Token': ticket
    }   
    resp = requests.get(url,headers=headers,verify=False)
    response_json = resp.json()
    netDevices = []
    i = 0
    
    for host in response_json["response"]:
        i += 1
        auxDevs = [
            i,
            host["hostname"],
            host["family"],
            host["macAddress"],
            host["softwareVersion"],
            host["type"]
        ] 
        netDevices.append(auxDevs)
    
    header_print = [
        "Hostname",
        "Family",
        "MAC",
        "Version",
        "Type"
    ]
    print(tabulate(netDevices, header_print))
    #pprint(response_json)


def print_networkVlans():
    url = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/network-device"
    ticket = get_ticket()
    headers = {
        'Content-Type': 'application/json',
        'X-Auth-Token': ticket
    }   
    resp = requests.get(url,headers=headers,verify=False)
    response_json = resp.json()
    netIds = []
    vlanDevs = []
    i = 0
    for host in response_json["response"]:
        netIds.append(host["id"])
    print("Processing...")    
    for id in netIds:
        url = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/network-device/" + id + "/vlan"
        resp = requests.get(url,headers=headers,verify=False)
        response_json = resp.json()
        if((resp.status_code == 200)):
            for device in response_json["response"]:
                i += 1
                interfaceName = "No Data"
                ipAddress = "No Data"
                networkAddress = "No Data"
                numberOfIPs = "No Data"
                if "interfaceName" in device:
                    interfaceName = device["interfaceName"]
                if "ipAddress" in device:
                    ipAddress = device["ipAddress"]
                if "networkAddress" in device:
                    networkAddress = device["networkAddress"]
                if "numberOfIPs" in device:
                    numberOfIPs = device["numberOfIPs"]
                auxDevs = [
                    i,
                    interfaceName,
                    ipAddress,
                    networkAddress, 
                    numberOfIPs
                ] 
                vlanDevs.append(auxDevs)
                
    header_print = [
        "Interface",
        "IP",
        "Network IP",
        "Number of IPs",
    ]
    print(tabulate(vlanDevs, header_print))



def print_networkLicense():
    url = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/network-device"
    ticket = get_ticket()
    headers = {
        'Content-Type': 'application/json',
        'X-Auth-Token': ticket
    }   
    resp = requests.get(url,headers=headers,verify=False)
    response_json = resp.json()
    netIds = []
    licenseDevs = []
    i = 0
    for host in response_json["response"]:
        netIds.append(host["id"])
    print("Processing...")    
    for id in netIds:
        url = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/network-device/" + id
        resp = requests.get(url,headers=headers,verify=False)
        response_json = resp.json()        
        if((resp.status_code == 200)):
            device = response_json["response"]
            i += 1
            auxDevs = [
                i,
                device["family"],
                device["hostname"],
                device["id"], 
                device["type"],
                device["upTime"]
                ] 
            licenseDevs.append(auxDevs)
    header_print = [
        "Family",
        "Hostname",
        "ID",
        "Type",
        "UpTime"
    ]
    print(tabulate(licenseDevs, header_print))
