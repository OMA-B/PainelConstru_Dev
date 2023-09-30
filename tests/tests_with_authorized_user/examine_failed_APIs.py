import requests, json, pprint

# gather all failed endpoints
from all_APIs import *

failed_endpoints = [projects_endpoints[6], projects_endpoints[1], projects_endpoints[0], projects_endpoints[3], projects_endpoints[8], projects_endpoints[7], projects_endpoints[9], projects_endpoints[4], analytics_endpoints[3], users_authentication_endpoints[1], users_authentication_endpoints[2], users_authentication_endpoints[3], users_authentication_endpoints[0], supplier_endpoints[6], products_endpoints[11], products_endpoints[12], proposals_quotations_endpoints[0], proposals_quotations_endpoints[1]]


# at first, fetch access token
with open('tokens.json', mode='r+') as file:
    access_token = json.load(file)['data']['tokens']['access_token']

header = {'Authorization': f'Bearer {access_token}'}

result_list = []

# consult each endpoint to retrieve error messages
for endpoint in failed_endpoints:
    if endpoint.split(' : ')[0] == 'GET':
        response = requests.get(endpoint.split(' : ')[1], headers=header)
    else:
        response = requests.post(endpoint.split(' : ')[1], headers=header)
    # response.raise_for_status()
    if response.status_code == 404:
        response_text = 'Page not found!'
    else:
        response_text = response.text

    result_list.append({
        'Endpoint': endpoint,
        'Response': response_text,
        'HTTP Error code': response.status_code,
    })

with open('failed_endpoints_response_list.json', mode='w+') as file:
    json.dump(result_list, file)