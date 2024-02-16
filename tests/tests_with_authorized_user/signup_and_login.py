from dotenv import load_dotenv
import os, requests,json, pprint

load_dotenv()

header = {'Content': 'application/json'}

# # Sign up section
# parameters = {
#     'fullname': os.getenv('NAME'),
#     'email': os.getenv('EMAIL'),
#     'password': os.getenv('PASSWORD'),
#     'platform': 'products-panel',
# }

# # signing up
# response = requests.post(url='https://api2.painelconstru.com.br/auth/signup/', params=parameters, headers=header)
# response.raise_for_status()
# print(response.json())

# Login section
parameters = {
    'email': os.getenv('EMAIL'),
    'password': os.getenv('PASSWORD'),
}

# logging in
response = requests.post(url='https://api2.painelconstru.com.br/auth/login/', data=parameters, headers=header)
response.raise_for_status()

with open('tokens.json', mode='w+') as file:
    json.dump(response.json(), file)
pprint.pprint(response.json())