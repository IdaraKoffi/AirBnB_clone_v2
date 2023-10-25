import unittest
from console import HBNBCommand
from models.state import State
from models.place import Place

class TestParamsCreateCommand(unittest.TestCase):
    def test_create_state_with_parameters(self):
        console = HBNBCommand()
        result = console.onecmd('create State name="California"')
        self.assertTrue(result)

        state = State()
        state.reload()
        state_id = state.id
        self.assertEqual(result.strip(), state_id)

    def test_create_place_with_parameters(self):
        console = HBNBCommand()
        result = console.onecmd('create Place city_id="0001" user_id="0001" name="My_little_house" number_rooms=4 number_bathrooms=2 max_guest=10 price_by_night=300 latitude=37.773972 longitude=-122.431297')
        self.assertTrue(result)

        place = Place()
        place.reload()
        place_id = place.id
        self.assertEqual(result.strip(), place_id)
        self.assertEqual(place.city_id, "0001")
        self.assertEqual(place.user_id, "0001")
        self.assertEqual(place.name, "My little house")

if __name__ == '__main__':
    unittest.main()
