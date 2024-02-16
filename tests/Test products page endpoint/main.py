import requests

def fetch_data(url):
    # fetch data from API
    response = requests.get(url=url)
    response.raise_for_status()
    data = response.json()
    # getting amount of products returned
    try:
        len(data['data'])
        print(f"\nSuccess status: {data['success']} for URL - {url}")
        
        try: print(f"Message: {data['message']} from the URL - {url}")
        except: pass
    except KeyError:
        print(f"\nProduct Data could not be retreived from {url} \nSuccess status: {data['success']}")
        return data['success']
    else:
        return data['success']