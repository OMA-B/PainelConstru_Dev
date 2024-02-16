import pandas as pd, json



def create_csv(sorted_data):
    
    products_data = {
        'product_name': [data['product_name'] for data in sorted_data],
        'company_name': [data['company_name'] for data in sorted_data],
        'address': [data['address'] for data in sorted_data],
        'phone_number': [data['phone_number'] for data in sorted_data],
        'e_mail': [data['e_mail'] for data in sorted_data],
        'website': [data['website'] for data in sorted_data],
    }

    products_data_df = pd.DataFrame(products_data)

    products_data_df.to_csv(path_or_buf='products_companies_data.csv', index=False)

def update_csv(sorted_data):

    old_csv = pd.read_csv(filepath_or_buffer='products_companies_data.csv')
    
    products_data = {
        'product_name': old_csv['product_name'].to_list() + [data['product_name'] for data in sorted_data],
        'company_name': old_csv['company_name'].to_list() + [data['company_name'] for data in sorted_data],
        'address': old_csv['address'].to_list() + [data['address'] for data in sorted_data],
        'phone_number': old_csv['phone_number'].to_list() + [data['phone_number'] for data in sorted_data],
        'e_mail': old_csv['e_mail'].to_list() + [data['e_mail'] for data in sorted_data],
        'website': old_csv['website'].to_list() + [data['website'] for data in sorted_data],
    }

    products_data_df = pd.DataFrame(products_data)

    products_data_df.to_csv(path_or_buf='products_companies_data.csv', index=False)


for i in range(3):

    with open(file=f'products_companies_data{i+2}.json', mode='r') as file:
        json_data = json.load(file)

    sorted_data_list = []

    for data in json_data:

        if 'Endereço' in data: address = data['Endereço']
        else: address = ''

        if 'Telefone' in data: phone_number = data['Telefone']
        else: phone_number = ''

        if 'E-mail' in data: e_mail = data['E-mail']
        else: e_mail = ''

        if 'Website' in data: website = data['Website']
        else: website = ''

        sorted_data_list.append({
            'product_name': data['product_name'],
            'company_name': data['Razão Social'],
            'address': address,
            'phone_number': phone_number,
            'e_mail': e_mail,
            'website': website,
        })

    # create_csv(sorted_data=sorted_data_list)
    update_csv(sorted_data=sorted_data_list)
    print('Done!')
