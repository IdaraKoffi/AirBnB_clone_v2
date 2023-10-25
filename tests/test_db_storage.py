import unittest
from models import storage

class TestDBStorage(unittest.TestCase):
    def test_DBStorage_exists(self):
        self.assertIsNotNone(storage)
