#!/usr/bin/python3
"""test Base Model"""
import unittest
import os
from os import getenv
from models import storage
from models.base_model import BaseModel
from models.state import State
import pep8
import MySQLdb
import datetime


class TestBaseModel(unittest.TestCase):
    """this will test Basemodel class"""

    @classmethod
    def setUpClass(cls):
        """setup for the test"""
        cls.base = BaseModel()
        cls.base.name = "Kev"
        cls.base.num = 20
        if getenv("HBNB_TYPE_STORAGE") == "db":
            cls.db = MySQLdb.connect(getenv("HBNB_MYSQL_HOST"),
                                     getenv("HBNB_MYSQL_USER"),
                                     getenv("HBNB_MYSQL_PWD"),
                                     getenv("HBNB_MYSQL_DB"))
            cls.cursor = cls.db.cursor()

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.base
        if getenv("HBNB_TYPE_STORAGE") == "db":
            self.db.close()

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

<<<<<<< HEAD
    def test_pep8_BaseModel(self):
        """Testing for pep8"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/base_model.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_checking_for_docstring_BaseModel(self):
        """checking  docstrings"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_method_BaseModel(self):
        """chekcing the basemodel """
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))
        self.assertTrue(hasattr(BaseModel, "delete"))

    def test_init_BaseModel(self):
        """test if  base  type BaseModel"""
        self.assertTrue(isinstance(self.base, BaseModel))

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == 'db', "can't run if\
                     storage is set to file")
    def test_save_BaseModel(self):
        """test the save works"""
        self.base.save()
        self.assertNotEqual(self.base.created_at, self.base.updated_at)

    def test_to_dict_BaseModel(self):
        """test the dictionary works"""
        base_dict = self.base.to_dict()
        self.assertEqual(self.base.__class__.__name__, 'BaseModel')
        self.assertIsInstance(base_dict['created_at'], str)
        self.assertIsInstance(base_dict['updated_at'], str)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == 'file', "can't run if\
                     storage is set to file")
    def test_attributes_v2_BaseModel(self):
        """Test attributes from the v2"""
        attributes = storage.attributes()["BaseModel"]
        o = BaseModel()
        for k, v in attributes.items():
            self.assertTrue(hasattr(o, k))
            self.assertEqual(type(getattr(o, k, None)), v)

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == 'file', "can't run if\
                     storage is set to file")
    def test_to_dict_v2_BaseModel(self):
        """Test _dict() method v2"""
        base_dict = self.base.to_dict()
        self.assertFalse('_sa_instance_state' in base_dict.keys())

if __name__ == "__main__":
=======
    def test_default(self):
        """ """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """ """
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """ """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """ """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """ """
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    def test_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)

    class TestConsoleCreate(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()
        self.obj_id = None
        self.saved_stdout = sys.stdout
        sys.stdout = StringIO()

    def tearDown(self):
        sys.stdout = self.saved_stdout
        if self.obj_id:
            HBNBCommand._all = {}

    def test_create_base_model(self):
        # Test creating a BaseModel instance with parameters
        self.console.onecmd('create BaseModel name="My House" number=42')
        output = sys.stdout.getvalue().strip()
        self.assertTrue(len(output) == 36)  # Check if a valid ID is returned
        self.obj_id = output
        obj = HBNBCommand._all["BaseModel.{}".format(output)]
        self.assertEqual(obj.name, "My House")
        self.assertEqual(obj.number, 42)

    def test_create_invalid_class(self):
        # Test creating an instance of an invalid class
        self.console.onecmd('create InvalidClass')
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")

if __name__ == '__main__':
>>>>>>> 5f50dd86a4f6927a24072fcef5e8b75746d96949
    unittest.main()
