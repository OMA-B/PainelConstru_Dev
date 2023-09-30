import unittest, main

product_api_list = ['similar', 'featured', 'prices', 'prices2', 'images', 'images2']

class TestProductApi(unittest.TestCase):
         
    def test_api_similar(self):
        data = main.fetch_data(url='https://api2.painelconstru.com.br/products/similar/21')
        self.assertTrue(data)

    def test_api_featured(self):
        data = main.fetch_data(url='https://api2.painelconstru.com.br/products/featured/')
        self.assertTrue(data)

    def test_api_prices(self):
        data = main.fetch_data(url='https://api2.painelconstru.com.br/products/prices?format=json&id=16&id=17&id=18&id=188&id=19&id=20&id=202&id=21&id=212&id=22&id=258&id=305&id=425&id=433&id=5844&id=6349&id=6352&id=6353&id=6354&id=6363')
        self.assertTrue(data)

    def test_api_prices2(self):
        data = main.fetch_data(url='https://api2.painelconstru.com.br/products/prices?format=json&id=407&id=408&id=410&id=5690&id=5692&id=5693&id=5832&id=5986&id=6276&id=6763&id=6764&id=6765&id=6766')
        self.assertTrue(data)

    def test_api_images(self):
        data = main.fetch_data(url='https://api2.painelconstru.com.br/products/images?format=json&id=16&id=17&id=18&id=188&id=19&id=20&id=202&id=21&id=212&id=22&id=258&id=305&id=425&id=433&id=5844&id=6349&id=6352&id=6353&id=6354&id=6363')
        self.assertTrue(data)

    def test_api_images2(self):
        data = main.fetch_data(url='https://api2.painelconstru.com.br/products/images?format=json&id=407&id=408&id=410&id=5690&id=5692&id=5693&id=5832&id=5986&id=6276&id=6763&id=6764&id=6765&id=6766')
        self.assertTrue(data)

    
if __name__ == '__main__':
        for api in product_api_list:
            test_to_run = unittest.TestLoader().loadTestsFromName(name=f'test_api_{api}', module=TestProductApi)
            unittest.TextTestRunner(verbosity=2).run(test=test_to_run)