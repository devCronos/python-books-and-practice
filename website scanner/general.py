import os
from socket import gethostbyname

def get_ip_adress(url):
    return gethostbyname(url)


print(get_ip_adress('nmap.org'))