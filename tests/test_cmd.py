import unittest
from app.command import Cmd


class TestSum(unittest.TestCase):
    _keyboard_input = 'ease connect --set http://localhost:5050 --no-output --user admin --password 1234  --retry 5'
    _cmd = Cmd('ease', 'Error', 'Info', ['connect', 'ping'])

    def test_should_cmd_correctly_parse_command(self):
        parsed = self._cmd.parse(self._keyboard_input)

        self.assertEqual(len(parsed), 5)

    # Standalone command has no value for example: --no-output
    def test_should_cmd_correctly_parse_standalone_command(self):
        parsed = self._cmd.parse(self._keyboard_input)

        self.assertEqual(len(parsed['standalone']), 1)
        self.assertEqual('--no-output', parsed['standalone'][0])

    def test_should_return_empty_dict_when_option_not_exists(self):
        _invalid_input = 'ease search -f 4'
        parsed = self._cmd.parse(_invalid_input)

        self.assertEqual(1, len(parsed))


if __name__ == '__main__':
    unittest.main()
