import requests, pprint, random


# provide required ZIP code
zip_codes = ['60130235', '60411260', '60120385', '60135140', '60050081', '60010010', '60150160', '60115080', '60060550', '60060440', '60030100', '60110370', '60030160', '60010700', '60321160', '60355260', '60356140', '60040082', '61635090', '60534130', '61652650', '60541492', '60520514', '61660040', '01001000']



def standard_response_format(address_details: dict, success=True, error=False, message='success') -> dict:
    '''reformatting JSON response'''
    standard_format = {
        "status": 200,
        "success": success,
        "error": error,
        "message": message,
        "data": address_details
    }

    return standard_format


def get_address_from_zip_code(zip_code: str) -> dict:
    '''
        Retrieve address from viacep API using zip_code.
    '''
    try:
        response = requests.get(url=f'https://viacep.com.br/ws/{zip_code}/json/')
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
        error_message = {'error': 'location not found.'}
        return standard_response_format(address_details=error_message, success=False, error=True, message='failed to get location details.')
    else:
        return standard_response_format(address_details=address_details)



for zip_code in zip_codes:
    pprint.pprint(get_address_from_zip_code(zip_code=zip_code))