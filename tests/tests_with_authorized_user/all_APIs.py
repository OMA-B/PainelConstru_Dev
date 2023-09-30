# TESTS FOR PRODUCTS APPLICATION
prodID = '7464'
prodID2 = '7081'
itemID = '129120'
# itemID2 = '129077'
project_ID = 'project ID'


analytics_endpoints = [
    'GET : https://api2.painelconstru.com.br/analytics/projects/?type=overall-budget',
    'GET : https://api2.painelconstru.com.br/analytics/projects/?type=budget-per-budgetist',
    'GET : https://api2.painelconstru.com.br/analytics/products/?type=catalog-count',
    'GET : https://api2.painelconstru.com.br/analytics/products/',
    'GET : https://api2.painelconstru.com.br/analytics/products/?type=catalog-count',
    'GET : https://api2.painelconstru.com.br/projects/analytics-prices/9998/',
    'GET : https://api2.painelconstru.com.br/projects/analytics-proposals/9998/',
]

supplier_endpoints = [
    'GET : https://api2.painelconstru.com.br/suppliers/list/',
    'GET : https://api2.painelconstru.com.br/suppliers/subcategory/?supplier=50&supplier=51',
    'GET : https://api2.painelconstru.com.br/suppliers/subcategory/?category=45&category=78',
    'GET : https://api2.painelconstru.com.br/suppliers/subcategory/?subcategory=38',
    'GET : https://api2.painelconstru.com.br/suppliers/subcategory/?project=9998',
    'GET : https://api2.painelconstru.com.br/suppliers/list/?q=leroy',
    'POST : https://api2.painelconstru.com.br/suppliers/message/email/',
]

products_endpoints = [
    'GET : https://api2.painelconstru.com.br/products/list/',
    f'GET : https://api2.painelconstru.com.br/products/{prodID}/items/',
    f'GET : https://api2.painelconstru.com.br/products/{prodID}/stores/',
    f'GET : https://api2.painelconstru.com.br/products/prices/?={prodID}&id=4',
    f'GET : https://api2.painelconstru.com.br/products/similar/{prodID}/',
    'GET : https://api2.painelconstru.com.br/products/featured/',
    f'GET : https://api2.painelconstru.com.br/products/prices/?id={prodID}&id={prodID2}',
    'GET : https://api2.painelconstru.com.br/products/images/',
    f'GET : https://api2.painelconstru.com.br/products/{prodID}/wishlist/',
    'GET : https://api2.painelconstru.com.br/products/user-products/',
    f'POST : https://api2.painelconstru.com.br/products/{prodID}/wishlist/',
    f'POST : https://api2.painelconstru.com.br/products/{prodID}/track-price/',
    'POST : https://api2.painelconstru.com.br/products/create/',
    'GET : https://api2.painelconstru.com.br/products/open-products/',
    'GET : https://api2.painelconstru.com.br/products/alert-prices/',
]

projects_endpoints = [
    'POST : https://api2.painelconstru.com.br/projects/create/',
    f'POST : https://api2.painelconstru.com.br/projects/edit/{project_ID}/',
    'GET : https://api2.painelconstru.com.br/projects/list/',
    f'GET : https://api2.painelconstru.com.br/projects/history/{project_ID}/',
    f'GET : https://api2.painelconstru.com.br/projects/sectors/{project_ID}/',
    'GET : https://api2.painelconstru.com.br/projects/',
    f'GET : https://api2.painelconstru.com.br/suppliers/subcategory/?project={project_ID}',
    f'GET : https://api2.painelconstru.com.br/projects/products/{project_ID}/',
    f'POST : https://api2.painelconstru.com.br/projects/populate/10030//{project_ID}/',
    f'GET : https://api2.painelconstru.com.br/projects/price-matrix/{project_ID}/',
]

composition_endpoints = ['GET : https://api2.painelconstru.com.br/projects/list/?type=composition']

items_endpoints = [f'GET : https://api2.painelconstru.com.br/items/associated-products/{itemID}/']

proposals_quotations_endpoints = [
    f'POST : https://api2.painelconstru.com.br/proposals/request/quotation/{project_ID}/',
    f'POST : https://api2.painelconstru.com.br/proposals/submit/{project_ID}/',
]

users_authentication_endpoints = [
    'POST : https://api2.painelconstru.com.br/auth/signup/',
    'POST : https://api2.painelconstru.com.br/auth/update-password/',
    'POST : https://api2.painelconstru.com.br/auth/recover-account/',
    'GET : https://api2.painelconstru.com.br/auth/recover-account/',
]

print(len(analytics_endpoints) + len(supplier_endpoints) + len(products_endpoints))