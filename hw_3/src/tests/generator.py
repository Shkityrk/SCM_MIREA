import unittest

from hw_3.src.utils.generator import generate_output


class TestGenerator(unittest.TestCase):

    def test_generate_output(self):
        parsed_data = "begin\n key := 'value';\nend"
        self.assertEqual(generate_output(parsed_data), parsed_data)

if __name__ == '__main__':
    unittest.main()
