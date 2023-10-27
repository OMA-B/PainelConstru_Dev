import pandas as pd, json, pprint



# def create_csv_file(data_mass):

#     companies_data = {
#         "Transversal_Sector": [data["transversal_sector"] for data in data_mass],
#         "Company": [data["company"] for data in data_mass],
#         "State": [data["state"] for data in data_mass],
#         "City": [data["city"] for data in data_mass],
#         "Address": [data["address"] for data in data_mass],
#         "Complement": [data["complement"] for data in data_mass],
#         "Neighborhood": [data["neighborhood"] for data in data_mass],
#         "Zip_Code": [data["zip_code"] for data in data_mass],
#         "Contact": [data["contact"] for data in data_mass],
#         "Telephone": [data["telephone"] for data in data_mass],
#         "E_Mail": [data["mail"] for data in data_mass],
#         "Website_URL": [data["site"] for data in data_mass],
#         "Paid": [data["paid"] for data in data_mass],
#         "Extra_Info": [data["extra_info"] for data in data_mass]
#     }

#     companies_data_df = pd.DataFrame(data=companies_data)

#     companies_data_df.to_csv(path_or_buf='transversal_companies_data.csv', index=False)

# with open(file=f'transversal_companies_data1.json', mode='r') as file:
#     data_mass = json.load(fp=file)

# create_csv_file(data_mass=data_mass)


def update_csv_file(data_mass):
    existing_csv_file = pd.read_csv(filepath_or_buffer='transversal_companies_data.csv')
    
    companies_data = {
        "Transversal_Sector": existing_csv_file['Transversal_Sector'].to_list() + [data["transversal_sector"] for data in data_mass],
        "Company": existing_csv_file['Company'].to_list() + [data["company"] for data in data_mass],
        "State": existing_csv_file['State'].to_list() + [data["state"] for data in data_mass],
        "City": existing_csv_file['City'].to_list() + [data["city"] for data in data_mass],
        "Address": existing_csv_file['Address'].to_list() + [data["address"] for data in data_mass],
        "Complement": existing_csv_file['Complement'].to_list() + [data["complement"] for data in data_mass],
        "Neighborhood": existing_csv_file['Neighborhood'].to_list() + [data["neighborhood"] for data in data_mass],
        "Zip_Code": existing_csv_file['Zip_Code'].to_list() + [data["zip_code"] for data in data_mass],
        "Contact": existing_csv_file['Contact'].to_list() + [data["contact"] for data in data_mass],
        "Telephone": existing_csv_file['Telephone'].to_list() + [data["telephone"] for data in data_mass],
        "E_Mail": existing_csv_file['E_Mail'].to_list() + [data["mail"] for data in data_mass],
        "Website_URL": existing_csv_file['Website_URL'].to_list() + [data["site"] for data in data_mass],
        "Paid": existing_csv_file['Paid'].to_list() + [data["paid"] for data in data_mass],
        "Extra_Info": existing_csv_file['Extra_Info'].to_list() + [data["extra_info"] for data in data_mass]
    }

    companies_data_df = pd.DataFrame(data=companies_data)

    companies_data_df.to_csv(path_or_buf='transversal_companies_data.csv', index=False)


for i in range(7):

    with open(file=f'transversal_companies_data{i+2}.json', mode='r') as file:
        data_mass = json.load(fp=file)
    
    update_csv_file(data_mass=data_mass)












# total = 0
# for i in range(10):

#     with open(file=f'companies_data{i+1}.json', mode='r') as file:
#         data = json.load(fp=file)
#         print(len(data))
#         total += len(data)

# print(f'Total gathered so far is: {total}.')