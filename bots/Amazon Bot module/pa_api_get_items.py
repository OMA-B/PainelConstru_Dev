"""
 ProductAdvertisingAPI

 https://webservices.amazon.com/paapi5/documentation/index.html

"""

"""
This sample code snippet is for ProductAdvertisingAPI 5.0's GetItems API

For more details, refer:
https://webservices.amazon.com/paapi5/documentation/get-items.html

"""

from paapi5_python_sdk.api.default_api import DefaultApi
from paapi5_python_sdk.models.condition import Condition
from paapi5_python_sdk.models.get_items_request import GetItemsRequest
from paapi5_python_sdk.models.get_items_resource import GetItemsResource
from paapi5_python_sdk.models.partner_type import PartnerType
from paapi5_python_sdk.rest import ApiException
import json, pprint


def parse_response(item_response_list):
    """
    The function parses GetItemsResponse and creates a dict of ASIN to Item object
    :param item_response_list: List of Items in GetItemsResponse
    :return: Dict of ASIN to Item object
    """
    mapped_response = {}
    for item in item_response_list:
        mapped_response[item.asin] = item
    return mapped_response


def get_items(id_list):
    """ Following are your credentials """
    """ Please add your access key here """
    access_key = "AKIAIZEP3L7JNQ2VO6DQ"

    """ Please add your secret key here """
    secret_key = "1pUKtGgLs1vS5aTKbsgn3x7/TkZm0aUd8JgxYqgf"

    """ Please add your partner tag (store/tracking id) here """
    partner_tag = "painelconst0a-20"

    """ PAAPI host and region to which you want to send request """
    """ For more details refer: https://webservices.amazon.com/paapi5/documentation/common-request-parameters.html#host-and-region"""
    host = "webservices.amazon.com.br"
    region = "us-east-1"

    """ API declaration """
    default_api = DefaultApi(
        access_key=access_key, secret_key=secret_key, host=host, region=region
    )

    """ Request initialization"""

    """ Choose item id(s) """
    item_ids = id_list

    """ Choose resources you want from GetItemsResource enum """
    """ For more details, refer: https://webservices.amazon.com/paapi5/documentation/get-items.html#resources-parameter """
    get_items_resource = [
        GetItemsResource.ITEMINFO_BYLINEINFO,
        GetItemsResource.ITEMINFO_FEATURES,
        GetItemsResource.ITEMINFO_PRODUCTINFO,
        GetItemsResource.ITEMINFO_TITLE,
        GetItemsResource.OFFERS_LISTINGS_PRICE,
    ]

    """ Forming request """

    try:
        get_items_request = GetItemsRequest(
            partner_tag=partner_tag,
            partner_type=PartnerType.ASSOCIATES,
            marketplace="www.amazon.com.br",
            condition=Condition.NEW,
            item_ids=item_ids,
            resources=get_items_resource,
            languages_of_preference= ['pt_BR']
        )
    except ValueError as exception:
        print("Error in forming GetItemsRequest: ", exception)
        return

    try:
        """ Sending request """
        response = default_api.get_items(get_items_request)

        print("API called Successfully")
        # print("Complete Response:", response)
        product_retreived_list = []

        """ Parse response """
        if response.items_result is not None:
            '''extract data from returned result'''
            data = parse_response(response.items_result.items)

            for item_id in item_ids:
                # print("Printing information about the item_id: ", item_id)
                if item_id in data:
                    item = {
                        'product_name': data[item_id].item_info.title.display_value,
                        'price': data[item_id].offers.listings[0].price.display_amount,
                        'page_url': data[item_id].detail_page_url,
                        'SKU': data[item_id].asin,
                        'manufacturer': data[item_id].item_info.by_line_info.manufacturer.display_value,
                        'description': '\n'.join(data[item_id].item_info.features.display_values),
                    }
                    product_retreived_list.append(item)
                else:
                    print("Item not found, check errors")

            with open(file='products.json', mode='w+') as file:
                json.dump(product_retreived_list, file)

            return product_retreived_list

        if response.errors is not None:
            print("\nPrinting Errors:\nPrinting First Error Object from list of Errors")
            print("Error code", response.errors[0].code)
            print("Error message", response.errors[0].message)

    except ApiException as exception:
        print("Error calling PA-API 5.0!")
        print("Status code:", exception.status)
        print("Errors :", exception.body)
        print("Request ID:", exception.headers["x-amzn-RequestId"])

    except TypeError as exception:
        print("TypeError :", exception)

    except ValueError as exception:
        print("ValueError :", exception)

    except Exception as exception:
        print("Exception :", exception)


if __name__ == '__main__':
    '''paste links of products to get in product list'''
    product_list = ['https://www.amazon.com.br/dp/B08DH24F2D?pf_rd_m=A3RN7G7QC5MWSZ&pf_rd_s=merchandised-search-11&pf_rd_r=GV0S8XMNYTPBYWAVPTNB&pf_rd_t=101&pf_rd_p=d7d6de16-b2fe-44ed-8d82-bc5c66fa98d4&pf_rd_i=20941779011&linkCode=sl1&tag=painelconst0a-20&linkId=796f2d352c701d2ab4793a168699f089&language=pt_BR&ref_=as_li_ss_tl','https://www.amazon.com.br/L%C3%A2mpada-Positivo-Casa-Inteligente-Branco/dp/B09WF3CH36/', 'https://www.amazon.com.br/Echo-Dot-5%C2%AA-gera%C3%A7%C3%A3o-Cor-Preta/dp/B09B8VGCR8/', 'https://www.amazon.com.br/Patrulha-Central-Comando-Sunny-Multicor/dp/B07B9MQKJR/ref=asc_df_B07B9MQKJR/?hvadid=379742433241&hvpos=&hvnetw=g&hvrand=11878202361525725922&hvpone=&hvptwo=&hvqmt=&hvdev=m&hvdvcmdl=&hvlocint=&hvlocphy=1001686&hvtargid=pla-819411289386&psc=1', 'https://www.amazon.com.br/dp/B0C4CDGFWC/ref=cm_sw_r_as_gl_apa_gl_i_TZYQDHJJJR786CSTYCJA', 'https://www.amazon.com.br/dp/B098YKFS8P/ref=cm_sw_r_as_gl_apa_gl_i_ERPZBA4WJ3RHV4ARTG6G', 'https://www.amazon.com.br/dp/B098YKFS8P/ref=cm_sw_r_as_gl_apa_gl_i_ERPZBA4WJ3RHV4ARTG6G?linkCode=ml2&tag=painelconstruapi-20']

    item_id_list = []

    for product_link in product_list:
        for string in product_link.strip('/').split('/'):
            if len(string.split('?')[0]) == 10:
                item_id_list.append(string.split('?')[0])
                break
        

    pprint.pprint(get_items(id_list=item_id_list))