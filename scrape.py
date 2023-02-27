import json
import requests
from bs4 import BeautifulSoup

def scrape(country='India'):
    country = country.lower().replace(' ', '-')
    res = requests.get('https://www.factmonster.com/world/countries/'+country)
    url_data = BeautifulSoup(res.text, 'html.parser')


    def data_heading_nolink(url_data):
        keys = ('Monetary unit', 'National name')
        result: dict = {}
        for j in keys:
            for i in url_data.find_all('p'):
                try:
                    if j in str(i):
                        result[j] = i.text.split(':')[1].strip()
                        break
                    else:
                        result[j] = None
                except IndexError:
                    result[j] = 'Failed to retrieve'
        return result


    def data_heading_link(url_data):
        keys = ('Capital', 'Language')
        result: dict = {}
        for j in keys:
            for i in url_data.find_all('p'):
                try:
                    if j in str(i):
                        result[j] = i.text.split(':')[1].split(',')[0].strip()
                        break
                    else:
                        result[j] = None
                    if 'Capital and largest' in str(i):
                        result['Largest city'] = result['Capital']
                    else:
                        result['Largest city'] = None
                except IndexError:
                    result[j] = 'Failed to retrieve'
        return result


    def get_map(url_data):
        map_code = str(url_data.select('.field_country_map')).split()
        for i in map_code:
            if 'src' in i:
                return('https://www.factmonster.com'+i[5:])
        return 'Map not found'


    info: dict = {}
    info.update(data_heading_nolink(url_data))
    info.update(data_heading_link(url_data))
    info['map']=get_map(url_data)

    counrty_json = json.dumps(info)
    print(info)
    return counrty_json
