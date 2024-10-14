import requests, json
from bs4 import BeautifulSoup
from pprint import pprint


def load_soup(URL):
    page_content = None

    while page_content == None:

        try:
            page_content = requests.get(URL, timeout = None, headers={
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36"
                }).content
        except:
            print("Generic Bot - Server failed to respond. Retrying in 6 seconds. Please wait...")

    soup = BeautifulSoup(page_content, 'html.parser')
    # time.sleep(6)

    return soup

def leroymerlin_spider(link):

    print("Generic BOT - Fetching Items to Update Prices")


    # link = "https://loja.kingspan-isoeste.com.br/telha-termica-sanduiche-trapezoidal-aco-superior-e-filme-aluminio-nucleo-em-pir-com-espessura-de-30mm-largura-util-de-01-metro.html"

    soup = load_soup(link)


    try:
        product_name = soup.select("h1.product-title.product-description")[0].text.strip()
    except:
        product_name = ""

    try:
        supplier_code = soup.select("div[data-product-id]")[0]["data-product-id"]
    except:
        supplier_code = ""

    try:
        description = ""
        desc = soup.select("div.product-info-details table > tr")

        for i in desc:
            th = i.select("th")[0].text
            td = i.select("td")[0].text
            
            description += (th + ": ")
            description += (td + "\n")
    except:
        description = ""

    try:
        #select price from span dada-cy="product-price-tag"
            # Encontrar a div que contém os dados do produto
        product_div = soup.find('div', {'data-props': True})
        
        # Extraindo o JSON de dentro do atributo 'data-props'
        data_props = product_div['data-props']
        
        # Converter o JSON em um dicionário Python
        product_data = json.loads(data_props)
        
        # Acessar o preço do produto
        price = product_data['product']['price']
    except:
        price = ""

    try:
        img = soup.select("span[itemprop='image']")[0]["content"]
    except:
        img = ""

    try:
        unit = soup.select("div[data-unit]")[0]["data-unit"]
    except:
        unit = ""

    try:
        manufacturer = ""
        desc = soup.select("div.product-info-details table > tr")
        if len(desc) != 0:
            for i in desc:
                th = i.select("th")[0].text
                td = i.select("td")[0].text
                
                if th == "Marca":
                    manufacturer = td
    except Exception as e:
        print(f"Error on 'manufacturer'{e}")

    if any(i.isdigit() for i in str(price)) is False:
        data = {
            "status": 0
        }
    else:
        
        data = {
            "price": price,
            "product_name": product_name,
            "supplier_code": supplier_code,
            "description": description,
            "unit": unit,
            "image_link": img,
            "manufacturer": manufacturer
        }
    
    return(data)


if __name__ == '__main__':
    """This will be used to test the links sent"""
    links = ["https://www.leroymerlin.com.br/visor-escotilha-para-portas-polido-35-cm_1567302876",
        "https://www.leroymerlin.com.br/visor-escotilha-para-portas-polido-40-cm_1567302575",
        "https://www.leroymerlin.com.br/voltimetro-digital-taramps-vtr-1000_1566939089",
        ]
    
    for link in links:
        pprint(leroymerlin_spider(link))