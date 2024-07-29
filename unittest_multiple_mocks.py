import unittest
from unittest.mock import patch
import requests

def get_multiple_data():
    data1 = requests.get('http://example.com/data1').json()
    data2 = requests.get('http://example.com/data2').json()
    return data1, data2

class TestGetMultipleData(unittest.TestCase):

    @patch('requests.get')
    def test_get_multiple_data(self, mock_get):
        # Set up the mock to return different values each time it is called
        mock_get.side_effect = [
            unittest.mock.Mock(status_code=200, json=lambda: {'data': 'value1'}),
            unittest.mock.Mock(status_code=200, json=lambda: {'data': 'value2'}),
        ]

        data1, data2 = get_multiple_data()

        self.assertEqual(data1, {'data': 'value1'})
        self.assertEqual(data2, {'data': 'value2'})

        # Verify the calls
        self.assertEqual(mock_get.call_count, 2)
        mock_get.assert_any_call('http://example.com/data1')
        mock_get.assert_any_call('http://example.com/data2')

if __name__ == '__main__':
    unittest.main()
