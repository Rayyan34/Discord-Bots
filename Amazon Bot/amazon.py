import requests
from bs4 import BeautifulSoup

def search(query):
    url = f'https://www.amazon.ae/s?k={query.replace(" ", "+")}'

    headers = {
        'x-amz-rid': 'BPEXJG3RAR454WT9JDDS',
        'cache-control': 'no-cache',
        'accept-ch-lifetime': '86400',
        'content-encoding': 'gzip',
        'accept-ch': 'ect,rtt,downlink,device-memory,sec-ch-device-memory,viewport-width,sec-ch-viewport-width,dpr,sec-ch-dpr',
        'expires': '-1',
        'x-xss-protection': '1',
        'x-content-type-options': 'nosniff',
        'pragma': 'no-cache',
    }

    html = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(html.text, 'html.parser')
    output = soup.find_all('div', {'data-component-type': 's-search-result'})[0]

    data = {
        'title': output.find('span', {'class': 'a-size-base-plus a-color-base a-text-normal'}).text,
        'image': output.find('img', {'class': 's-image'})['src'],
        'price': output.find('span', {'class': 'a-offscreen'}).text,
        'rating': output.find('div', {'class': 'a-row a-size-small'}).find('span', {'class': 'a-icon-alt'}).text,
        '#_of_ratings': output.find('span', {'class': 'a-size-base s-underline-text'}).text,
        'url': output.find('a', {'class': 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})['href']
    }
    return data

