import requests
import unittest


class TestStringMethods(unittest.TestCase):

    def test_page_headers(self):
        url = 'http://localhost:80'
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Weather Home', response.text)


if __name__ == '__main__':
    unittest.main()
