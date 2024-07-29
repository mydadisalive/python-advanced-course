import unittest
from unittest.mock import Mock

def process_data(api_client):
    try:
        data = api_client.get("http://example.com/data")
    except Exception as e:
        return str(e)
    return data

class TestProcessData(unittest.TestCase):
    def test_exception(self):
        mock_api_client = Mock()
        mock_api_client.get.side_effect = Exception("Network error")

        result = process_data(mock_api_client)

        self.assertEqual(result, "Network error")

if __name__ == '__main__':
    unittest.main()
