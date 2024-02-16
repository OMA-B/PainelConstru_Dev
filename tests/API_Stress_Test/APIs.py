# TESTS FOR PRODUCTS APPLICATION
prodID = '7464'
prodID2 = '7081'
# itemID = '129120'
# itemID2 = '129077'


analytics_endpoints = [
    'https://api2.painelconstru.com.br/analytics/projects/?type=overall-budget',
    'https://api2.painelconstru.com.br/analytics/projects/?type=budget-per-budgetist',
    'https://api2.painelconstru.com.br/analytics/products/?type=catalog-count',
]

supplier_endpoints = [
    'https://api2.painelconstru.com.br/suppliers/list/',
    'https://api2.painelconstru.com.br/suppliers/subcategory/?supplier=50&supplier=51',
    'https://api2.painelconstru.com.br/suppliers/subcategory/?category=45&category=78',
    'https://api2.painelconstru.com.br/suppliers/subcategory/?subcategory=38',
    'https://api2.painelconstru.com.br/suppliers/list/?q=leroy',
]

products_endpoints = [
    'https://api2.painelconstru.com.br/products/list/',
    f'https://api2.painelconstru.com.br/products/{prodID}/items/',
    f'https://api2.painelconstru.com.br/products/{prodID}/stores/',
    f'https://api2.painelconstru.com.br/products/{prodID}/prices/',
    f'https://api2.painelconstru.com.br/products/similar/{prodID}/',
    f'https://api2.painelconstru.com.br/products/featured/',
    f'https://api2.painelconstru.com.br/products/prices/?id={prodID}&id={prodID2}',
    'https://api2.painelconstru.com.br/products/images/',
]

print(len(analytics_endpoints) + len(supplier_endpoints) + len(products_endpoints))