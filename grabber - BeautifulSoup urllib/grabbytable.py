import urllib
import request

dis= 'http://chart.finance.yahoo.com/table.csv?s=CSV&a=8&b=2&c=2016&d=9&e=2&f=2016&g=d&ignore=.csv'

def download_table_thing(url):
    response=urllib.urlopen(url)
    csv=response.read()
    csv_str=str(csv)
    lines=csv_str.split('//n')
    dest_url=r'googl.csv'
    fx=open(dest_url, "w")
    for line in lines:
        fx.write(line+"/n")
    fx.close()
download_table_thing(dis)


