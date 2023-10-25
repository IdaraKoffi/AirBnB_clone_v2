import unittest
from models.state import State

class TestState(unittest.TestCase):
    def test_State_instantiation(self):
        state = State()
        self.assertIsInstance(state, State)
        self.assertEqual(state.__class__.__name__, "State")
    
    def test_State_attributes(self):
        state = State()
        self.assertTrue(hasattr(state, "name"))
    
    def test_State_attributes_type(self):
        state = State()
        self.assertIsInstance(state.name, str)
    
    def test_State_attributes_default(self):
        state = State()
        self.assertEqual(state.name, "")
