import unittest
from unittest.mock import Mock

def get_data(api_client):
    data1 = api_client.get("http://example.com/data1")
    data2 = api_client.get("http://example.com/data2")
    data3 = api_client.get("http://example.com/data3")
    return data1, data2, data3

class TestGetData(unittest.TestCase):
    def test_multiple_returns(self):
        mock_api_client = Mock()
        mock_api_client.get.side_effect = [
            {"id": 1, "value": "data1"},
            {"id": 2, "value": "data2"},
            {"id": 3, "value": "data3"}
        ]

        result = get_data(mock_api_client)

        self.assertEqual(result[0], {"id": 1, "value": "data1"})
        self.assertEqual(result[1], {"id": 2, "value": "data2"})
        self.assertEqual(result[2], {"id": 3, "value": "data3"})

if __name__ == '__main__':
    unittest.main()
