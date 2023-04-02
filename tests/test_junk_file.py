import unittest
from handy_tool.junk_file import _parse_size


class JunkFileTest(unittest.TestCase):
    def test_parse_size(self):
        assert _parse_size("10G") == 10 * 1024
        assert _parse_size("10M") == 10
        assert _parse_size("10G10M") == 10 * 1024 + 10
        assert _parse_size("10") == 10


if __name__ == '__main__':
    unittest.main()
