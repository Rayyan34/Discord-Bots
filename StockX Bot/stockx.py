import requests
import json 

def search(query):
    url = f'https://stockx.com/api/browse?_search={query}'

    headers = {
        'Accept': 'application/json',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'utf-8',
        'X-Requested-With': 'XMLHttpRequest',
        'App-Platform': 'Iron',
        'Host': 'stockx.com',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-GPC': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0'        
    }

    html = requests.get(url=url, headers=headers)
    output = json.loads(html.text)
    return output['Products'][0]

