import unittest

from main import parse_filenames


class TestParseFilenames(unittest.TestCase):
    def test_parse_no_space(self):
        actual_result = parse_filenames("abc1,dfg2,rewd,g42w,desti")
        expected_result = ["abc1", "dfg2", "rewd", "g42w", "desti"]
        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
