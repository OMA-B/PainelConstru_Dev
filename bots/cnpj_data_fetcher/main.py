import requests, pprint, os, time
from dotenv import load_dotenv

load_dotenv()


def retrieve_data_from_rapidapi_using_cnpj(cnpj_number):
    """
        NOTE_:

        the response structure from this API is different
        from the default one (receitaws API).
    """

    url = f"https://consulta-cnpj-gratis.p.rapidapi.com/office/{cnpj_number}"

    querystring = {"simples":"false"}

    headers = {
        "X-RapidAPI-Key": os.getenv('IGOR_RAPIDAPI_KEY'),
        "X-RapidAPI-Host": "consulta-cnpj-gratis.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    if 'message' in response.json():
        # wait for 1 minute for the API to reset
        time.sleep(60)
        retrieve_data_from_rapidapi_using_cnpj(cnpj_number=cnpj)
    else:
        return response.json()


def retrieve_data_from_receitawsapi_using_cnpj(cnpj_number):
    """
        NOTE_:

        this is the default API
        it should be considered of more use.
    """
    
    url = f"https://receitaws.com.br/v1/cnpj/{cnpj_number}"

    headers = {"Accept": "application/json"}

    response = requests.get(url, headers=headers)

    if 'message' in response.json():
        # wait for 1 minute for the API to reset
        time.sleep(60)
        retrieve_data_from_receitawsapi_using_cnpj(cnpj_number=cnpj)
    else:
        return response.json()



if __name__ == '__main__':

    for cnpj in ['46688275000160', '46707089000121', '50656156000101', '52853181000100', '52559499000175', '21998472000155', '50776665000160']:

        # retrieve_data_from_rapidapi_using_cnpj(cnpj_number=cnpj)
        retrieve_data_from_receitawsapi_using_cnpj(cnpj_number=cnpj)