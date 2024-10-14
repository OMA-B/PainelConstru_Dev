import requests
from bs4 import BeautifulSoup
import re
import time
from pprint import pprint


def load_soup(URL):
    page_content = None
    count=0
    count_limit=3
    while page_content == None:
        count+=1
        try:
            page_content = requests.get(URL, timeout = None, headers={
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36"
                }).content
        except:
            print("Generic Bot - Server failed to respond. Retrying in 6 seconds. Please wait...")
            if page_content==None and count==count_limit: page_content=''

    soup = BeautifulSoup(page_content, 'html.parser')
    # time.sleep(6)

    return soup

def madeiramadeira_spider(link):

    print("Generic BOT - Fetching Items to Update Prices")


    # link = "https://loja.kingspan-isoeste.com.br/telha-termica-sanduiche-trapezoidal-aco-superior-e-filme-aluminio-nucleo-em-pir-com-espessura-de-30mm-largura-util-de-01-metro.html"

    soup = load_soup(link)


    try:
        product_name = soup.select("h1.cav--c-fpAEqe")[0].text.strip()
    except:
        product_name = ""

    try:
        supplier_code = soup.select("span.cav--c-gNPphv.cav--c-gNPphv-epiGtV-textStyle-bodySmallRegular")[0].text.split("ID: ")[1]
    except: 
        supplier_code = ""

    try:
        description = soup.select("div.cav--c-lesPJm.cav--c-lesPJm-ijSrwAU-css")[0].text.split("Descrição")[1]
    except:
        description = ""

    try:
        price = soup.select("span.cav--c-gNPphv.cav--c-gNPphv-iELazp-textStyle-h3Semibold.cav--c-gNPphv-hHqInm-size-h3")[0].text
    except:
        price = ""

    try:
        imgs = soup.select("ul.cav--c-ngEAm > li img")

        img = []
        for i in imgs:
            img.append(i['src'])

        nimg = []
        for i in img:
            if "https://product-hub-prd" in i:
                nimg.append(i)
    except:
        nimg = ""

    unit = ""

    if soup.find(text=re.compile(r"Produto esgotado")) == "Produto esgotado":
        data = {
            "status": 0
        }
    else:
        data = {
            "product_name": product_name,
            "supplier_code": supplier_code,
            "description": description,
            "price": price,
            "unit": unit,
            "image_link": nimg
        }
        
    return(data)


if __name__ == '__main__':
    """This will be used to test the links sent"""
    links = ["https://www.madeiramadeira.com.br/cuba-inox-gourmet-cozinha-sobrepor-embutir-valvula-slx-40-2196324.html?index=prod-madeira-listings",
            "https://www.madeiramadeira.com.br/cuba-inox-dupla-39-x-89cm-c-valvula-de-4-1-2-acabamento-alto-brilho-tramontina-1550703.html?index=prod-madeira-listings",
            "https://www.madeiramadeira.com.br/cuba-pia-inox-quadrada-lux-600x400-2335996.html?index=prod-madeira-listings",
            "https://www.madeiramadeira.com.br/cuba-sobrepor-tramontina-93831-133-aco-inox-acetinado-c-acessorios-torneira-1059991.html?index=prod-madeira-listings",
            "https://www.madeiramadeira.com.br/cuba-aco-inox-430-retangular-standard-56x34-tramontina-1026109.html?index=prod-madeira-listings",
            "https://www.madeiramadeira.com.br/cuba-lr50-embutir-retangular-raio-10-handmade-inox-escovado-2273795.html?index=prod-madeira-listings",
            "https://www.madeiramadeira.com.br/torneira-para-banheiro-de-mesa-1193-globalmedic-2504043.html?id=2504043"]

    
    for link in links:
        pprint(madeiramadeira_spider(link))