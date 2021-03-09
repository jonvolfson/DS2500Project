import csv
from urllib.request import urlopen

# reads in data from the given url and 
url = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'


with urlopen(url) as response:
    html_response = response.read()
    encoding = response.headers.get_content_charset('utf-8')
    decoded_html = str(html_response.decode(encoding))
    
    lines = decoded_html.split('\n')

    cr = csv.reader(lines, delimiter=',')
    
    for row in cr:
        print(row)