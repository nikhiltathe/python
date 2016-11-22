import random
from urllib import request

goog_url = 'http://real-chart.finance.yahoo.com/table.csv?s=GOOG&d=8&e=9&f=2016&g=d&a=7&b=19&c=2004&ignore=.csv'

def download_csv(url):
    response = request.urlopen(goog_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    dest = r'Goog.csv'
    fx = open(dest,"w")
    for line in lines:
        fx.write(line + "\n")

    fx.close()

download_csv(goog_url)