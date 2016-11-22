import random
import urllib.request

def download_image(url):
    name = random.randrange(1,1000)
    full_name = str(name)+'.jpg'
    urllib.request.urlretrieve(url,full_name)

download_image("http://a1.espncdn.com/combiner/i?img=%2Fphoto%2F2016%2F0819%2Fr116843_1296x518_5%2D2.jpg&w=768&h=307&scale=crop&cquality=80&location=origin")