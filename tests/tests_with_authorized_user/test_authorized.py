from locust import HttpUser, task, between
from all_APIs import *
import random, json


# at first, fetch access token
with open('tokens.json', mode='r+') as file:
    access_token = json.load(file)['data']['tokens']['access_token']

header = {'Authorization': f'Bearer {access_token}'}


# conducting authorized tests
class ApiUser(HttpUser):
    '''Create fake users to load server'''

    wait_time = between(2, 5)

    @task
    def analytics_endpoints(self):
        api = random.choice(analytics_endpoints)
        if api.split(' : ')[0] == 'GET':
            self.client.get(api.split(' : ')[1], headers=header)
        else:
            self.client.post(api.split(' : ')[1], headers=header)

    @task
    def supplier_endpoints(self):
        api = random.choice(supplier_endpoints)
        if api.split(' : ')[0] == 'GET':
            self.client.get(api.split(' : ')[1], headers=header)
        else:
            self.client.post(api.split(' : ')[1], headers=header)

    @task
    def products_endpoints(self):
        api = random.choice(products_endpoints)
        if api.split(' : ')[0] == 'GET':
            self.client.get(api.split(' : ')[1], headers=header)
        else:
            self.client.post(api.split(' : ')[1], headers=header)

    @task
    def projects_endpoints(self):
        api = random.choice(projects_endpoints)
        if api.split(' : ')[0] == 'GET':
            self.client.get(api.split(' : ')[1], headers=header)
        else:
            self.client.post(api.split(' : ')[1], headers=header)

    @task
    def composition_endpoints(self):
        api = random.choice(composition_endpoints)
        if api.split(' : ')[0] == 'GET':
            self.client.get(api.split(' : ')[1], headers=header)
        else:
            self.client.post(api.split(' : ')[1], headers=header)

    @task
    def items_endpoints(self):
        api = random.choice(items_endpoints)
        if api.split(' : ')[0] == 'GET':
            self.client.get(api.split(' : ')[1], headers=header)
        else:
            self.client.post(api.split(' : ')[1], headers=header)

    @task
    def proposals_quotations_endpoints(self):
        api = random.choice(proposals_quotations_endpoints)
        if api.split(' : ')[0] == 'GET':
            self.client.get(api.split(' : ')[1], headers=header)
        else:
            self.client.post(api.split(' : ')[1], headers=header)

    @task
    def users_authentication_endpoints(self):
        api = random.choice(users_authentication_endpoints)
        if api.split(' : ')[0] == 'GET':
            self.client.get(api.split(' : ')[1], headers=header)
        else:
            self.client.post(api.split(' : ')[1], headers=header)