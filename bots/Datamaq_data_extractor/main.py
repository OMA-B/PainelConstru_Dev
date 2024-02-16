import time, pprint, json, time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# later use container(s)
company_data_list = []


# get to the home page/the sectors page
driver = Chrome()
driver.get(url='http://www.datamaq.org.br/SearchResult/AdditionalFilter?parentId=undefined&sectorName=undefined&isSegment=undefined&cacheSectorName=undefined')
wait = WebDriverWait(driver=driver, timeout=120)

# gather all under industrial and transversal sector
industries = wait.until(method=EC.presence_of_all_elements_located(locator=(By.CSS_SELECTOR, 'div.container:nth-child(4) div.col-auto input')))

for i, industry in enumerate(industries[23:]):
    # start clicking them one after the other to check out the companies and segments under each industry
    wait.until(method=EC.presence_of_element_located(locator=(By.CSS_SELECTOR, f'div.container:nth-child(4) div.col-auto:nth-child({i+24}) input'))).click()
    # click on companies
    wait.until(method=EC.presence_of_element_located(locator=(By.CSS_SELECTOR, 'div.container:nth-child(6) div.col-auto:nth-child(2) input'))).click()

    # gather all the individual companies and start clicking them one after the other and remember to take note if a company is paid or not
    companies = wait.until(method=EC.presence_of_all_elements_located(locator=(By.CSS_SELECTOR, 'div.container:nth-child(2) tbody tr')))

    count = 0

    for company in companies:
        company_name = company.find_element(By.CSS_SELECTOR, 'td:nth-child(1)').text
        is_paid = company.find_element(By.CSS_SELECTOR, 'td:nth-child(2)').text
        company.click()
        time.sleep(2)
        # gather all the info under the company
        company_detail = wait.until(method=EC.presence_of_element_located(locator=(By.CSS_SELECTOR, 'div.container:nth-child(4)')))
        if is_paid == 'Não':
            driver.execute_script("arguments[0].style.visibility = 'visible';", company_detail)
            time.sleep(2)

        # organize retrieved data
        industry_name = wait.until(method=EC.presence_of_element_located(locator=(By.CSS_SELECTOR, 'div.container:nth-child(3) div.row:nth-child(2) .col'))).text
        address = company_detail.find_element(By.CSS_SELECTOR, 'div.row:nth-child(1) .col').text
        complement = company_detail.find_element(By.CSS_SELECTOR, 'div.row:nth-child(2) .col').text
        neighborhood = company_detail.find_element(By.CSS_SELECTOR, 'div.row:nth-child(3) .col').text
        zip_code = company_detail.find_element(By.CSS_SELECTOR, 'div.row:nth-child(4) .col').text
        city = company_detail.find_element(By.CSS_SELECTOR, 'div.row:nth-child(5) .col').text
        state = company_detail.find_element(By.CSS_SELECTOR, 'div.row:nth-child(6) .col').text

        contact_pack = company_detail.find_element(By.CSS_SELECTOR, 'div.row:nth-child(7)')
        driver.execute_script("arguments[0].style.visibility = 'visible';", contact_pack)
        contact = contact_pack.find_element(By.CSS_SELECTOR, '.col').text
        
        telephone = company_detail.find_element(By.CSS_SELECTOR, 'div.row:nth-child(8) .col').text
        
        mail_pack = company_detail.find_element(By.CSS_SELECTOR, 'div.row:nth-child(9)')
        driver.execute_script("arguments[0].style.visibility = 'visible';", mail_pack)
        mail = mail_pack.find_element(By.CSS_SELECTOR, '.col').text
        
        site = company_detail.find_element(By.CSS_SELECTOR, 'div.row:nth-child(10) .col').text

        extra_info_pack = wait.until(method=EC.presence_of_element_located(locator=(By.CSS_SELECTOR, 'div.container:nth-child(4) > div:nth-child(11)')))
        driver.execute_script("arguments[0].style.visibility = 'visible';", extra_info_pack)
        extra_info = extra_info_pack.text.replace('\n', '   ')
        
        company_data_list.append({
            'transversal_sector': industry_name,
            'company': company_name,
            'address': address,
            'complement': complement,
            'neighborhood': neighborhood,
            'zip_code': zip_code,
            'city': city,
            'state': state,
            'contact': contact,
            'telephone': telephone,
            'mail': mail,
            'site': site,
            'paid': is_paid,
            'extra_info': extra_info
        })
        count += 1
        print(count, industry_name, company_name, is_paid)

        if count % 30 == 0 or count == len(companies):
            with open(file='transversal_companies_data.json', mode='w+') as file:
                json.dump(obj=company_data_list, fp=file)

        print(time.ctime())
        
        driver.back()

    driver.back()
    driver.back()


time.sleep(2)