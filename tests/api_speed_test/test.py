import unittest
import main


class TestProductApi(unittest.TestCase):

    def test_api_speed(self):
        url = 'http://api2.painelconstru.com.br/products/7465/items/'
        data = main.fetch_data(url=url)

        self.assertTrue(data)


    
if __name__ == '__main__':
    unittest.main()