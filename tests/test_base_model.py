import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_create_instance(self):
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)

    def test_id_generation(self):
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_created_at_and_updated_at(self):
        obj = BaseModel()
        self.assertIsNotNone(obj.created_at)
        self.assertIsNotNone(obj.updated_at)
        self.assertEqual(obj.created_at, obj.updated_at)

    def test_to_dict_method(self):
        obj = BaseModel()
        obj_dict = obj.to_dict()

        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)

    def test_custom_attributes(self):
        obj = BaseModel()
        obj.name = "Test Name"
        obj.value = 42

        self.assertEqual(obj.name, "Test Name")
        self.assertEqual(obj.value, 42)

    def test_str_representation(self):
        obj = BaseModel()
        obj.name = "Test Name"
        obj.value = 42

        obj_str = str(obj)
        self.assertIn("[BaseModel]", obj_str)
        self.assertIn("'name': 'Test Name'", obj_str)
        self.assertIn("'value': 42", obj_str)

if __name__ == '__main__':
    unittest.main()
