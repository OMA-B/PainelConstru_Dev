from locust import HttpUser, task, between
from all_APIs import *
import random



class ApiUser(HttpUser):
    '''Create fake users to load server'''

    wait_time = between(2, 5)

    @task
    def analytics_endpoints(self):
        api = random.choice(analytics_endpoints)
        if api.split(' : ')[0] == 'GET':
            self.client.get(api.split(' : ')[1])
        else:
            self.client.post(api.split(' : ')[1])

    @task
    def supplier_endpoints(self):
        api = random.choice(supplier_endpoints)
        if api.split(' : ')[0] == 'GET':
            self.client.get(api.split(' : ')[1])
        else:
            self.client.post(api.split(' : ')[1])

    @task
    def products_endpoints(self):
        api = random.choice(products_endpoints)
        if api.split(' : ')[0] == 'GET':
            self.client.get(api.split(' : ')[1])
        else:
            self.client.post(api.split(' : ')[1])

    @task
    def projects_endpoints(self):
        api = random.choice(projects_endpoints)
        if api.split(' : ')[0] == 'GET':
            self.client.get(api.split(' : ')[1])
        else:
            self.client.post(api.split(' : ')[1])

    @task
    def composition_endpoints(self):
        api = random.choice(composition_endpoints)
        if api.split(' : ')[0] == 'GET':
            self.client.get(api.split(' : ')[1])
        else:
            self.client.post(api.split(' : ')[1])

    @task
    def items_endpoints(self):
        api = random.choice(items_endpoints)
        if api.split(' : ')[0] == 'GET':
            self.client.get(api.split(' : ')[1])
        else:
            self.client.post(api.split(' : ')[1])

    @task
    def proposals_quotations_endpoints(self):
        api = random.choice(proposals_quotations_endpoints)
        if api.split(' : ')[0] == 'GET':
            self.client.get(api.split(' : ')[1])
        else:
            self.client.post(api.split(' : ')[1])

    @task
    def users_authentication_endpoints(self):
        api = random.choice(users_authentication_endpoints)
        if api.split(' : ')[0] == 'GET':
            self.client.get(api.split(' : ')[1])
        else:
            self.client.post(api.split(' : ')[1])