"""Tests for the :mod:`hello` helper module."""

import unittest

from hello import hello


class HelloTest(unittest.TestCase):
    def test_hello(self) -> None:
        self.assertEqual(hello(), "hello")


if __name__ == "__main__":
    unittest.main()
