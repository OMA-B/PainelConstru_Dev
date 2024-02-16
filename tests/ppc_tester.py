import requests
import pytest


# TESTS FOR PRODUCTS APPLICATION
prodID = '7464'
prodID2 = '7081'
# itemID = '129120'
# itemID2 = '129077'
analytics_endpoints = [
    'https://api2.painelconstru.com.br/analytics/projects/?type=overall-budget',
    'https://api2.painelconstru.com.br/analytics/projects/?type=budget-per-budgetist'
]

supplier_endpoints = [
    'https://api2.painelconstru.com.br/suppliers/list/',
    'https://api2.painelconstru.com.br/suppliers/subcategory/?supplier=50&supplier=51',
    'https://api2.painelconstru.com.br/suppliers/subcategory/?category=45&category=78',
    'https://api2.painelconstru.com.br/suppliers/subcategory/?subcategory=38',
    'https://api2.painelconstru.com.br/suppliers/list/?q=leroy'
]

@pytest.mark.parametrize('url', [
    'https://api2.painelconstru.com.br/products/list/',
    f'https://api2.painelconstru.com.br/products/{prodID}/items/',
    f'https://api2.painelconstru.com.br/products/{prodID}/stores/',
    f'https://api2.painelconstru.com.br/products/{prodID}/prices/',
    f'https://api2.painelconstru.com.br/products/similar/{prodID}/',
    f'https://api2.painelconstru.com.br/products/featured/',
    f'https://api2.painelconstru.com.br/products/prices/?id={prodID}&id={prodID2}',
    f'https://api2.painelconstru.com.br/products/prices/?id={prodID}&id={prodID2}'
])

def test_endpoint_availability(url):
    response = requests.get(url)
    assert response.status_code == 200

@pytest.mark.parametrize('url', analytics_endpoints)
def test_analytics_endpoint_availability(url):
    response = requests.get(url)
    assert response.status_code == 200

@pytest.mark.parametrize('url', supplier_endpoints)
def test_supplier_endpoint_availability(url):
    response = requests.get(url)
    assert response.status_code == 200


if __name__ == "__main__":
    pytest.main([__file__])
