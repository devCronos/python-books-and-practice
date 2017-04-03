import random
import urllib

def image_grabby(url):
    name= random.randrange(1,199)
    full_name= str(name)+".jpg"
    urllib.urlretrieve(url,full_name)

image_grabby("https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Blausen_0193_Catheter_PICC.png/220px-Blausen_0193_Catheter_PICC.png")