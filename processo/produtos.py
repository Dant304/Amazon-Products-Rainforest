import requests
import json
# set up the request parameters

def pegarDados():
    params = {
    'api_key': '00D50ED3D7F64B188068466EA73FADDE',
    'type': 'search',
    'amazon_domain': 'amazon.com',
    'search_term': 'iphone',
    'search_results': 'array',
    'sort_by': 'most_recent', 
    'total_pages': 1,
    'page': 1
    }

    # make the http GET request to Rainforest API
    api_result = requests.get('https://api.rainforestapi.com/request', params)
    produtos = json.loads(api_result.content)

    return produtos
