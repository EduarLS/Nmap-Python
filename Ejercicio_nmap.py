# Autor: Eduardo Lopez Solis
# Programa que muestra los puertos abiertos de un host
# 27/11/2020 – 5:59 pm
import nmap

objetivo = '127.0.0.1'
scanner = nmap.PortScanner()
lista = scanner.scan(objetivo)
hosts = [(x, scanner[x]['status']['state']) for x in scanner.all_hosts()]

for host, status in hosts:
    if scanner[host].all_protocols() == []:
        pass
    else:
        for protocolo in scanner[host].all_protocols():
            puertos = list(scanner[host][protocolo].keys())
            puertos.sort()
            print('-'*40)
            print('Host:', host + ' ' + 'status:', status)
            print('Protocol : ' + protocolo)
            for puerto in puertos:
                print(f"Puerto: {puerto} State: {scanner[host][protocolo][puerto]['state']}")
        print('-'*40)