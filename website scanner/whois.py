import os

def get_whois(url):
    command = "nmap --script whois* -sn " +url
    process = os.popen(command)
    results = str(process.read())
    return results

print(get_whois('thenewboston.com'))