import time, pprint, json
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


# container variable(s)
products_data_container = []

counter = 0

# set up driver
options = ChromeOptions()
options.add_argument('--disable-popup-blocking')
driver = Chrome(options=options)
# got to desired simecs webpage
driver.get(url='https://simecs.com.br/empresas-simecs?prod=1&produto_nome=&produto_segmento=')
wait = WebDriverWait(driver=driver, timeout=30)

time.sleep(3)
try:
    wait.until(method=EC.presence_of_element_located(locator=(By.CSS_SELECTOR, '.cc-btn.cc-ALLOW'))).click()
    driver.find_element(By.CSS_SELECTOR, 'button#rd-close_button-l8j5nmni').click()
except: pass

# gather all products
all_products = wait.until(method=EC.presence_of_all_elements_located(locator=(By.CSS_SELECTOR, '.item_prod')))[139:]

for i, product in enumerate(all_products):

    time.sleep(2)

    try: driver.find_element(By.CSS_SELECTOR, 'button#rd-close_button-l8j5nmni').click()
    except: pass
    # get product name
    product_name = wait.until(method=EC.presence_of_element_located(locator=(By.CSS_SELECTOR, f'.item_prod:nth-child({i+141}) .m-b-20'))).text
    # click one product after another
    # try:
    wait.until(method=EC.presence_of_element_located(locator=(By.CSS_SELECTOR, f'.item_prod:nth-child({i+141}) button'))).click()
    # except Exception: pass 
        # click button to go back
        # wait.until(method=EC.presence_of_element_located(locator=(By.CSS_SELECTOR, '.modal-footer button'))).click()
        # continue
    try: driver.find_element(By.CSS_SELECTOR, 'button#rd-close_button-l8j5nmni').click()
    except: pass
    # extract information within
    try:
        try: driver.find_element(By.CSS_SELECTOR, 'button#rd-close_button-l8j5nmni').click()
        except: pass

        product_companies = wait.until(method=EC.presence_of_all_elements_located(locator=(By.CSS_SELECTOR, 'section .m-b-30')))

        # sort and store fetched data
        for c, company in enumerate(product_companies):
            
            try: driver.find_element(By.CSS_SELECTOR, 'button#rd-close_button-l8j5nmni').click()
            except: pass

            product_details = wait.until(method=EC.presence_of_all_elements_located(locator=(By.CSS_SELECTOR, f'section .m-b-30:nth-child({c+1}) .m-b-0')))

            # sort and store fetched data
            data_dict = {}
            data_dict.update({'product_name': product_name})

            time.sleep(2)

            for product_d in product_details:
                data_dict.update({product_d.text.split(': ')[0]: product_d.text.split(': ')[1]})
                # print(product_d.text.split(': '))
            
            products_data_container.append(data_dict)

        try: driver.find_element(By.CSS_SELECTOR, 'button#rd-close_button-l8j5nmni').click()
        except: pass

        counter += 1
        # save in json format
        if counter % 5 == 0 or counter == len(all_products):
            with open(file='products_companies_data.json', mode='w+') as file:
                json.dump(products_data_container, file)

        print(i+1, product_name)
    except Exception: pass

    # import pdb; pdb.set_trace()
    # click button to go back
    wait.until(method=EC.presence_of_element_located(locator=(By.CSS_SELECTOR, '.modal-footer button'))).click()
    driver.refresh()

time.sleep(5)

# pprint.pprint(products_data_container)