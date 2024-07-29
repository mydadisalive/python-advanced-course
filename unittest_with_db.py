from unittest import TestCase
from unittest.mock import Mock, patch

class Database:

    def connect(self):
        pass

    def get_data(self):
        pass

class DataProcessor:

    def __init__(self, db: Database):
        self.db = db

    def process(self):
        self.db.connect()
        data = self.db.get_data()
        return data

class TestDataProcessor(TestCase):

    @patch.object(Database, 'connect')
    @patch.object(Database, 'get_data')
    def test_process(self, mock_get_data, mock_connect):
        mock_get_data.return_value = {'key': 'value'}
        db = Database()
        processor = DataProcessor(db)

        result = processor.process()

        mock_connect.assert_called_once()
        mock_get_data.assert_called_once()
        self.assertEqual(result, {'key': 'value'})
