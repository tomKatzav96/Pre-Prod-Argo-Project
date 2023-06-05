import unittest
import sys
sys.path.append(".")
from app.app import app

class TestWeatherApp(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Weather Home', response.data)

    def test_valid_country_input(self):
        response = self.client.post('/', data={'user_input': 'new york'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'New York', response.data)

    def test_valid_city_input(self):
        response = self.client.post('/', data={'user_input': 'los angeles'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Los Angeles', response.data)

    def test_valid_israel_input(self):
        response = self.client.post('/', data={'user_input': 'tel aviv'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Humidity', response.data)

    def test_valid_uppercase_input(self):
        response = self.client.post('/', data={'user_input': 'LONDON'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'England', response.data)

    def test_invalid_numbers_input(self):
        response = self.client.post('/', data={'user_input': '1234235'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Please try another one', response.data)

    def test_invalid_hebrew_input(self):
        response = self.client.post('/', data={'user_input': 'תל אביב'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Please try another one', response.data)

    def test_invalid_empty_input(self):
        response = self.client.post('/', data={'user_input': ''})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Please try another one', response.data)

    def test_invalid_special_characters_input(self):
        response = self.client.post('/', data={'user_input': 'tel!@#()aviv'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Please try another one', response.data)

    def test_invalid_not_exist_input(self):
        response = self.client.post('/', data={'user_input': 'asddgdfhgfhrds'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Please try another one', response.data)

if __name__ == '__main__':
    unittest.main()
