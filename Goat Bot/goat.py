import requests
import json

def search(query):
    url = f'https://ac.cnstrc.com/search/{query.replace(" ", "%20")}?c=ciojs-client-2.27.11&key=key_XT7bjdbvjgECO5d8&i=c3513e16-4f21-4bfe-8480-f0b21ebb8e67&s=1&num_results_per_page=25&_dt=1655376325725'

    html = requests.get(url=url)
    output = json.loads(html.text)

    return output['response']['results'][0]

