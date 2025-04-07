import requests as r

#super simple ip geo lookup
#using the api of ipinfo.io

def x1(ip):
    y1 = f'https://ipinfo.io/{ip}/json'
    z1 = r.get(y1)
    
    if z1.status_code == 200:
        w1 = z1.json()

        print(f"IP: {w1.get('ip')}")
        print(f"Host: {w1.get('hostname')}")
        print(f"City: {w1.get('city')}")
        print(f"Region: {w1.get('region')}")
        print(f"Country: {w1.get('country')}")
        print(f"Postal Code: {w1.get('postal')}")
        print(f"Coordinates: {w1.get('loc')}")
        print(f"Org: {w1.get('org')}")
        print(f"ASN: {w1.get('asn')}")
        print(f"Network: {w1.get('network')}")
    else:
        print(f"Error did not find any geo info for {ip}")

def y2():
    ip = input("Enter an ip to geo lookup ")
    x1(ip)

y2()