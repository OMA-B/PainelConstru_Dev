import requests, json


def fetch_data(url):
    # fetch data from API
    response = requests.get(url=url)
    response.raise_for_status()
    data = response.json()
    # getting amount of products returned
    print(f"Amount of products retreived: {len(data['data']['items'])}")

    # store retrieved data
    with open('products.json', mode='w+') as file:
        json.dump(data, file)

    return len(data['data']['items'])
