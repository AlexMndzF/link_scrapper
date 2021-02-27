import unittest
from unittest.mock import MagicMock

from Utils import GetUrls, HtmlParser, Node


class TestStringMethods(unittest.TestCase):

    def test_get_urls_ok(self):
        thing = HtmlParser()
        thing.get_links = MagicMock(return_value=['a', 'b'])
        url ='google.es'
        GetUrls(thing).get_urls(url=Node(url), deep=2, indentation=0)

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()