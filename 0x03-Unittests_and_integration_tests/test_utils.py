#!/usr/bin/env python3
"""
Parameterize a unit test
"""
import unittest
from utils import access_nested_map
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """
    Test access_nested_map function
    """

    @parameterized.expand([
        ({"a": 1, "b": {"c": 2}, "d": {"e": {"f": 3}}}, ["a"], 1),
        ({"a": 1, "b": {"c": 2}, "d": {"e": {"f": 3}}}, ["b", "c"], 2),
        ({"a": 1, "b": {"c": 2}, "d": {"e": {"f": 3}}}, ["d", "e", "f"], 3),
        ({"a": 1, "b": {"c": 2}, "d": {"e": {"f": 3}}}, ["d", "e", "g"], None),
        ({"a": 1, "b": {"c": 2}, "d": {"e": {"f": 3}}}, ["a", "b"], None),
        ({"a": 1, "b": {"c": 2}, "d": {"e": {"f": 3}}}, ["d", "e", "f", "g"], None),
        ({"a": 1, "b": {"c": 2}, "d": {"e": {"f": 3}}}, ["f"], None),
        ({"a": 1, "b": {"c": 2}, "d": {"e": {"f": 3}}}, [], None),
        ({"a": {"b": {"c": {"d": 4}}}}, ["a", "b", "c", "d"], 4),
        ({"a": {"b": {"c": {"d": 4}}}}, ["a", "b", "c"], {"d": 4}),
        ({"a": {"b": {"c": {"d": 4}}}}, ["a", "b"], {"c": {"d": 4}}),
        ({"a": {"b": {"c": {"d": 4}}}}, ["a"], {"b": {"c": {"d": 4}}}),
        ({"a": {"b": {"c": {"d": 4}}}}, ["a", "b", "c", "e"], None),
        ({"a": {"b": {"c": {"d": 4}}}}, ["a", "b", "e"], None),
        ({"a": {"b": {"c": {"d": 4}}}}, ["a", "e"], None),
        ({"a": {"b": {"c": {"d": 4}}}}, ["e"], None),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test access_nested_map function
        """
        try:
            result = access_nested_map(nested_map, path)
        except KeyError:
            result = None
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
