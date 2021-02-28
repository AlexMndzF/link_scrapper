import unittest
from unittest.mock import Mock

import test.settings as st
from Utils import Node
from src.htmlParser import HtmlParser
from src.linkScrapper import LinkScrapper
from requests.exceptions import ConnectionError, MissingSchema


class TestLinkScrapper(unittest.TestCase):

    def test_get_urls_ok(self):
        thing = HtmlParser()
        thing.get_links = Mock(side_effect=st.url_mock)
        url = Node(value='google.es')
        LinkScrapper(thing).get_urls(url=url, deep=3, indentation=0)


class TestHtmlParser(unittest.TestCase):

    def test_get_urls_invalid_host(self):
        url = Node(value='https://www.google.')
        with self.assertRaises(ConnectionError):
            LinkScrapper(HtmlParser()).get_urls(url=url, deep=3, indentation=0)


if __name__ == '__main__':
    unittest.main()
