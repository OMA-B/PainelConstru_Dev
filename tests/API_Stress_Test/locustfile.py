from locust import HttpUser, task, between
from APIs import analytics_endpoints, supplier_endpoints, products_endpoints
import random



class ApiUser(HttpUser):
    '''Create fake users to load server'''

    wait_time = between(2, 5)

    @task
    def analytics_endpoints(self):
        self.client.get(random.choice(analytics_endpoints))

    @task
    def supplier_endpoints(self):
        self.client.get(random.choice(supplier_endpoints))

    @task
    def products_endpoints(self):
        self.client.get(random.choice(products_endpoints))