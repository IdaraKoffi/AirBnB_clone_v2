import unittest
from console import HBNBCommand

class TestConsoleCommands(unittest.TestCase):
    def test_create_command(self):
        console = HBNBCommand()
        result = console.onecmd("create State")
        self.assertTrue(result.startswith("** value missing **"))

    def test_show_command(self):
        console = HBNBCommand()
        result = console.onecmd("show State 12345")
        self.assertTrue(result.startswith("** no instance found **"))

if __name__ == '__main__':
    unittest.main()
