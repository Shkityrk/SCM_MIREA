import unittest

from hw_3.src.utils.errors import ConfigurationError
from hw_3.src.utils.parser import parse_json


class TestParser(unittest.TestCase):

    def test_parse_dict(self):
        data = {"key1": "value1", "key2": 123}
        expected = "begin\n key1 := 'value1';\n key2 := 123;\nend"
        self.assertEqual(parse_json(data), expected)

    def test_parse_array(self):
        data = ["value1", 123, {"key": "value"}]
        expected = "{ 'value1' . 123 . begin\n key := 'value';\nend }"
        self.assertEqual(parse_json(data), expected)

    def test_invalid_data_type(self):
        with self.assertRaises(ConfigurationError):
            parse_json(None)

if __name__ == '__main__':
    unittest.main()
