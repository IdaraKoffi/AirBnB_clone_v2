import unittest
from models.city import City
from models.state import State

class TestCity(unittest.TestCase):
    def test_City_instantiation(self):
        city = City()
        self.assertIsInstance(city, City)
        self.assertEqual(city.__class__.__name__, "City")
    
    def test_City_attributes(self):
        city = City()
        self.assertTrue(hasattr(city, "state_id"))
        self.assertTrue(hasattr(city, "name"))
    
    def test_City_attributes_type(self):
        city = City()
        self.assertIsInstance(city.state_id, str)
        self.assertIsInstance(city.name, str)
    
    def test_City_attributes_default(self):
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")
