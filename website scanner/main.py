from domain_name import*
from general import*
from nmap import*
from robots_txt import*
from webscanner1 import*
from whois import*
from sys import*

ROOT_DIR = 'targets'
create_dir(ROOT_DIR)


def gather_info(name, url):
    domain_name = get_domain_name(url)
    #ip_adress = get_ip_adress(url)
    #nmap = get_nmap('-F', ip_adress)
    #robots_txt = get_robots_txt(url)
    #whois = get_whois(domain_name)
    create_report(name, url, domain_name, nmap, robots_txt, whois)


def create_report(name, full_url, domain_name, ip_address, nmap, robots_txt, whois):
    project_dir = ROOT_DIR + '/' + name
    create_dir(project_dir)
    write_file(project_dir + '/full_url.txt', full_url)
    write_file(project_dir + '/domain_name.txt', domain_name)
    write_file(project_dir + '/ipaddress.txt', ip_address)
    write_file(project_dir + '/nmap.txt', nmap)
    write_file(project_dir + '/robots.txt', robots_txt)
    write_file(project_dir + '/whois.txt', whois)

gather_info('yahoo.com', 'http://www.yahoo.com')
