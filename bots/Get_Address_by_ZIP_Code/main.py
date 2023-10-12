import requests, pprint, re


# provide required ZIP code
zip_codes = ['60130-235', '60411260', '60120385', '60135-140', '6005008 1', '60010010', 'gjahedb60150160', '60115080', '6006055', '60060440', '60030100', '60110370', '60030160', '60010700', '60321160', '60355260', '60356140', '60040082', '61635090', '60534130', '61652650', '60541492', '60520514', '61660040', '01001000']



def standard_response_format(details: dict, success=True, error=False, message='success') -> dict:
    '''reformatting JSON response'''
    standard_format = {
        "status": 200,
        "success": success,
        "error": error,
        "message": message,
        "data": details
    }

    return standard_format


def get_address_from_zip_code(zip_code) -> dict:
    '''
        Retrieve address from viacep API using zip_code.
    '''
    # checking and formatting user input
    digits = str(zip_code).replace('-', '')
    pattern = re.compile(pattern=r'^\d{8}$')
    expected_digits = pattern.fullmatch(string=digits)

    if expected_digits == None:
        return standard_response_format(details={'error': 'pls, input the right BR zip code or format.'}, success=False, error=True, message=f'Bad Zip Code: {zip_code}')
    
    try:
        response = requests.get(url=f'https://viacep.com.br/ws/{digits}/json/')
        address_data = response.json()

        address_details = {
            'country': 'Brazil',
            'state_acronym': address_data['uf'],
            'city': address_data['localidade'],
            'address_line_1': address_data['logradouro'],
            'address_line_2': address_data['complemento'],
            'neighborhood': address_data['bairro']
        }
    except:
        return standard_response_format(details={'error': 'location not found.'}, success=False, error=True, message='failed to get location details')
    else:
        return standard_response_format(details=address_details)



if __name__ == '__main__':
    
    for zip_code in zip_codes:
        pprint.pprint(get_address_from_zip_code(zip_code=zip_code))